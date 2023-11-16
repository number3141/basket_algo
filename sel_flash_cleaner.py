import datetime
import re

from bs4 import BeautifulSoup

from entity.match import Match
from present_controll.data_cleaner import DataCleaner


# Обработчик даты для презентатора обрезания ненужного HTML 

class MatchDate(): 
    """
    Класс, содержащий дату матча 

    Атрибуты: 
    ----------
    date_str : str
        Дата, с какого дня нужно начать "собирать" матчи

    Методы:
    ----------
    decDate()
        Отнимает от текущей даты 1 день
        
    """
    def __init__(self, date_str) -> None:
        self.dateList = date_str.split('.')
        self.day = int(self.dateList[0])
        self.month = int(self.dateList[1])
        self.date = datetime.datetime(2022, self.month, self.day)
        

    def __repr__(self) -> str:
        return f'День - {self.day}, Месяц - {self.month}'


    def getDay(self):
        return self.day if self.day >= 10 else f'0{self.day}'  
    

    def getMonth(self): 
        return self.month if self.month >= 10 else f'0{self.month}'


    def decDate(self): 
        """
        Отнимает от текущей даты 1 день
        
        Не принимает аргументов, работает с датой, 
        которую передали при создании экземпляра объекта

        """
        if self.day == 1: 
            if self.month == 1:
                self.day = 31 
                self.month = 12 
            else: 
                self.day = 31
                self.month -= 1
        else: 
            self.day -= 1

# Обрезание ненужного HTML 


class DataCleanerSelFlash(DataCleaner):
    """

    """
    def __init__(self, dateString, content) -> None:
        super().__init__()
        self.date = MatchDate(dateString)
        self.dirty_data = BeautifulSoup(content, 'lxml')
        
  
    def cleaning_data(self, match: Match) -> list:
        for dirty_match in self.cutter_content: 
            date = dirty_match.find('div', class_='event__time').text
            name_home = dirty_match.find('div', class_=f'event__participant--home').text
            name_away = dirty_match.find('div', class_=f'event__participant--away').text

            points_home = []
            points_away = []
            for part in [1, 2, 3, 4]: 
                point_home_in_part = dirty_match.select(f'.event__part--home' + f'.event__part--{part}')
                point_away_in_part = dirty_match.select(f'.event__part--away' + f'.event__part--{part}')
                points_home.append(self.findDecimalNumImStr(point_home_in_part))
                points_away.append(self.findDecimalNumImStr(point_away_in_part))
            
            new_match = match
            new_match.set_date(date)
            new_match.set_name_home(name_home)
            new_match.set_name_away(name_away)
            new_match.set_points_home(points_home)
            new_match.set_points_away(points_away)

            new_match.calc_result()

            if new_match.check_match():
                new_match.set_underhand(True)
                print('Подходит!')
            else: 
                new_match.set_underhand(False)
                print('Не подходит!')

        
            self.clear_data.append(new_match.get_info())
           
        
        return self.clear_data
         

    def cut_content(self):
        """Пока не найдёт ближайшие матчи - будет уменьшать дату"""
        while True: 
            self.stopMatch = self.find_stop_match()
            if self.stopMatch: 
                # Склеенный массив 
                self.cutter_content = [self.stopMatch] + list(self.stopMatch.find_all_previous('div', class_ = 'event__match'))
                break 
    
    
    def find_stop_match(self):
        """Получает дату и находит последний матч, перебирая все времена, в которых играют команды"""
        self.timeList = ['01:00', '01:30', '02:30', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00',
        '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30']
        
        while True: 
            for time in self.timeList:
                print(f"{self.date.getDay()}.{self.date.getMonth()} {time}")
                self.stopMatch = self.isMatchWithDate(time)
                if self.stopMatch: 
                    print('Вернул матч!')
                    return self.stopMatch

            self.date.decDate()
    

    def isMatchWithDate(self, time): 
        try: 
            stringForFind = f"{self.date.getDay()}.{self.date.getMonth()}. {time}"
            # parent из-за того, что возвращается строка, а нам нужен весь матч (родитель)
            findMatch = self.dirty_data.find(string=stringForFind).parent.parent
            return findMatch
        except: 
            return False


    def findDecimalNumImStr(self, findStr):
        # Регулярная строка для поиска всех десятичных чисел 
        self.reg = re.compile(r'\d{2}')
        # Конверт в строку, потому что тип - ResultSet бьютифушный 
        self.findPointInPart = self.reg.findall(str(findStr))
        return int(*self.findPointInPart)
    

