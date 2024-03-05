import re

from bs4 import BeautifulSoup

from entity.match import MatchBasketDTO
from exceptions.sel_flash_exceptions import NoDataExceptions
from present_controll.data_cleaner import DataCleaner


def find_decimal_in_str(find_str):
    reg = re.compile(r'\d{2}')
    # Конверт в строку, потому что тип - ResultSet бьютифушный
    quarter_points = reg.findall(str(find_str))
    return int(*quarter_points)


# Обрезание ненужного HTML
class DataCleanerSelFlash(DataCleaner):
    def __init__(self, date_str, content) -> None:
        super().__init__()
        self.date_list = date_str.split('.')
        self.day, self.month, self.year = [i if len(i) == 2 else f"0{i}" for i in self.date_list]
        self.dirty_data = BeautifulSoup(content, 'lxml')

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
                points_home.append(find_decimal_in_str(point_home_in_part))
                points_away.append(find_decimal_in_str(point_away_in_part))

            new_match = MatchBasketDTO()
            new_match.date = date
            new_match.name_home = name_home
            new_match.name_away = name_away
            new_match.points_home = points_home
            new_match.points_away = points_away
            self.clear_data.append(new_match)

        return self.clear_data

    def cut_content(self):
        """Получает дату и находит последний матч, перебирая все времена, в которых играют команды"""
        time_list = ['01:00', '01:30', '02:30', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00',
                     '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30']
        stop_match = None
        for time in time_list:
            stop_match = self.is_match_with_date(time)
            if stop_match:
                break
        if not stop_match:
            raise NoDataExceptions('Нет такой даты!')

        self.cutter_content = [stop_match] + list(stop_match.find_all_previous('div', class_='event__match'))

    def is_match_with_date(self, time):
        try:
            search_date = f"{self.day}.{self.month}. {time}"
            # parent из-за того, что возвращается строка, а нам нужен весь матч (родитель)
            return self.dirty_data.find(string=search_date).parent.parent
        except Exception:
            return False
