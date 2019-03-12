import json
from typing import Text


class Config:
    """Config class which allows to load and save config from json.
    """

    def __init__(self, path: Text):
        self.path = path

        with open(self.path, 'r') as fstr:
            self.__dict__ = json.load(fstr)

    def dump(self):
        """Just saves configuration to json located in place, where was the init conf.
        """

        with open(self.path, 'w') as fstr:
            json.dump(self, fstr)
