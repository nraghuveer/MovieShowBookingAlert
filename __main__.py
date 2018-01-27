import argparse
from configparser import SafeConfigParser
import os

# project specific imports
from configuration import Configuration
from model import Movie

def main(*args, **kwargs):
    """
    Mandatory entry for the system/project.
    Calls the respective engines based on the arguments.
    """
    # read the configuration file, default file name is default.ini
    # TODO: replace the hardcoded filename with the one from the arguments
    configuration = Configuration(os.path.join(os.sep, os.getcwd(), 'configurations', 'default.ini'))


if __name__ == '__main__':
    main()

