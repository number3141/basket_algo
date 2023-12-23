from exceptions.sel_flash_exceptions import NoDataExceptions
from playwright_connection import PlayWrightConnection
from sel_flash_connection import HTMLConnection
from sel_flash_manager import WebDataManager
from sel_flash_interface import GraphInterface
from user_interface.data_manager import DataManager
from user_interface.interface import Interface


def create_connection(type_connection):
    if type_connection == 'selenium':
        return HTMLConnection()
    elif type_connection == 'playwright':
        return PlayWrightConnection()


class General:
    def __init__(self, data_manager: DataManager, interface: Interface) -> None:
        self.data_manager = data_manager
        self.interface = interface
        self.freq_list = None

    def start_and_draw(self, user_data, type_con):
        try:
            self.data_manager.set_connection(connection=create_connection(type_con))
            self.data_manager.start_program(user_data)
            self.freq_list = self.data_manager.get_freq_list()
            self.interface.draw_freq_table(self.freq_list)
        except NoDataExceptions: 
            self.interface.draw_text_in_board('Нет такой даты!')

    def save_freq_list(self): 
        self.interface.save_freq_list(self.freq_list)

    def start_program(self): 
        self.interface.draw_main_window(self.start_and_draw, self.save_freq_list)


if __name__ == '__main__':
    t = General(WebDataManager(), GraphInterface())
    t.start_program()


    