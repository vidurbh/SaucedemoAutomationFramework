from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome", 
        help="Browser to run tests: chrome | firefox | edge"
    )

@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser").lower()

    if browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    return driver
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)