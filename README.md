#  Data Engineering Coding Challenge

`$ poetry env info --path`

Install all dependencies:

`$ poetry install`

Add new dependencies:

`$ poetry add fastapi`

Add dev dependencies:

`$ poetry add --dev pytest coverage`

Run on locally:

`$ poetry run python g_challenge_de/src/main.py`

Run tests with HTML viewer:

`$ poetry run pytest tests --doctest-modules --junitxml=junit/test-results.xml --cov=. --cov-report=xml --cov-report=html`