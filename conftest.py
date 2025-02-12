import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--browser_name',
                        action='store',
                        default='chrome',
                        help="Choose browser: '--browser_name=chrome''")
    
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language: ec or ru")



@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")
    user_browser_name = request.config.getoption("browser_name")

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    if (user_browser_name == 'chrome'):
        browser = webdriver.Chrome(options=options)
    elif user_browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # options_firefox = OptionsFirefox()
        # options_firefox.set_preference("intl.accept_languages", user_language)
        # browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome")
    
    yield browser
    browser.quit()