clean:
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf htmlcov

coverage: test
	@pipenv run coverage html 
	@pipenv run coverage xml


unit-test:
	@pipenv run pytest -v src/testing/unit/ --cov

test:
	@pipenv run pytest -v src/testing/ --cov=src/ --cov-report term-missing

update:
	@pipenv update
	@pipenv requirements > requirements.txt