PYTHON       = python3.8
VENVDIR      = ./.env

help:
	@echo "Usage:\n"
	@echo "        make <target>\n"
	@echo "Where <target> is one of:\n"
	@echo "        venv     create a venv with necessary tools"
	@echo "        clean    remove $(VENVDIR) directory if exists\n"
	
venv:
	@if [ -d $(VENVDIR) ] ; then \
		echo "venv already exists.-"; \
		echo "- To recreate it, remove it first with \`make clean\`.-"; \
	else \
		$(PYTHON) -m venv $(VENVDIR); \
		$(VENVDIR)/bin/python3 -m pip install -U pip setuptools; \
		$(VENVDIR)/bin/python3 -m pip install .; \
		echo "- The venv has been created in the \`$(VENVDIR)\` directory.- "; \
		echo "- Type \`source $(VENVDIR)/bin/activate\` to activate venv.-"; \
	fi

clean:
	@rm -rf $(VENVDIR)
	@echo "Removed directory \`$(VENVDIR)\`."
