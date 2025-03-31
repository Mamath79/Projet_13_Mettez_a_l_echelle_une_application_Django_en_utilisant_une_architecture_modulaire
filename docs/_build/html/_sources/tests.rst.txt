Tests
=====

This project uses `pytest` for testing and `coverage` to measure test coverage. All tests are located in dedicated `tests` folders within each Django app.

How to Run Tests
----------------

To execute the full test suite:

```bash
pytest --ds=oc_lettings_site.settings
```

This command will automatically discover and run all tests in the `lettings`, `profiles`, and `oc_lettings_site` apps.

To run tests with coverage and generate a report:

```bash
pytest \
  --ds=oc_lettings_site.settings \
  --cov=. \
  --cov-report=term-missing \
  --cov-report=html
```

This will:
- Display coverage info in the terminal.
- Generate an `htmlcov/` folder with a visual HTML report.

Test Coverage Requirement
--------------------------

The CI/CD pipeline requires a **minimum coverage of 80%** to pass.
If coverage is below this threshold, the pipeline will fail.

Testing Guidelines
-------------------

- Use `pytest` style for writing test functions.
- Place your test files in `tests/` folders inside each app.
- Keep test cases modular and independent.
- Mock external services (like Sentry) when needed.

Examples
--------

Run tests only for the `profiles` app:

```bash
pytest profiles/tests
```

Run a single test module:

```bash
pytest lettings/tests/test_models.py
```

For detailed info, refer to the `pytest` and `coverage` documentation.


