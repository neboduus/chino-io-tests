.PHONY: unit-test
unit-test:
	env/bin/python3 -m pytest -vv --log-cli-level=DEBUG
