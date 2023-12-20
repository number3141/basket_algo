#!/usr/bin/python3.12

from entity.match import MatchBasketDTO
from sel_flash_cleaner import DataCleanerSelFlash
from sel_flash_connection import HTMLConnection
from playwright_connection import PlayWrightConnection
from sel_flash_usecase import SelFlashFindStatistic
from user_interface.data_manager import DataManager

def create_connection(type):
    if type == 'selenium':
        return HTMLConnection
    elif type == 'playwright':
        return PlayWrightConnection

class SiteManager(DataManager):
    def set_type_connection(self, type) -> None:
        self.connect = create_connection(type)('https://www.flashscorekz.com/basketball/usa/nba/results/')

    def start_program(self, user_data): 
        self.connect.start_connect()
        res  = self.connect.get_content(user_data)
        self.connect.close_connect()
    
        data_cleaner = DataCleanerSelFlash(user_data, res)
        data_cleaner.cut_content()
        clear_data = data_cleaner.cleaning_data()

        finder_stat = SelFlashFindStatistic(clear_data)
        finder_stat.find_statistic_in_data()

        self.match_list = finder_stat.get_match_list()
        self.freq_list = finder_stat.get_freq_list()

    def get_match_list(self):
        return self.match_list
    
    def get_freq_list(self):
        return self.freq_list