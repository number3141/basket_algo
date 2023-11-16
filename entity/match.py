"""
Модуль сущности Match (Entity). Не знает о низших слоях 
Класс, который позволяет рассчитать результат и вернуть его 
"""

import re
from abc import ABC, abstractmethod


class Match(ABC): 
    def __init__(self) -> None:
        self.date = ''
        self.name_home = ''
        self.name_away = ''
        self.points_home = list()
        self.points_away = list()
        self.underhand = False


    @abstractmethod
    def calc_result(self):
        pass 

    @abstractmethod
    def check_match(self):
        pass 

    def set_date(self, date): 
        self.date = date

    def set_name_home(self, name_home): 
        self.name_home = name_home

    def set_name_away(self, name_away):
        self.name_away = name_away

    def set_points_home(self, points_home): 
        self.points_home = points_home

    def set_points_away(self, point_away): 
        self.points_away = point_away

    def set_underhand(self, underhand):
        self.underhand = underhand

    def get_team_list(self) -> list[str]: 
        return [self.name_home, self.name_away]


    def get_info(self):
        return {
            'date': self.date, 
            'name_home': self.name_home, 
            'name_away': self.name_away, 
            'points_home': self.points_home, 
            'points_away': self.points_away, 
            'is_inderhand': self.underhand,
        } 