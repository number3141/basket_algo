from abc import ABC, abstractmethod


class ResourseConnection(ABC): 
    @abstractmethod
    def start_connect(self): 
        pass 

    @abstractmethod
    def get_content(self): 
        pass 

    @abstractmethod
    def close_connect(self): 
        pass 



