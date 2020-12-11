PYTHON = python3

.PHONY: init test

test:
	py.test tests

init:
	@echo "installing requirements..."
	pip install -r requirements.txt
	@echo "All done! Now you can run the application:"
	@echo ""
	@echo "    python gitmass.py"
	@echo ""

help:
	@echo "Installing requirements and setting up the project:"
	@echo "make init"
	@echo ""
	@echo "Running tests"
	@echo "make test"
	@echo ""
	@echo "Running the project"
	@echo "make run"
	@echo ""
	@echo "Usage help"
	@echo "./gitmass.py --help"
	@echo ""