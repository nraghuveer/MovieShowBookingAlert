import argparse
from configparser import SafeConfigParser
import os
import sys

from selenium import webdriver

# project specific imports
from configuration import Configuration
from profile_manager import ProfileManager
from model import Movie

def main(*args, **kwargs):
    """
    Mandatory entry for the system/project.
    Calls the respective engines based on the arguments.
    """
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-config', dest= 'config')
    argparser.add_argument('-engine', dest= 'engine')
    arg_values = argparser.parse_args(['-config', 'default', '-engine', 'cinemas'])

    configuration = Configuration(os.path.join(os.sep, os.getcwd(), 'configurations', arg_values.config+'.ini'))
    
    profile_manager = ProfileManager('bms', configuration)
    profile_manager.execute_engine('hyderabad', arg_values.engine)
    

if __name__ == '__main__':
    main(sys.argv[1:])

