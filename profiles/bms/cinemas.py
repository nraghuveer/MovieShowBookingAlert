from profiles import BaseProfile

# selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

class Profile(BaseProfile):
    def execute(self):
        print(self.url)
        print('BMS cinemas profile')