# Frictional log — CI/CD & GitHub Actions

## 2026-11-05 — the project update, in two aspect ratios

**What I was working on.** Setting up a GitHub Actions CI pipeline to run Pytest and build our Docker images on every push.

**What I tried, and what I expected.** 
- I created the `ci.yml` file, set it to run on `ubuntu-latest`, installed `pytest`, and pushed to GitHub. I expected a clean, green checkmark on my first run.

**Where it resisted, and what I did next.** 
- The pipeline immediately crashed with a `ModuleNotFoundError: No module named 'app'`. Because GitHub Actions checks out the code into a raw Ubuntu runner, Python's module pathing got confused. I had to ensure the runner's working directory was correctly aligned with the `app/` folder.
- The Pytest suite also failed because the GitHub runner didn't have the environment variables (`GATEKEEPER_SECRET_KEY`, `ALERT_WEBHOOK_URL`) that normally live locally in my `docker-compose.yml`. I had to manually inject dummy environment variables into the YAML step so FastAPI wouldn't crash on startup during the tests.

**What Claude contributed, and what I did with it.** 
- Mine: The logic for the `test_api.py` testing suite.
- Claude's: The YAML syntax for injecting `env:` variables directly into the GitHub Actions run step to satisfy FastAPI's `os.getenv()` requirements.

**What I understand now, and what I still do not.**
- Understood: Cloud CI runners are completely blank slates. You cannot assume they have any configuration, environment variables, or pathing that exists on your local laptop. You have to explicitly declare everything.