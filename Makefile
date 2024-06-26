define coverage_teardown
    coverage report
	coverage html
	coverage xml
endef

setup-database-tests:
	python manage.py makemigrations --settings=core.testing
	python manage.py migrate --settings=core.testing

test:
	coverage run ./manage.py test --keepdb --settings=core.testing
	$(call coverage_teardown)