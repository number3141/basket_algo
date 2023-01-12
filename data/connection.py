# from seleniumwire import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

from .driver import Driver


class Connection(): 
    def __init__(self, url, browser) -> None:
        self.url = url 
        self.browser = browser
        self.startConnect()
        self.takeContent()
        self.closeConnect()
        

    def startConnect(self): 
        """Начинает соединение с url"""
        self.driver = Driver(self.browser).getDriver()
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)   
        self.mainStatus = self.driver.requests[0].response.status_code
        while self.mainStatus != 200:
            self.driver.refresh() 
            

    def takeContent(self): 
        """Забирает контент со страницы"""       
        try:
            while self.driver.find_element(By.CSS_SELECTOR, '.event__more--static'): 
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.driver.find_element(By.CSS_SELECTOR, '.event__more--static').click()
        except: 
            print('Вы на дне!')
        self.content = self.driver.page_source
    

    def getContent(self): 
        return self.content
    

    def closeConnect(self): 
        self.driver.quit()
    

    def __repr__(self) -> str:
        return f'Соединение с сайтом {self.url}'
    

if __name__ == '__main__': 
    newCon = Connection()
    print(newCon)