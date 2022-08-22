
dist:
	source venv/bin/activate; \
	pip install --upgrade setuptools wheel twine; \
	python setup.py sdist bdist_wheel; \
	python -m twine upload dist/*

testdist:
	source venv/bin/activate; \
	pip install --upgrade setuptools wheel twine; \
	python setup.py sdist bdist_wheel; \
	python -m twine upload --repository testpypi dist/*

wheel:
	python setup.py bdist_wheel

clean:
	rm -rf *.egg-info build dist

