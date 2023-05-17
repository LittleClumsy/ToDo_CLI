PACKAGE_VERSION := $(shell cat VERSION)
major := $(shell echo $(PACKAGE_VERSION) | cut -d'.' -f 1)
minor := $(shell echo $(PACKAGE_VERSION) | cut -d'.' -f 2)
patch := $(shell echo $(PACKAGE_VERSION) | cut -d'.' -f 3)
newPatch := $(shell expr $(patch) + 1)
newMinor := $(shell expr $(minor) + 1)
newMajor := $(shell expr $(major) + 1)
SONAR_FILE :=$(shell find ./ -iname sonar-project.properties -type f)

patch:
	@echo "Current version: $(PACKAGE_VERSION)"
	@echo "Bumping patch version..."
	@echo $(major).$(minor).$(newPatch) > VERSION
	@echo "New version: $(major).$(minor).$(newPatch)"
	@echo "sonar.projectKey=LittleClumsy_ToDo_CLI\nsonar.organization=littleclumsy\n\n# This is the name and version displayed in the SonarCloud UI.\nsonar.projectName=ToDo_CLI\nsonar.projectVersion=$(major).$(minor).$(newPatch)\n\n# Path is relative to the sonar-project.properties file. Replace "" by "/" on Windows.\nsonar.sources=todo_cli/\nsonar.python.coverage.reportPaths=coverage.xml\nsonar.python.version=3.10" > $(SONAR_FILE)
	@echo "Updated SonarCloud version"

minor:
	@echo "Current version: $(PACKAGE_VERSION)"
	@echo "Bumping minor version..."
	@echo $(major).$(newMinor).$(patch) > VERSION
	@echo "New version: $(major).$(newMinor).$(patch)"
	@echo "sonar.projectKey=LittleClumsy_ToDo_CLI\nsonar.organization=littleclumsy\n\n# This is the name and version displayed in the SonarCloud UI.\nsonar.projectName=ToDo_CLI\nsonar.projectVersion=$(major).$(newMinor).$(patch)\n\n# Path is relative to the sonar-project.properties file. Replace "" by "/" on Windows.\nsonar.sources=todo_cli/\nsonar.python.coverage.reportPaths=coverage.xml\nsonar.python.version=3.10" > $(SONAR_FILE)
	@echo "Updated SonarCloud version"

major:
	@echo "Current version: $(PACKAGE_VERSION)"
	@echo "Bumping major version..."
	@echo $(newMajor).$(minor).$(patch) > VERSION
	@echo "New version: $(newMajor).$(minor).$(patch)"
	@echo "sonar.projectKey=LittleClumsy_ToDo_CLI\nsonar.organization=littleclumsy\n\n# This is the name and version displayed in the SonarCloud UI.\nsonar.projectName=ToDo_CLI\nsonar.projectVersion=$(newMajor).$(minor).$(patch)\n\n# Path is relative to the sonar-project.properties file. Replace "" by "/" on Windows.\nsonar.sources=todo_cli/\nsonar.python.coverage.reportPaths=coverage.xml\nsonar.python.version=3.10" > $(SONAR_FILE)
	@echo "Updated SonarCloud version"

setup:
	pipenv install --dev

setup-build:
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