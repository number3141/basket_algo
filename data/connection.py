from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .driver import Driver


class Connection(): 
    """
    Класс, устанавливающий соединение с url c помощью selenium 

    Аргументы
    ----------
    - url - url с которым нужно определить соединение 
    """
    def __init__(self, url) -> None:
        self.url = url
        self.driver = Driver().getDriver()
       

    def startConnect(self): 
        """Начинает соединение с url
        TODO - Сделать выбор браузера (browser)
        """
        self.driver.get(self.url)
        self.main_status = self.driver.requests[0].response.status_code
        while self.main_status != 200:
            self.driver.refresh() 
            

    def closeConnect(self): 
        self.driver.quit()
    

    def __repr__(self) -> str:
        return f'Соединение с сайтом {self.url}'
    

class ContentEngine():    
    """
    Класс для работы с контентом сайта

    Атрибуты
    ----------
    - connection - Экземпляр объекта Connection 
    """
    def __init__(self, connection) -> None:
        self.connection = connection
        self.content = ''
    
    
    def get_content(self): 
        if self.content == '':
            self.content = self.connection.driver.page_source
        return self.content


class ContentEngineBasket(ContentEngine):
    """
    Класс для работы с контентом сайта flaschscore 

    Аргументы 
    ----------
    - connection - Экземпляр объекта Connection
    - date - Дата, до которой нужно найти все матчи
    """
    def __init__(self, connection) -> None:
        super().__init__(connection)


    def push_down_btn_while_is_not_it(self, it, css_class_btn = 'event__more--static'): 
        """
        Метод, нажимающий кнопку "Листать вниз", пока не найдёт матч с текстом it 

        Аргументы
        ----------
        - it (str) - Текст, найдя который, функция вернёт разметку страницы 
        - css_class_btn - CSS-класс кнопки, на которую нужно нажимать
        """
        try:
            while True:
                # Если на странице есть матч с датой пользователя 
                if self.connection.driver.find_element(by=By.XPATH, value = f"""//div[contains(text(), '{it}')]"""): 
                    break

                self.connection.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.element = WebDriverWait(self.connection.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, f".{css_class_btn}"))
                )

                self.element.click()

                # Пока у элемента не пропадёт класс loading  
                WebDriverWait(self.connection.driver, 10).until_not(
                    EC.text_to_be_present_in_element_attribute(
                    (By.TAG_NAME, "body"), "class", "loading")
                )
        finally:
            return self.connection.driver.page_source


# if __name__ == '__main__': 
    # newCon = BaskConnection('https://www.flashscorekz.com/basketball/usa/nba/results/')
    # print(help(newCon.takeContent))


