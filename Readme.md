# 🧪 SauceDemo QA Automation Framework

This is a UI test automation framework built with **Pytest** and **Selenium**, using the **Page Object Model** design pattern. It covers core scenarios for [saucedemo.com](https://www.saucedemo.com), provided as part of a QA/QC technical assignment.

---

##  Project Structure

```
Saucedemo/
├── TestCases/             # All test case files
├── PageObjects/           # Page Object classes
├── Utilities/             # Logger, config reader, etc.
├── testData/              # Test input data (valid/invalid users)
├── reports/               # HTML reports (excluded via .gitignore)
├── conftest.py            # Browser setup and Pytest hooks
├── requirements.txt       # All required packages
├── README.md              # Project documentation
```

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

### 1️ Clone the Repo

```bash
git clone https://github.com/vidurbh/SaucedemoAutomationFramework.git
cd SaucedemoAutomationFramework
```

### 2️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  How to Run Tests

###  Basic Command

```bash
pytest -v
```

### ✅ With HTML Report

```bash
pytest -v --html=reports/report.html
```

### ✅ Cross-browser Testing

```bash
pytest -v --browser chrome
```

Supported browsers: `chrome`, `firefox`, `edge`

---

##  Test Scenarios Covered

-  **Login**
  - Valid credentials
  - Invalid credentials
  - Locked-out user

-  **Sorting Items**
  - Sort by Name (A-Z, Z-A)
  - Sort by Price (Low to High, High to Low)

-  **Verify Products Displayed**
  - Ensure all products are visible on inventory page

-  **Add to Cart & Validate Totals**
  - Add products
  - Check price summary and tax
  - Validate final total

-  **Checkout Process**
  - Step 1: Enter info
  - Step 2: Summary validation
  - Cancel button validation
  - Finish button validation

-  **Logout**

-  **Negative and Edge Case Tests**
  - Empty credentials
  - Wrong credentials
  - Remove items from cart

---

##  Notes

- All test credentials are publicly listed on [saucedemo.com](https://www.saucedemo.com).
- `standard_user` is used for most successful flows.
- Reports and `.pyc` cache are ignored via `.gitignore`.

---

##  Author

**Vidurbh Raj**  
QA Engineer | Python | Selenium | Automation  
[GitHub](https://github.com/vidurbh)  
