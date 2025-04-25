VENV_PATH = .venv
PIP = pip3
PYTHON = python3
PACKAGE_NAME = math_undie
DIST_DIR = dist

.DEFAULT_GOAL := build

.PHONY: test build setup clear help upload update req

help:
	@echo "Makefile para gerenciamento de pacotes Python"
	@echo ""
	@echo "Alvos disponíveis:"
	@echo "  make build       # Cria o pacote"
	@echo "  make test        # Executa os testes"
	@echo "  make upload      # Faz upload do pacote para o TestPyPI"
	@echo "  make clear       # Remove artefatos antigos de build"

clear:
	rm -rf $(DIST_DIR) ./**/*.egg-info ./**/__pycache__ ./**/**/__pycache__
	@echo "Old build artifacts removed."

setup:
	@. .venv/bin/activate && pip3 install --upgrade pip --break-system-packages
	@. .venv/bin/activate && pip3 install -r requirements --break-system-packages


build:
	PYTHONPATH=src python3 -m build && $(MAKE) test

upload: clear
	$(MAKE) build
	python3 -m twine upload --repository testpypi $(DIST_DIR)/* --verbose --config-file .pypirc
	@echo "Package uploaded to TestPyPI."
	$(MAKE) req_update

update:
	$(eval CURRENT_VERSION = $(shell grep -o 'version = ".*"' pyproject.toml | awk -F'= "' '{print $$2}' | sed 's/"$$//'))
	$(eval MAJOR = $(shell echo $(CURRENT_VERSION) | awk -F'.' '{print $$1}'))
	$(eval MINOR = $(shell echo $(CURRENT_VERSION) | awk -F'.' '{print $$2}'))
	$(eval PATCH = $(shell echo $(CURRENT_VERSION) | awk -F'.' '{print $$3}'))
	$(eval NEW_VERSION=$(MAJOR).$(MINOR).$(shell echo $$(( $(PATCH) + 1 ))))

	@sed -i '' 's/^version = .*/version = "$(NEW_VERSION)"/' pyproject.toml
	$(MAKE) upload

req_update:
	@. $(VENV_PATH)/bin/activate && pip freeze > requirements
	@echo "requirements atualizado."

test:
	@PYTHONPATH=src python3 -m unittest discover -s tests/* -p '*.py' -v

exercises:
	@PYTHONPATH=src python3 -m unittest discover -s book-exercises/* -p '*.py' -v