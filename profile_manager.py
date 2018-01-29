import enum
import os
import importlib
from selenium import webdriver

from definitions import source_base_urls, source_keywords, profile_engines,PROJECT_ROOT_DIR

class ProfileManager:
    """
    Loads profiles based on the source keyword
    Executes and returns the results based on profile engine keyword
    """
    def __init__(self, source_keyword, configuration):
        """
        Input:
            source_keyword : Keyword for source
            configuration : configuration 
        """
        if source_keyword not in source_keywords.keys():
            raise Exception('Invalid source keyword, Unable to find {} in the source keywords dictionary.')
            
        self.source_keyword = source_keyword
        self.configuration = configuration

    def execute_engine(self, city, engine_keyword, *args, **kwargs):
        """
        Calls the respective method for the given keyword
        """
        if engine_keyword not in profile_engines:
            raise Exception('Engine {}, not specified in the profile engine keywords.')

        # get the base url for the source
        url = self.get_city_url(city)

        profile = self.get_profile(url, engine_keyword, self.get_browser())

        profile.execute()


    def get_profile(self, url, engine_keyword, browser):
        """
        create and return a profile instance base on the source
        """
        try:
            # get the module for the profile
            profile_module = importlib.import_module('profiles.'+self.source_keyword+'.'+engine_keyword)
            # create profile instance
            profile = getattr(profile_module, 'Profile')(url, self.configuration, browser)
            return profile
        except KeyError:
            raise Exception('Engine with keyword {} not found.'.format(engine_keyword))

    def get_city_url(self, city):
        """
        construct the city specific url from the source keyword base url
        """
        return source_base_urls[self.source_keyword]+'/'+city

    def get_browser(self):
        """
        Creates and returns browser instance
        """
        options = webdriver.ChromeOptions()
        options.add_argument(' - incognito')

        driver_path = PROJECT_ROOT_DIR + self.configuration.web_driver.file_path
        # convert to raw string
        driver_path.replace('\\', '\\\\')
        print(driver_path)
        browser = webdriver.Chrome(executable_path= driver_path, chrome_options= options)

        return browser
