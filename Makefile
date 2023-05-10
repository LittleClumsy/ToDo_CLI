PACKAGE_VERSION := $(shell cat version.txt)
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
	@echo $(major).$(minor).$(newPatch) > version.txt
	@echo "New version: $(major).$(minor).$(newPatch)"
	@echo "sonar.projectKey=LittleClumsy_ToDo_CLI\nsonar.organization=littleclumsy\n\n# This is the name and version displayed in the SonarCloud UI.\nsonar.projectName=ToDo_CLI\nsonar.projectVersion=$(major).$(minor).$(newPatch)\n\n# Path is relative to the sonar-project.properties file. Replace "" by "/" on Windows.\nsonar.sources=source/todo_cli/\nsonar.python.coverage.reportPaths=source/coverage.xml\nsonar.python.version=3.10" > $(SONAR_FILE)
	@echo "Updated SonarCloud version"

minor:
	@echo "Current version: $(PACKAGE_VERSION)"
	@echo "Bumping minor version..."
	@echo $(major).$(newMinor).$(patch) > version.txt
	@echo "New version: $(major).$(newMinor).$(patch)"
	@echo "sonar.projectKey=LittleClumsy_ToDo_CLI\nsonar.organization=littleclumsy\n\n# This is the name and version displayed in the SonarCloud UI.\nsonar.projectName=ToDo_CLI\nsonar.projectVersion=$(major).$(minor).$(newPatch)\n\n# Path is relative to the sonar-project.properties file. Replace "" by "/" on Windows.\nsonar.sources=source/todo_cli/\nsonar.python.coverage.reportPaths=source/coverage.xml\nsonar.python.version=3.10" > $(SONAR_FILE)
	@echo "Updated SonarCloud version"

major:
	@echo "Current version: $(PACKAGE_VERSION)"
	@echo "Bumping major version..."
	@echo $(newMajor).$(minor).$(patch) > version.txt
	@echo "New version: $(newMajor).$(minor).$(patch)"
	@echo "sonar.projectKey=LittleClumsy_ToDo_CLI\nsonar.organization=littleclumsy\n\n# This is the name and version displayed in the SonarCloud UI.\nsonar.projectName=ToDo_CLI\nsonar.projectVersion=$(major).$(minor).$(newPatch)\n\n# Path is relative to the sonar-project.properties file. Replace "" by "/" on Windows.\nsonar.sources=source/todo_cli/\nsonar.python.coverage.reportPaths=source/coverage.xml\nsonar.python.version=3.10" > $(SONAR_FILE)
	@echo "Updated SonarCloud version"
