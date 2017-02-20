install:
	pip3 install -r requirements.txt

test:
	nosetests tests

clean:
	sudo find . -name '*.pyc' -delete
