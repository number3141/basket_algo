from abc import ABC, abstractmethod


class ResourseConnection(ABC):
    def __init__(self):
        self.path = None

    def set_path(self, path):
        self.path = path

    @abstractmethod
    def start_connect(self): 
        pass 

    @abstractmethod
    def get_content(self): 
        pass 

    @abstractmethod
    def close_connect(self): 
        pass 



