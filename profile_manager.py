import enum
import os
import importlib

from definitions import source_base_urls, source_keywords, profile_engines

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
        url = source_base_urls[self.source_keyword]+'/'+city

        try:
            # get the module for the profile
            profile_module = importlib.import_module('profiles.'+self.source_keyword+'.'+engine_keyword)
            # create profile instance
            profile = getattr(profile_module, 'Profile')(url)
            profile.execute()
        except KeyError:
            raise Exception('Engine with keyword {} not found.'.format(engine_keyword))

    def get_browser(self):
        """
        Creates and returns browser instance
        """
        options = webdriver.ChromeOptions()
        options.add_argument(' - incognito')

        browser = webdriver.Chrome(executable_path= \
        os.path.join(PROJECT_ROOT_DIR, self.configuration.web_driver.file_path), chrome_options= options)

        return browser




