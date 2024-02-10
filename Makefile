setup:
	pipenv install --dev

setup-build:
	pipenv install

clean: Pipfile.lock
	pipenv clean
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf htmlcov
	rm -rf ./dist
	rm -rf ./build
	rm -rf ./todo.spec
	rm -rf ./todo_cli.egg-info
	rm -rf ./.mypy_cache

coverage: test
	@pipenv run coverage html 
	@pipenv run coverage xml
	@open http://0.0.0.0:8000/
	@cd htmlcov && python -m http.server 8000

lint:
	@pipenv run pylint todo_cli/
	@echo "Linting Tests..."
	@pipenv run pylint tests/

unit-test:
	@pipenv run pytest -v tests/unit/

test:
	@pipenv run python -m pytest -v tests/ --cov=todo_cli/ --cov-report term-missing

update:
	@pipenv clean
	@pipenv update
	@pipenv requirements --dev > requirements.txt

pipeline:
	@make test
	@make lint
	@make build

build:
	@pipenv run pyinstaller --onefile todo.py
	@pipenv run python -m build .

requirements:
	@pipenv requirements > requirements.txt
	@pipenv requirements --dev > requirements.dev.txt 