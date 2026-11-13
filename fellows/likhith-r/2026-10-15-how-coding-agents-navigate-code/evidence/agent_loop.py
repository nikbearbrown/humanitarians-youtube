"""agent_loop.py — executable evidence for B03–B07 of claude-hai-coding-agents.

Builds a small toy shop repo in a temp dir, then REPLAYS the tool calls a coding
agent makes on it (a scripted replay, not a live model): list the tree, search
for the bug's keyword, read the matching file, make one scoped edit, run the
tests, read the failure, make a second edit, run the tests again. Every command
is real and its output is printed verbatim; the reel shows these outputs.

    uv run --no-project --with "pytest==8.3.3" python evidence/agent_loop.py > evidence/agent_loop.out.txt
"""
import os, shutil, subprocess, sys, tempfile, textwrap

FILES = {
    "README.md": "# shop\nA tiny store backend.\n",
    "shop/__init__.py": "",
    "shop/cart.py": textwrap.dedent('''\
        from shop.pricing import apply_discount


        def cart_total(prices, coupon_percent=0):
            subtotal = sum(prices)
            return apply_discount(subtotal, coupon_percent)
        '''),
    "shop/pricing.py": textwrap.dedent('''\
        TAX_RATE = 0.0


        def apply_discount(price, percent):
            """Take `percent` % off `price`."""
            return price - percent


        def with_tax(price):
            return price * (1 + TAX_RATE)
        '''),
    "shop/inventory.py": "STOCK = {}\n\n\ndef in_stock(sku):\n    return STOCK.get(sku, 0) > 0\n",
    "shop/users.py": "def display_name(user):\n    return user.get('name', 'guest')\n",
    "shop/emails.py": "def receipt_subject(order_id):\n    return f'Your order {order_id}'\n",
    "shop/shipping.py": "def shipping_cost(weight_kg):\n    return 5 if weight_kg < 1 else 9\n",
    "tests/__init__.py": "",
    "tests/test_cart.py": textwrap.dedent('''\
        from shop.cart import cart_total


        def test_no_coupon():
            assert cart_total([40, 60]) == 100


        def test_ten_percent_coupon():
            assert cart_total([40, 60], coupon_percent=10) == 90
        '''),
    "tests/test_pricing.py": textwrap.dedent('''\
        from shop.pricing import apply_discount


        def test_discount_rounds_to_cents():
            assert apply_discount(19.99, 15) == 16.99
        '''),
    "tests/test_shipping.py": "from shop.shipping import shipping_cost\n\n\ndef test_light():\n    assert shipping_cost(0.5) == 5\n",
}

BUG = "Bug report: a 10% coupon takes $10 off instead of 10%."


def run(cmd, cwd, shown=None):
    print(f"$ {shown or cmd}")
    p = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    print((p.stdout + p.stderr).replace(cwd + "/", "").rstrip())
    print()
    return p.returncode


def edit(root, path, old, new):
    """A scoped edit: replace one exact string, which must occur exactly once."""
    f = os.path.join(root, path)
    src = open(f).read()
    assert src.count(old) == 1, f"edit target not unique in {path}"
    open(f, "w").write(src.replace(old, new))
    print(f"EDIT {path}")
    print(f"- {old.strip()}")
    print(f"+ {new.strip()}")
    print(f"(1 line changed, {src.count(chr(10)) - 1} lines untouched)")
    print()


def main():
    root = os.path.realpath(tempfile.mkdtemp(prefix="shop-"))
    for rel, body in FILES.items():
        os.makedirs(os.path.join(root, os.path.dirname(rel)), exist_ok=True)
        open(os.path.join(root, rel), "w").write(body)
    py = sys.executable
    print(BUG)
    print()
    print("## STEP 1 — explore")
    run("find . -name '*.py' -not -name '__init__.py' | sort", root)
    print("## STEP 2 — targeted search")
    run("grep -rn 'discount' --include='*.py' shop tests", root)
    run("sed -n '4,6p' shop/pricing.py", root)
    print("## STEP 3 — scoped edit")
    edit(root, "shop/pricing.py", "    return price - percent\n",
         "    return price * (1 - percent / 100)\n")
    print("## STEP 4 — verify")
    rc1 = run(f"{py} -m pytest -q -p no:cacheprovider --tb=line", root, "pytest -q --tb=line")
    print("## STEP 5 — iterate")
    edit(root, "shop/pricing.py", "    return price * (1 - percent / 100)\n",
         "    return round(price * (1 - percent / 100), 2)\n")
    rc2 = run(f"{py} -m pytest -q -p no:cacheprovider --tb=line", root, "pytest -q --tb=line")
    print(f"exit codes: first run {rc1}, second run {rc2}")
    shutil.rmtree(root)


if __name__ == "__main__":
    main()
