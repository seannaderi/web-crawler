init:
	pip install -r requirements.txt

test:
	nosetests test

#clean-pyc: 
#	find . -name '*.pyc' -exec rm --force {} +
#	find . -name '*.pyo' -exec rm --force {} +
#	find . -name '*~' -exec rm --force {} +
