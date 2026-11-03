"""graph_demo.py — executable evidence for claude-hai-graph-databases.

Builds ONE toy friendship network twice: in Kuzu (an embedded graph database that
speaks Cypher) and in SQLite (relational: a people table + a friendships table of
foreign keys). Runs the same questions both ways and prints the real output that
the reel's B06/B07 put on screen.

Run (throwaway env, nothing installed into the repo):
  uv run --no-project --python 3.12 --with kuzu==0.11.3 python evidence/graph_demo.py
"""
import sqlite3, tempfile, os, kuzu

PEOPLE = ["Ana", "Ben", "Cai", "Dev", "Eli", "Fay", "Gus"]
FRIENDS = [("Ana", "Ben"), ("Ana", "Cai"), ("Ben", "Dev"), ("Cai", "Eli"),
           ("Dev", "Fay"), ("Eli", "Fay"), ("Fay", "Gus")]

# --- graph: nodes + edges stored directly -----------------------------------
db = kuzu.Database(os.path.join(tempfile.mkdtemp(), "g"))
g = kuzu.Connection(db)
g.execute("CREATE NODE TABLE Person(name STRING, PRIMARY KEY(name))")
g.execute("CREATE REL TABLE FRIENDS_WITH(FROM Person TO Person)")
for p in PEOPLE:
    g.execute("CREATE (:Person {name: $n})", {"n": p})
for a, b in FRIENDS:
    g.execute("MATCH (a:Person {name: $a}), (b:Person {name: $b}) CREATE (a)-[:FRIENDS_WITH]->(b)", {"a": a, "b": b})

def cypher(q):
    r = g.execute(q); rows = []
    while r.has_next(): rows.append(r.get_next())
    print(q); print("  ->", rows); return rows

print(f"kuzu {kuzu.__version__}")
cypher("MATCH (a:Person {name: 'Ana'})-[:FRIENDS_WITH]->(b:Person) RETURN b.name ORDER BY b.name")
cypher("MATCH (a:Person {name: 'Ana'})-[:FRIENDS_WITH*3]->(c:Person) RETURN DISTINCT c.name")

# --- relational: the same edges as foreign keys ------------------------------
s = sqlite3.connect(":memory:")
s.execute("CREATE TABLE people(id INTEGER PRIMARY KEY, name TEXT)")
s.execute("CREATE TABLE friendships(person_id INT REFERENCES people(id), friend_id INT REFERENCES people(id))")
s.executemany("INSERT INTO people VALUES (?, ?)", list(enumerate(PEOPLE, 1)))
ids = {n: i for i, n in enumerate(PEOPLE, 1)}
s.executemany("INSERT INTO friendships VALUES (?, ?)", [(ids[a], ids[b]) for a, b in FRIENDS])
SQL3 = """SELECT DISTINCT p.name FROM friendships f1
JOIN friendships f2 ON f2.person_id = f1.friend_id
JOIN friendships f3 ON f3.person_id = f2.friend_id
JOIN people p ON p.id = f3.friend_id
WHERE f1.person_id = (SELECT id FROM people WHERE name = 'Ana')"""
print(f"sqlite {sqlite3.sqlite_version}")
print(SQL3); print("  ->", s.execute(SQL3).fetchall())
