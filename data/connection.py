from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .driver import Driver


class Connection(): 
    def __init__(self, url) -> None:
        self.url = url


    def start_connect(self): 
        raise NotImplementedError(
            f"Создайте метод start_connect в классе {self.__class__.__name__}"
        )
    

    def close_connect(self): 
        raise NotImplementedError(
            f"Создайте метод close_connect в классе {self.__class__.__name__}"
        )
    

    def get_content(self):
        raise NotImplementedError(
            f"Создайте метод get_content в классе {self.__class__.__name__}"
        )


class Connection_Selenium(Connection): 
    """
    Класс, устанавливающий соединение с url c помощью selenium 

    Аргументы
    ----------
    - url - url с которым нужно определить соединение 
    """
    def __init__(self, url) -> None:
        super().__init__(url)
        self.driver = Driver().getDriver()
       

    def start_connect(self): 
        """Начинает соединение с url
        TODO - Сделать выбор браузера (browser)
        """
        self.driver.get(self.url)
        self.main_status = self.driver.requests[0].response.status_code
        while self.main_status != 200:
            self.driver.refresh() 
            

    def close_connect(self): 
        self.driver.quit()
    

    def get_content(self):
        return self.driver.page_source
    

class Interface_Scraper_HTML():
    """
    Класс, создающий интерфейс для скрапперов сайта, которые ищут нужный HTML
    
    Для работы каждого метода требуется рабочее соединение (Connection).   
    Возможны дополнительные параметры
    
    """
    def get_result_flashcsore(self, connection, date): 
        return Scraper_HTML_Selenium_Flashscore(connection).get_need_html(it = date) 
        
 
class Scraper_HTML(): 
    def __init__(self, connection) -> None:
        self.connection = connection

    def get_need_html(self): 
        raise NotImplementedError(
            f'Установите метод get_need_html у класса {self.__class__.__name__}'
        )


class Scraper_HTML_Selenium_Flashscore(Scraper_HTML): 
    def __init__(self, connection) -> None:
        super().__init__(connection)


    def get_need_html(self, it, css_class_btn = 'event__more--static'): 
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


