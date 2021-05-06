from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path='C:\selenium browser driver\chromedriver_win32\chromedriver.exe')
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path='C:\selenium browser driver\geckodriver-v0.29.0-win64\geckodriver.exe')
    else:
        driver = webdriver.Ie(executable_path='C:\selenium browser driver\IEDriverServer_Win32_3.150.1\IEDriverServer.exe')
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########## Ptest HTML Report ##########

#it is hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers Commerce'
    config._metadata['Tester'] = 'George'

#it is hook of delet/modify environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

