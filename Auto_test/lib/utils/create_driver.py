import pytest
from selenium.webdriver import Chrome,Firefox,Ie
def get_driver_instance():
    browser_type=pytest.config.option.browser
    system_info=pytest.config.option.system
    url_info=pytest.config.option.url
    if system_info == 'windows':
        if browser_type != 'safari':
            driver=Chrome("./browser-servers/chromedriver.exe")
        elif browser_type == 'firefox':
            driver=Firefox("./browser_type/geckodriver.exe")
        elif browser_type == 'ie':
            driver=Ie("./browser_type/IEDriverServer.exe")
    elif system_info == 'mac':
        pass
    if url_info == 'test':
        driver.get("http://localhost/login.do")
    elif url_info == 'prod':
        driver.get("https://demo.actitime.com/login.do")
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver