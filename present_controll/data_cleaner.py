from abc import ABC, abstractmethod
from typing import Any


class DataCleaner(ABC):
    def __init__(self) -> None:
        self.clear_data: list = list()

    @abstractmethod
    def cut_content(self):
        pass 

    @abstractmethod
    # Подготовка данных для UseCase
    def cleaning_data(self) -> list[str]: 
        pass 

    def set_dirty_data(self, dirty_data): 
        self.dirty_data = dirty_data

    def get_clear_data(self): 
        return self.clear_data

        

    