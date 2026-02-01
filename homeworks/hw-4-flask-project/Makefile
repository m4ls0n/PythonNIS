PIP := venv/bin/pip
PYTHON3 := venv/bin/python3
TESTS := venv/bin/pytest
MYPY := venv/bin/mypy

clear:
	rm -rf venv

venv:
	python3 -m venv venv

install_requirements:
	${PIP} install -r requirements.txt

run:
	${PYTHON3} server.py

test:
	${TESTS} -v test_controllers.py
	
check_types:
	${MYPY} server.py controllers.py test_controllers.py