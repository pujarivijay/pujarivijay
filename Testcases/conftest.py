import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeservice

@pytest.fixture(scope='function', autouse=True)
def setup(request):
    driver = webdriver.Chrome(service=chromeservice(ChromeDriverManager().install()))
    driver.get("https://www.goibibo.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
