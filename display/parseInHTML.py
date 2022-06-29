from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from bs4 import BeautifulSoup
class SoupFromHTML():
  def __init__(self, url='https://www.flashscore.com.ua/basketball/usa/nba/results/') -> None:
    self.url = url 
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(self.url)
    self.soup = BeautifulSoup(self.driver.page_source, 'lxml')
    
  def getSoup(self): 
    return self.soup

