# -*- coding: utf-8 -*-

import logging
import os
from classes.configuration import Configuration
from classes.logger import Logger

class Documentation(object):
    def _get_help():
        if os.path.exists(Configuration.HTML_TEMPLATES_LOCATION):
            try:
                with open(Configuration.HTML_TEMPLATES_LOCATION, 'r') as html_file:
                    return html_file.read()
            except:
                Logger.add_log_item('Request for getting HELP was failed!'.format(Configuration.APPLICATION_NAME), 'ERROR', 'REQUEST')
        else:
            Logger.add_log_item('Template for HELP does not exists!'.format(Configuration.APPLICATION_NAME), 'ERROR', 'REQUEST')


            