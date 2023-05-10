setup:
	pipenv install --dev

ci:
	pipenv install

clean:
	pipenv clean
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf htmlcov
	rm -rf src/testing/tasks.json
	rm -rf src/testing/unit/tasks.json

coverage: test
	@pipenv run coverage html 
	@pipenv run coverage xml
	@open http://0.0.0.0:8000/
	@cd htmlcov && python -m http.server 8000

lint:
	@pipenv run pylint todo_cli/

unit-test:
	@pipenv run pytest -v tests/unit/

test:
	@pipenv run python -m pytest -q tests/ --cov=todo_cli/ --cov-report term-missing

update:
	@pipenv clean
	@pipenv update
	@pipenv requirements --dev > requirements.txt

pipeline:
	@make test
	@make lint