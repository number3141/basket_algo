import re

from bs4 import BeautifulSoup

from entity.match import MatchBasketDTO
from exceptions.sel_flash_exceptions import NoDataExceptions
from present_controll.data_cleaner import DataCleaner


# Обрезание ненужного HTML

class DataCleanerSelFlash(DataCleaner):
    def __init__(self, date_str, content) -> None:
        super().__init__()
        self.date_list = date_str.split('.')
        self.day, self.month = [i if len(i) == 2 else f"0{i}" for i in self.date_list]
        self.dirty_data = BeautifulSoup(content, 'lxml')

    #   ДОДЕЛАТЬ ВОЗВРАТ ЗНАЧЕНИЙ
    def cleaning_data(self) -> list:
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

            new_match = MatchBasketDTO()
            new_match.set_date(date)
            new_match.set_name_home(name_home)
            new_match.set_name_away(name_away)
            new_match.set_points_home(points_home)
            new_match.set_points_away(points_away)
            self.clear_data.append(new_match)

        return self.clear_data

    def cut_content(self):
        self.stopMatch = self.find_stop_match()
        self.cutter_content = [self.stopMatch] + list(self.stopMatch.find_all_previous('div', class_='event__match'))

    def find_stop_match(self):
        """Получает дату и находит последний матч, перебирая все времена, в которых играют команды"""
        self.timeList = ['01:00', '01:30', '02:30', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00',
                         '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30']

        for time in self.timeList:
            print(f"{self.day}.{self.month} {time}")
            self.stopMatch = self.isMatchWithDate(time)
            if self.stopMatch:
                print('Вернул матч!')
                return self.stopMatch

        raise NoDataExceptions('Нет такой даты!')

    def isMatchWithDate(self, time):
        try:
            stringForFind = f"{self.day}.{self.month}. {time}"
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
