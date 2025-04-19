VENV_PATH = .venv
PIP = $(VENV_PATH)/bin/pip3
PYTHON = $(VENV_PATH)/bin/python3
PACKAGE_NAME = math_undie
DIST_DIR = dist

.DEFAULT_GOAL := build

.PHONY: test build setup clear help upload update req

# Regra para criar o venv se não existir
$(VENV_PATH):
	python3 -m venv $(VENV_PATH)

# Instala dependências
deps: $(VENV_PATH)

help:
	@echo "Makefile para gerenciamento de pacotes Python"
	@echo ""
	@echo "Alvos disponíveis:"
	@echo "  make build       # Cria o pacote"
	@echo "  make test        # Executa os testes"
	@echo "  make upload      # Faz upload do pacote para o TestPyPI"
	@echo "  make clear       # Remove artefatos antigos de build"

clear:
	rm -rf $(DIST_DIR) ./**/*.egg-info
	@echo "Old build artifacts removed."

setup: $(VENV_PATH)
	@. $(VENV_PATH)/bin/activate && pip install --upgrade pip --break-system-packages
	@. $(VENV_PATH)/bin/activate && pip3 install -r requirements --break-system-packages

build: setup
	python3 -m build && $(MAKE) test

upload: clear
	$(MAKE) build
	python3 -m twine upload --repository testpypi $(DIST_DIR)/* --verbose --config-file .pypirc
	@echo "Package uploaded to TestPyPI."
	$(MAKE) req

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
	@python3 -m unittest discover -s tests -p '*.py' -v
