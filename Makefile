clean:
	rm -rf .pytest_cache
	rm -rf .coverage

unit-test:
	@pipenv run pytest -v src/testing/unit/ --cov

update:
	@pipenv update
	@pipenv requirements > requirements.txt