import pytest
from Tools.scripts.pathfix import rep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def initialize_browser(browser):

    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching CHROME BROWSER.........")

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        print("Launching FIREFOX BROWSER.........")
    return driver

def pytest_addoption(parser):  # this will get value from CLI /HOOKS
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # this will return browser value to setup method
    return request.config.getoption("--browser")



















































































































































































"""@pytest.fixture()
def log_on_failure(request):
    yield
    item= request.node
    if item.rep_call.failed:



@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):
    outcome= yield
    setattr(item,"rep_" + rep.when,rep)
    return rep"""



####### pytest HTML REPORT ########
# hook for adding environment info to HTML report
"""def pytest_configure(config):
    config.metadata['Project name'] = 'Kirthi_Technologies'
    config.metadata['Module name'] = 'Home page'
    config.metadata['Tester'] = 'Deepak'


# hook for delete/modify the environment info to HTML report
@pytest.mark.optinalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)"""
