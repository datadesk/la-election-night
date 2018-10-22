test:
	flake8 la_election_night
	coverage run tests.py
	coverage report -m
