"""
Модуль сущности Match (Entity). Не знает о низших слоях 
Класс, который позволяет рассчитать результат и вернуть его 
"""
from abc import ABC, abstractmethod


class MatchDTO:
    def __init__(self) -> None:
        self.date = None
        self.name_home = None
        self.name_away = None
        self.loser = None
        self.winner = None 
        self.points_home = list()
        self.points_away = list()
        self.underhand = False
        self.result = False

    def __repr__(self):
        return f"{self.name_home} - {self.name_away}"
    
    def set_result(self, result):
        self.result = result
        
    def set_winner(self, winner): 
        self.winner = winner 
        
    def set_loser(self, loser): 
        self.loser = loser 

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
        
    def get_date(self):
        return self.date
        
    def get_name_home(self):
        return self.name_home
    
    def get_points_home(self):
        return self.points_home
    
    def get_points_away(self):
        return self.points_away
    
    def get_name_away(self): 
        return self.name_away

    def get_team_list(self) -> list: 
        return [self.name_home, self.name_away]
    
    def get_underhand(self): 
        return self.underhand
    
    def get_result(self): 
        return self.result
    
    def get_winner(self): 
        return self.winner 
    
    def get_loser(self): 
        return self.loser


class MatchBasketDTO(MatchDTO): 
    def __init__(self) -> None:
        super().__init__()
        self.win_3 = False
        self.win_4 = False 
        
    def get_win_3(self): 
        return self.win_3    
    
    def get_win_4(self): 
        return self.win_4


class Match(ABC):
    def __init__(self) -> None:
        self.data: MatchDTO = None
        
    def set_data(self, data): 
        self.data = data
        
    def get_data(self):
        return self.data
        
    @abstractmethod
    def calc_result(self):
        pass 

   
        
