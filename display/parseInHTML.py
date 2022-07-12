from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium import webdriver
from bs4 import BeautifulSoup

class SoupFromHTML():
  def __init__(self, date, url='https://www.flashscore.com.ua/basketball/usa/nba/results/') -> None:
    self.date = date
    self.url = url 
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
  
  def __repr__(self) -> str:
    return f'Объект - {self.soup}'
  
  def startConnect(self): 
    self.driver.get(self.url)   
    self.mainStatus = self.driver.requests[0].response.status_code
    while self.mainStatus != 200:
      self.driver.refresh() 
      print('Перезагрузил!')

  def startMakeSoup(self): 
    self.content = self.driver.page_source
    self.soup = BeautifulSoup(self.content, 'lxml')
  
  def closeConnect(self): 
    self.driver.quit()

  def getSoup(self): 
    return self.soup

  def returnAllFoundMatches(self):
    """Пока не найдёт ближайшие матчи - будет уменьшать дату"""
    while True: 
      self.stopMatch = self.findStopMatch()
      if self.stopMatch: 
        # Склеенный массив 
        self.findMatch = [self.stopMatch] + list(self.stopMatch.find_all_previous('div', class_ = 'event__match'))
        return self.findMatch
      else: 
        self.date = self.decData()  
  
  def findStopMatch(self):
    """Получает дату и находит последний матч, перебирая все времена, в которых играют команды"""
    self.timeList = ['01:00', '01:30', '02:30', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00',
    '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30']
    for time in self.timeList: 
      # Первый родитель - блок data, второй - само событие. Поэтому parent.parent
      try: 
        print(f"{self.date}. {time}")
        self.stopMatch = self.soup.find(string=f"{self.date}. {time}").parent.parent
        if self.stopMatch: 
          return self.stopMatch
      except: 
        continue

  def decData(self) -> str:
    """Уменьшает дату и возвращает обновлённую строку"""
    self.zeroBeforeDay = self.zeroBeforeMonth = ''
    self.dataList = [int(x) for x in self.date.split('.')]
    self.month = self.dataList[1]
    self.day = self.dataList[0]

    if self.day == 1:
      self.month -= 1
      self.day = 31
      if self.month < 1: 
        self.month = 12
    else: 
      self.day -= 1

    if self.month <= 9: 
      self.zeroBeforeMonth = '0'
    if self.day <= 9: 
      self.zeroBeforeDay = '0'
    return f'{self.zeroBeforeDay}{self.day}.{self.zeroBeforeMonth}{self.month}'


if __name__ == '__main__': 
  par = SoupFromHTML('12.04')
  par.startConnect()
  par.startMakeSoup()
  