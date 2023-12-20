from abc import ABC, abstractmethod

from entity.freq_list import Freq_List


class FindStatistic(ABC):
    def __init__(self, data_no_check: list, freq_list: Freq_List = Freq_List()) -> None:
        self.data_no_check = data_no_check
        self.freq_list = freq_list

    @abstractmethod 
    def find_statistic_in_data(self) -> list:
        pass 

    def get_freq_list(self): 
        return self.freq_list.get_freq_list()
