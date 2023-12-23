from sel_flash_cleaner import DataCleanerSelFlash
from sel_flash_usecase import SelFlashFindStatistic
from user_interface.data_manager import DataManager
from present_controll.resource_connection import ResourseConnection


class WebDataManager(DataManager):
    def __init__(self):
        self.freq_list = None
        self.connect = None

    def set_connection(self, connection: ResourseConnection) -> None:
        self.connect = connection
        self.connect.set_path('https://www.flashscorekz.com/basketball/usa/nba/results/')

    def start_program(self, user_data):
        self.connect.start_connect()
        res = self.connect.get_content(user_data)
        self.connect.close_connect()

        data_cleaner = DataCleanerSelFlash(user_data, res)
        data_cleaner.cut_content()
        clear_data = data_cleaner.cleaning_data()

        finder_stat = SelFlashFindStatistic(clear_data)
        finder_stat.find_statistic_in_data()

        self.freq_list = finder_stat.get_freq_list()

    def get_freq_list(self):
        return self.freq_list
