dev-setup:
	pipenv install --dev

setup:
	pipenv install

clean:
	pipenv clean
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf htmlcov

coverage:
	@pipenv run pytest -q src/testing/
	@pipenv run coverage html 
	@pipenv run coverage xml
	@open http://0.0.0.0:8000/
	@cd htmlcov && python -m http.server 8000

lint:
	@pipenv run pylint src/

unit-test:
	@pipenv run pytest -v src/testing/unit/ --cov=src/

test:
	@pipenv run pytest -q src/testing/ --cov=src/ --cov-report term-missing

update:
	@pipenv clean
	@pipenv update
	@pipenv requirements --dev > requirements.txt

pipeline:
	@make test
	@make lint