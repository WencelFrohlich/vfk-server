# -*- coding: utf-8 -*-

__author__ = "Vaclav Frohlich"
__copyright__ = "Copyright 2022"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Vaclav Frohlich"
__email__ = "vaclav @ frohlich . xyz"
__status__ = "Develop"

import os
from classes.configuration import Configuration
from classes.logger import Logger

class Documentation(object):
    """
    Class for testing loading file and sent via server to client
    """
    def _get_help():
        if os.path.exists(Configuration.HTML_TEMPLATES_LOCATION):
            try:
                with open(Configuration.HTML_TEMPLATES_LOCATION, 'r') as html_file:
                    return html_file.read()
            except:
                Logger.add_log_item('Request for getting HELP was failed!'.format(Configuration.APPLICATION_NAME), 'ERROR', 'REQUEST')
        else:
            Logger.add_log_item('Template for HELP does not exists!'.format(Configuration.APPLICATION_NAME), 'ERROR', 'REQUEST')


            