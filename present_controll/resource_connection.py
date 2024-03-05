from abc import ABC, abstractmethod


class ResourseConnection(ABC):
    def __init__(self, path=None):
        self.path = path

    def set_path(self, path):
        self.path = path

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    def get_content(self):
        pass




