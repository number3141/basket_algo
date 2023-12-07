from abc import ABC, abstractmethod

from entity.freq_list import Freq_List
from entity.match import Match
from entity.match_list import Match_List



class FindStatistic():
    def __init__(self, data_no_check: list, match_list: Match_List = Match_List(), freq_list: Freq_List = Freq_List()) -> None:
        self.data_no_check = data_no_check
        self.match_list = match_list
        self.freq_list = freq_list


    @abstractmethod 
    def find_statistic_in_data(self) -> list:
        pass 

    
    def get_match_list(self): 
        return self.match_list.get_match_list()
    

    def get_freq_list(self): 
        return self.freq_list.get_freq_list()
