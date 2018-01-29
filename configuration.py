from configparser import SafeConfigParser
import os.path

class Options():
    """
    Acts as proxy class for storing the options of a section as attributes
    so that they can be accessed as normal python properites with option name
    """
    pass

class Configuration:
    """
    Reads the .ini file and provides easy access to the contents.
    
    Reads the fields that are defined in the defined_configurations set
    this is set of tuples with
        section name as first element
        option name as second element

    Facilitates the configuration file contents as the normal python property access if present
    example:
        for value of option 'option1' in 'section1', it can be access as
        configuration_instance.section1.option1

        raises Attribute if option1 or section1 are not present
    """
    # only section-options that are in this list are parsed
    defined_configurations = set([
        ('web_driver', 'file_path'),
        ('connection', 'timeout')
    ])

    def __init__(self, file_path):
        self.file_path = file_path
        self._section_dict = {}
        self._sections = set()
        self._read()

    def _read(self):
        """
        Reads the contents of config file
        """
        if not os.path.isfile(self.file_path):
            raise Exception('Unable to find configuration file in the given path {}'.format(file_path))

        parser = SafeConfigParser()
        parser.read(self.file_path)

        for section, option in Configuration.defined_configurations:
            # test if dictionary has already section key
            # if not create one
            # lastly add the option to the Options instance
            try:
                self._section_dict[section]
            except KeyError:
                self._section_dict[section] = Options()
            finally:
                setattr(self._section_dict[section], option, parser.get(section, option))
                

    def __getattr__(self, name):
        if name not in self._section_dict:
            raise AttributeError('Unable to find {} attribute in {} instance'.format(name, __class__))
        
        return self._section_dict[name]