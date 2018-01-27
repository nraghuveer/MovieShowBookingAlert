import enum
import os

# selenium imports
from selenium import webdriver
from selenuim.webdriver.common.by import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from configuration import PROJECT_ROOT_DIR

# mappings for engine keywords to methods
engine_keyword_mappings = {
    'cinemas' : 'GetCinemas',
    'active_movies' : 'GetActiveMovies',
    'upcoming_movies' : 'GetUpcomingMovies',
    'bookings_open' : 'GetOpenBookings'
}

class TaskManager:
    """
    Executes the task based on given keyword.
    Also responsible to update the datastore/database with results.
    There are three types of tasks: MethodName - engine keyword
        1. Get List of Cinemas 
            GetCinemas          - 'cinemas'
        2. Get List of Now Showing and Coming Soon Movies 
            GetActiveMovies     - 'active_movies' 
            GetUpcomingMovies   - 'upcoming_movies'
        3. Get list of movies whose bookings are open 
            GetOpenBookings   - 'bookings_open'
    """
    def __init__(self, city, configuration, profile_manager):
        """
        Input:
            profile_manager: Gets the respective profile needed for the execution of trigged engine
        """
        self.city = city
        self.configuration = configuration
        self.profile_manager = profile_manager

    def execute_engine(self, keyword, *args, **kwargs):
        """
        Calls the respective method for the given keyword
        """
        try:
            getattr(self, engine_keyword_mappings[keyword])(*args, **kwargs)
        except KeyError, keyerror:
            raise Exception('Engine with keyword {} not found.'.format(keyword))

    
    def GetCinemas(self):
        """
        Gets the list of cinemas listed on the profile for the city.
        """
        


    def get_browser(self):
        """
        Creates and returns brower instance
        """
        options = webdriver.ChromeOptions()
        options.add_argument(' - incognito')

        browser = webdriver.Chrome(executable_path= \
        os.path.join(PROJECT_ROOT_DIR, self.configuration.web_driver.file_path), chrome_options= options)

        return browser




