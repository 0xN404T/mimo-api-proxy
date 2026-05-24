install:
	pip install -r requirements.txt

check:
	python -m py_compile app.py

run:
	python app.py
