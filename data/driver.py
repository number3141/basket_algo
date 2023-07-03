### Файл для определения браузера 
# 
# selenium 4.x

from seleniumwire import webdriver

# Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Driver(): 
    """
    Класс для автоматической загрузки драйвера 

    Свойства: 
    ----------

    self.install_service = Служебный класс, который отвечает за запуск и остановку `chromedriver`.
    self.driver = Установленный драйвер Google 
    
    TODO - В зависимости от выбранного браузера настраивает драйвера"""


    def __init__(self):
        self.install_service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.install_service)
        
     
    def getDriver(self): 
        "Возвращает драйвер"
        return self.driver


if __name__ == '__main__':
    dr = Driver('fr')
    help(dr.getDriver)