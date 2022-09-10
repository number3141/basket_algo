from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

from data.matchDate import MatchDate

class SoupFromHTML():
    def __init__(self, dateString, url='https://www.flashscore.com.ua/basketball/usa/nba/results/') -> None:
        self.date = MatchDate(dateString)
        self.url = url 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
  
    def __repr__(self) -> str:
        return f'Объект - {self.soup}'
    
    def startConnect(self): 
        """Начинает соединение с url"""
        self.driver.get(self.url)   
        self.mainStatus = self.driver.requests[0].response.status_code
        while self.mainStatus != 200:
            self.driver.refresh() 
        
    def startMakeSoup(self): 
        """Забирает контент со страницы и делает суп"""
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
                print('МАТЧ НАЙДЕН!')
                # Склеенный массив 
                self.findMatch = [self.stopMatch] + list(self.stopMatch.find_all_previous('div', class_ = 'event__match'))
                return self.findMatch
    
    def findStopMatch(self):
         # Первый родитель - блок data, второй - само событие. Поэтому parent.parent
        """Получает дату и находит последний матч, перебирая все времена, в которых играют команды"""
        self.timeList = ['01:00', '01:30', '02:30', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00',
        '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30']
        while True: 
            for time in self.timeList:
                print(f"{self.date.getDay()}.{self.date.getMonth()} {time}")
                self.stopMatch = self.isMatchWithDate(time)
                if self.stopMatch: 
                    return self.stopMatch
            self.date.decDate()
    
    def isMatchWithDate(self, time): 
        try: 
            stringForFind = f"{self.date.getDay()}.{self.date.getMonth()}. {time}"
            findMatch = self.soup.find(string=stringForFind).parent.parent
            return findMatch
        except: 
            return False
    



if __name__ == '__main__': 
    # par = SoupFromHTML('12.04')
    # par.startConnect()
    # par.startMakeSoup()
    
    da = MatchDate('01.01')
    print(da.getDay())
    da.decDate()
    print(da)