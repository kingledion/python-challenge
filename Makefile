lint:
	poetry run black .
	poetry run flake8 .
	poetry run isort --profile black .
	poetry run mypy .

server:
	@poetry run python ./dev/devserver.py

test:
	@poetry run pytest