
from exceptions.sel_flash_exceptions import NoDataExceptions
from sel_flash_manager import SiteManager
from sel_flash_interface import GraphInterface
from user_interface.data_manager import DataManager
from user_interface.interface import Interface

class General:
    def __init__(self, data_manager: DataManager, interface: Interface) -> None:
        self.data_manager = data_manager
        self.interface = interface
        self.match_list = None
        self.freq_list = None

    def start_and_draw(self, user_data, type):
        try:
            self.data_manager.set_type_connection(type)
            self.data_manager.start_program(user_data)
            self.match_list = self.data_manager.get_match_list()
            self.freq_list = self.data_manager.get_freq_list()
            self.interface.draw_match_table(self.match_list)
            self.interface.draw_freq_table(self.freq_list)
        except NoDataExceptions: 
            self.interface.draw_text_in_board('Нет такой даты!')

    def save_match_list(self): 
        self.interface.save_match_list(self.match_list)

    def save_freq_list(self): 
        self.interface.save_freq_list(self.freq_list)

    def start_program(self): 
        self.interface.draw_main_window(self.start_and_draw, self.save_match_list, self.save_freq_list)


if __name__ == '__main__':
    t = General(SiteManager(), GraphInterface())
    t.start_program()


    