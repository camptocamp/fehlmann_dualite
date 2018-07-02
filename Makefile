all: build


.venv/timestamp: build_requirements.txt requirements.txt Makefile
	/usr/bin/virtualenv --python=/usr/bin/python3 .venv
	.venv/bin/pip install --disable-pip-version-check --upgrade -r requirements.txt -r build_requirements.txt
	touch $@


.PHONY: lint
lint: .venv/timestamp
	.venv/bin/flake8 fehlmann_dualite tests


.PHONY: mypy
mypy: .venv/timestamp
	.venv/bin/mypy --ignore-missing-imports --strict-optional --disallow-untyped-defs dualite_transnumerique


.PHONY: build
build: lint mypy test
	.venv/bin/pip3 install --disable-pip-version-check -e .


.PHONY: test
test:
	rm -rf reports/coverage
	.venv/bin/pytest -vv --cov=dualite_transnumerique --junitxml reports/ut.xml --color=yes tests; \
	status=$$?; \
	.venv/bin/coverage html -d reports/coverage && \
	.venv/bin/junit2html reports/ut.xml reports/ut.html && \
	exit $$status


.PHONY: release
release: build
	rm -rf dualite_transnumerique.egg-info build dist dualite_transnumerique.egg-info
	.venv/bin/python ./setup.py bdist_wheel
	.venv/bin/twine upload dist/*.whl

