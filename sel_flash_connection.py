from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from present_controll.resource_connection import ResourseConnection



# Соединение с сайтом 
class HTMLConnection(ResourseConnection): 
    def start_connect(self):
        self.install_service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.install_service)

        self.driver.get(self.path)

        self.main_status = self.driver.requests[0].response.status_code

        while self.main_status != 200:
            self.driver.refresh() 


    def close_connect(self): 
        self.driver.quit()
    

    def get_content(self):
        return self.driver.page_source






if __name__ == '__main__':
    t = HTMLConnection('https://www.flashscorekz.com/basketball/usa/nba/results/')
    t.start_connect()
    print(t.get_content())
    t.close_connect()
    print('Завершил!')