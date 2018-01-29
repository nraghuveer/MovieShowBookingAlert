from profiles import BaseProfile
from profiles.bms.definitions import xpaths

# selenium imports
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

class Profile(BaseProfile):
    def execute(self):
        """
        Scrapes the url and gets the data
        """

        self.browser = self.get_self.browser()
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located((By.XPATH, xpaths['wait_for_load_complete'])))
        except TimeoutException:
            self.browser.quit()
            raise Exception('Timeout for profile {}',__file__)
        
        self.browser.find_element_by_xpath(xpaths['main_page_all_btn']).click()

        self.browser.find_element_by_xpath(xpaths['main_page_all_btn_movies']).click()

        broswer.implicitly_wait(2)

        cinemas_btn = self.browser.find_elements_by_tag_name('button')[1]

        print(cinemas_btn)



    
