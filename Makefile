.PHONY: test ship

test:
	flake8 la_election_night
	coverage run tests.py
	coverage report -m

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing
