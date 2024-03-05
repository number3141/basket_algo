"""
Модуль сущности Match (Entity). Не знает о низших слоях 
Класс, который позволяет рассчитать результат и вернуть его 
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class MatchDTO:
    date: str = None
    name_home: str = None
    name_away: str = None
    points_home: list = field(default_factory=list)
    points_away: list = field(default_factory=list)
    loser: str = None
    winner: str = None
    underhand: bool = False
    result: bool = False


@dataclass
class MatchBasketDTO(MatchDTO):
    win_3: bool = False
    win_4: bool = False


class Match(ABC):
    def __init__(self) -> None:
        self.dto_data: MatchDTO = None

    def __repr__(self):
        return f"{self.dto_data.name_home} - {self.dto_data.name_away}"

    def set_dto_data(self, data):
        self.dto_data = data

    def get_dto_data(self):
        return self.dto_data

    @abstractmethod
    def calc_result(self):
        pass

