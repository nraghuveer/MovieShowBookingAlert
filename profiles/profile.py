from abc import ABC, abstractmethod

class BaseProfile:
    """
    Base class for the profiles
    """
    __metaclass__ = ABC

    def __init__(self, url):
        self.url = url

    @abstractmethod
    def execute(self):
        pass