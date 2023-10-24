# Data Engineering Coding Challenge
##  How to install
### local bash:
poetry check env:
`$ poetry env info --path`

Install all dependencies:
`$ poetry install`

 Build App:
`$ poetry build`

Add dev dependencies:
`$ poetry add --dev pytest coverage`

Run on locally:
`$ poetry run python g_challenge_de/src/main.py`

Run tests with HTML viewer:
`$ poetry run pytest tests --doctest-modules --junitxml=junit/test-results.xml --cov=. --cov-report=xml --cov-report=html`
  
### Docker-compose:

Build app:
`poetry build`

Build img docker-compose
`docker-compose build`

Run:
`docker-compose up -d`

### Data base ER diagram


![](https://raw.githubusercontent.com/fmorocoima/g_challenge_de/main/g_challenge_de/src/docs/diagrams/er_diagram-Page-1.jpg)
