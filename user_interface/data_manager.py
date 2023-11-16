from abc import ABC, abstractmethod

class DataManager(ABC): 
    @abstractmethod
    def start_program(self, user_data) -> list:
        pass

    @abstractmethod
    def get_match_list(self):
        pass 

    @abstractmethod
    def get_freq_list(self):
        pass 