from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def draw_main_window(self, start_program, save_freq):
        pass 

    @abstractmethod
    def draw_freq_table(self, freq_list):
        pass 

    @abstractmethod
    def save_freq_list(self, freq_list): 
        pass 

    @abstractmethod
    def draw_text_in_board(self, mess): 
        pass
