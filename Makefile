define coverage_teardown
    coverage report
	coverage html
	coverage xml
endef

test:
	coverage run --source='.' manage.py test
	$(call coverage_teardown)
