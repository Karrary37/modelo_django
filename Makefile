define coverage_teardown
    coverage report
	coverage html
	coverage xml
endef
$(call coverage_teardown)