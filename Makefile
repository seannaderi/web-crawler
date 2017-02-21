install:
	pip3 install -r requirements.txt

test:
	nosetests tests

clean:
	sudo find . -name '*.pyc' -delete
	sudo find . -name '__pycache__'  -delete 

all:
	make test && make clean
