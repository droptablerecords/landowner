init:
	pip install -r requirements.txt

test:
	nose2 tests

build:
	python setup.py sdist bdist_wheel