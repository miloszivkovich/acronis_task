# Task for Acronis done by Miloš Živković


# Setup & Installation:

1. Clone the repository
- git clone <your-repo-url>
- cd <your-project-directory>

2. Create a virtual environment and activate it
- python -m venv venv
- .\venv\Scripts\Activate.ps1

3. Install dependencies
- pip install -r requirements.txt
- Required packages: 
    - pytest
    - pytest-bdd
    - playwright
    - pytest-html

4. Install Playwright Browsers
- playwright install

5. Running the Tests
- pytest -v 
or can be called specifically by
- pytest tests/step_defs.py


# Test Structure:

- feature/: Contains .feature files written in Gherkin (features and test scenarios).
- tests/: Contains step_defs.py which maps Gherkin steps to Python code.
- pages/: Contains Page Object Models (POMs) for interacting with the web pages.
- conftest.py: Contains Pytest fixtures.
- pytest.ini: Configuration file to automatically generate the HTML report.
- requirements.txt: Lists Python dependencies, and helps with installation


# Task explanations:

- Tests should be easily scalable with new features and new scenarios
- Explicit waits were used due to Kiwi.com’s flaky behavior with airport pickers, could have been solved in a better way
- report.html is generated after test suite is run
- I have added one more test to show scalability
- Scipt can be run in a Dockerfile 

# Docker environment:
- Setup container image 
- build and run tests within container image


# CI/CD server:
- push the project to server repository
- create a .yaml file 
- define setting up Python
- define installing dependencies and installing browsers
- define running tests and archiving the reports
