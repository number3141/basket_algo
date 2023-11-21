from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

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
    

    def get_content(self, date_str):
        return self.get_need_html(date_str)


    def get_need_html(self, it): 
        """
        Метод, нажимающий кнопку "Листать вниз", пока не найдёт матч с текстом it 

        Аргументы
        ----------
        - it (str) - Текст, найдя который, функция вернёт разметку страницы 
        """
        self.wait = WebDriverWait(self.driver, 7)
        self.driver.maximize_window() # For maximizing window
        # Если на странице есть матч с датой пользователя 

        replace_dot_date = f"{it}.2023".replace('.', ' ')

        a = datetime.strptime(replace_dot_date, "%d %m %Y")
        now_date = datetime.now()

        for _ in range((now_date - a).days // 10):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.element = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".event__more--static"))
            )

            self.element.click()

            # Пока у элемента не пропадёт класс loading  
            self.wait.until_not(
                EC.text_to_be_present_in_element_attribute(
                (By.TAG_NAME, "body"), "class", "loading")
            )
        else: 
            return self.driver.page_source




if __name__ == '__main__':
    t = HTMLConnection('https://www.flashscorekz.com/basketball/usa/nba/results/')
    t.start_connect()
    print(t.get_content('04.11'))
    t.close_connect()
    print('Завершил!')