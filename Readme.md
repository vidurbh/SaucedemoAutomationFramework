# 🧪 SauceDemo QA Automation Framework

This is a UI test automation framework built with **Pytest** and **Selenium**, using the **Page Object Model** design pattern. It covers core scenarios for [saucedemo.com](https://www.saucedemo.com), provided as part of a QA/QC technical assignment.

---

##  Project Structure

Saucedemo/
├── TestCases/ # All test case files
├── PageObjects/ # Page Object classes
├── Utilities/ # Logger, config reader, etc.
├── testData/ # Test input data (valid/invalid users)
├── reports/ # HTML reports (excluded via .gitignore)
├── conftest.py # Browser setup and Pytest hooks
├── requirements.txt # All required packages
├── README.md # Project documentation



---

##  Tech Stack

- Python 3
- Pytest
- Selenium
- Page Object Model
- Pytest HTML (`pytest-html`)
- Parallel execution with `pytest-xdist` (optional)

---

##  How to Set Up

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/saucedemo-qa-assignment.git
cd saucedemo-qa-assignment


2. Install Dependencies

Basic Command
pip install -r requirements.txt

With HTML Report
pytest -v --html=reports/report.html

Cross-browser (Optional)
pytest -v --browser chrome


```
Test Scenarios Covered
Login

Valid/invalid credentials

Locked-out user

Sorting items

A-Z, Z-A, Price Low-High, High-Low

Verify Products Displayed

Add to Cart & Validate Total

Checkout Process

Including Cancel and Finish button flows

Logout

Negative and Edge Case Tests

Long inputs, removing items, back button behavior, etc.

```


