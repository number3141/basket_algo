from abc import ABC, abstractmethod


class ResourseConnection(ABC): 
    def __init__(self, path) -> None:
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



