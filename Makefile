init:
	pip install -r requirements.txt

test:
	python3 -m 'nose'	
	
clean:
	find . -name '*.pyc' -delete
