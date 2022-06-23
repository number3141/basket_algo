from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def parsePageInHTML():
  """Парсит страницу в HTML-файл bask.html"""
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.get('https://www.flashscore.com.ua/basketball/usa/nba/results/')
  fileBask = open('../bask.html', 'w', encoding='utf-8')
  fileBask.write(driver.page_source)
  fileBask.close()


