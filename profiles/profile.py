from abc import ABC, abstractmethod
from definitions import PROJECT_ROOT_DIR
import os

class BaseProfile:
    """
    Base class for the profiles
    """
    __metaclass__ = ABC

    def __init__(self, url, configuration, browser):
        self.url = url
        self.configuration = configuration
        self.browser = browser


        self.timeout = int(configuration.connection.timeout)

    @abstractmethod
    def execute(self):
        pass
