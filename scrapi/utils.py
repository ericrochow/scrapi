import logging
import os
from logging.config import fileConfig

import yaml


class Config(object):
    """
    """

    def __init__(self):
        """
        """
        self.current_location = os.path.dirname(os.path.realpath(__file__))
        self.config_file = os.path.join(
            self.current_location, "../etc/config.yml"
        )
        self.config = open(self.config_file)
        self.full_config = yaml.safe_load(self.config)
        self.config.close()
        fileConfig(
            os.path.join(self.current_location, "../etc/logging.ini"),
            disable_existing_loggers=True,
        )
        self.handler = logging.fileHandler(
            os.path.join(self.current_location, "../var/scrapi.log")
        )
