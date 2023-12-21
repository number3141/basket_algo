from abc import ABC, abstractmethod


class DataManager(ABC):
    @abstractmethod
    def start_program(self, user_data) -> list:
        pass

    @abstractmethod
    def set_connection(self, connection):
        pass

    @abstractmethod
    def get_freq_list(self):
        pass
