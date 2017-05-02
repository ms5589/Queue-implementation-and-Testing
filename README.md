# Queue-implementation-and-Testing
This is an implementation of Queue data structure provided with the unit testing using PyTest and Hypothesis
- Install pytest plugin and run the project with the pytest command.
- To check the code coverage of testing,
  use command as below:

pytest --cov-fail-under=100 --cov=. --cov-report=term-missing -s --cov-config=coverage.rc --timeout=180 --timeout_method=thread test_impl.py

