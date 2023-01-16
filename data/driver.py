### Файл для определения браузера 
# 
# selenium 4.x
# Main
from selenium import webdriver

# Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Firefox 
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class Driver(): 
    """В зависимости от выбранного браузера настраивает драйвера"""
    def __init__(self, checkBrowser):
        if checkBrowser == 'Google': 
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif checkBrowser == 'Firefox': 
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print(f'Выбор браузера успешен. Вы выбрали {checkBrowser}')
    
    def getDriver(self): 
        return self.driver
