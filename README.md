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

## Creating a virtual environment

```commandline
poetry shell
```

## Installing dependencies

```commandline
poetry install
```

## (Optional) Code Formatter - `black`
- Automatically formats source code in this project, to make it neat

```commandline
black .
```

## (Optional) Linter - `ruff`
- Catches code smells automatically in this project, to avoid fundamental mistakes

```commandline
ruff --fix .
```

## (Optional) Type-checker - `mypy`
- Catches trivial type errors which can be avoided even before running the project
- This ensures our customers don't get bugs which could be avoided easily

```commandline
mypy .
```

## Spinning up a PostgreSQL local database server

Install PostgreSQL@15 with brew

```commandline
brew install postgresql@15
```

Spin up PostgreSQl database server locally, with `brew services`

```commandline
brew services start postgresql@15
```

Connect to your local postgresql server

```
psql -d postgres
```

Create the database

```sql
CREATE DATABASE google_search_service
```

Use alembic database migration tool, to create the remaining tables

```commandline
alembic upgrade head
```

This will create the tables for you in your local postgresql database

## (Optional) Run unit tests

```commandline
pytest unit_tests
```

## (Optional) Creating a new table with alembic

### Step 1: Define the new table in `database_management/tables.py`

### Step 2: Generate the alembic upgrade script

This generates a new file in `database_management/versions`

This same file will be used to migrate databases locally, allowing your team members to easily replicate the same postgresql setup as everyone

```commandline
alembic revision --autogenerate -m "Your commit message"
```

## Running the local server on Port 8080

```commandline
python main.py
```

## Making a sample request

POST `http://localhost:8080/perform_search`

Input JSON:

```json
{
	"search_term": "coffee"
}
```

Sample output:

```commandline
{
	"search_id": "54cb9e17-8442-400a-9364-0b90c70cda93",
	"search_term": "coffee",
	"response": "some_le_big_html :D",
	"status_code": 200,
	"is_deleted": false,
	"created_at": "2024-03-31 11:54:36"
}
```

![Image](./images/sample_result.png)

## TODOs:
- [ ] Implement a HTML parser, to extract the search results from raw HTML
  - [ ] This can be done with a simple ada model from the GPT3.5 series
  - [ ] Alternative, to save costs (OpenAI credits are expensive), we can deploy a simple open sourced LLM to do so
- We don't use a simple HTMLParser, as Google is notorious for making it's HTML difficult to parse with simple vanilla HTML scrapers (e.g with selenium-webdriver)
- [ ] Write integration tests for GoogleSearchDAO