# Google Search Service (API Server)

A highly-efficient python backend API server to Google
- Scrapes the results from Google on the user's behalf, and arrange it neatly as JSON, ready to be transformed
- This can help e.g Quant Companies to

1. making efficient queries to the google search service, given a search term
2. saving the results of the queries in a database, so they can be parsed
- Google search service returns back a HTML document
- This HTML document can be parsed with e.g a HTML parser, or an ML HTML model, to extract information from the results
- This can be expanded further into even a SaaS
  - https://www.scraperapi.com/solutions/serp-data-collection/?utm_source=google&utm_medium=cpc&utm_id=20804240837_162812098464&utm_term=serp%20apis&utm_mt=p&utm_device=d&utm_campaign=geoT1-s-UseCases&gad_source=1&gclid=Cj0KCQjwk6SwBhDPARIsAJ59Gwfpp-n3Q7t_e4s4xof8uMvG4cjkVWUrwoCoY8OsWLq-RlxyvKuyejcaAiX4EALw_wcB

## Dependency Manager: `poetry`
- `pyproject.toml` defines the dependencies this project uses, and makes it easy for us to install dependencies
- `poetry.lock` locks the dependencies the team uses. This ensures the dependency versions are the same across all collaborators

## (Optional) Code Formatter - `black`
- Automatically formats source code in this project, to make it neat

## (Optional) Linter - `ruff`
- Catches code smells automatically in this project, to avoid fundamental mistakes

## (Optional) Type-checker - `mypy`
- Catches trivial type errors which can be avoided even before running the project
- This ensures our customers don't get bugs which could be avoided easily