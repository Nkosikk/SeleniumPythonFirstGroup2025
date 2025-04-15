# SauceDemo Automation Testing Project

This project is an automated testing framework for the SauceDemo web application. It is built using Python and Selenium WebDriver, with Pytest as the test runner. The framework is designed to be modular, scalable, and easy to maintain.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Tests](#running-the-tests)
- [Test Configuration](#test-configuration)
- [Allure Reporting](#allure-reporting)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview
. ├── Pages/ │ ├── loginPage.py # Page Object Model for the login page ├── Utils/ │ ├── readProperties_Login.py # Utility to read configuration properties ├── tests/ │ ├── conftest.py # Pytest fixtures and setup │ ├── test_Login.py # Test cases for login functionality ├── README.md # Project documentation ├── requirements.txt # Python dependencies
The purpose of this project is to automate the login functionality of the SauceDemo application. It includes:

- Testing the login page with valid credentials.
- Modular Page Object Model (POM) design for better maintainability.
- Cross-browser testing support (Chrome, Edge, Safari).
- Integration with Allure for detailed test reporting.

---

## Technologies Used

- **Programming Language**: Python
- **Frameworks**: Selenium WebDriver, Pytest
- **Reporting Tool**: Allure
- **Browser Drivers**: ChromeDriver, EdgeDriver, SafariDriver

---

## Project Structure