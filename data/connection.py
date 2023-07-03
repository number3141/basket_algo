from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .driver import Driver


class Connection(): 
    def __init__(self, url, date) -> None:
        self.url = url 
        self.date = date
        self.startConnect()
        self.takeContent()
        self.closeConnect()
        

    def startConnect(self): 
        """Начинает соединение с url
        TODO - Сделать выбор браузера (browser)
        """
        self.driver = Driver().getDriver()
        self.driver.get(self.url)
           
  
        self.main_status = self.driver.requests[0].response.status_code
        while self.main_status != 200:
            self.driver.refresh() 
            

    def takeContent(self): 
        """Забирает контент со страницы"""    
        try:
            while True:
                # Если на странице есть матч с датой пользователя 
                if self.driver.find_element(by=By.XPATH, value = f"""//div[contains(text(), '{self.date}')]"""): 
                    break

                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".event__more--static"))
                )

                self.element.click()

                # Пока у элемента не пропадёт класс loading  
                WebDriverWait(self.driver, 10).until_not(
                    EC.text_to_be_present_in_element_attribute(
                    (By.TAG_NAME, "body"), "class", "loading")
                )
        finally:
            self.content = self.driver.page_source
    

    def getContent(self): 
        return self.content
    

    def closeConnect(self): 
        self.driver.quit()
    

    def __repr__(self) -> str:
        return f'Соединение с сайтом {self.url}'
    


# class ContentFinder(): 
#     def __init__(self) -> None:
        


if __name__ == '__main__': 
    newCon = Connection('https://www.flashscorekz.com/basketball/usa/nba/results/')
    print(help(newCon.takeContent))