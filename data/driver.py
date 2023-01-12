### Файл для определения брауззера 
# 
# 
# Main
from selenium import webdriver

# Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Firefox 
from webdriver_manager.firefox import GeckoDriverManager

class Driver(): 
    """В зависимости от выбранного браузера настраивает драйвера"""
    def __init__(self, checkBrowser):
        if checkBrowser == 'Google': 
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif checkBrowser == 'Firefox': 
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print(f'Выбор браузера успешен. Вы выбрали {checkBrowser}')
    
    def getDriver(self): 
        return self.driver
