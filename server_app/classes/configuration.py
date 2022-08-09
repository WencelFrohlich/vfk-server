# -*- coding: utf-8 -*-

__author__ = "Vaclav Frohlich"
__copyright__ = "Copyright 2022"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Vaclav Frohlich"
__email__ = "vaclav @ frohlich . xyz"
__status__ = "Develop"

import os

class Configuration(object):
    """
    This class contains option for running simple VFK processor server
    """

    APPLICATION_NAME = 'VFK processor server'
    BASE_LOCATION = os.path.join(os.getcwd(), 'server_app')
    LOGGER_FILE_LOCATION = os.path.join(BASE_LOCATION, 'server.log')
    LOGGER_VFK_PROCESSOR_FILE = os.path.join(BASE_LOCATION, 'vfk_processor.log')

    HTML_TEMPLATE_FOLDER = os.path.join(BASE_LOCATION, 'html_templates')
    HTML_TEMPLATES_LOCATION = os.path.join(BASE_LOCATION, 'html_templates', 'help.html')
    HTML_BASE_PAGE = 'index.html'
    UPLOADED_FILE_LOCATION = os.path.join(BASE_LOCATION,'uploaded_files')
    UPLOADED_FILE_EXENTSIONS = ['vfk']

    OGR2OGR_PATH = '/usr/bin/ogr2ogr'

    VB_LAYER_NAME = 'ZVB'
    VB_TABLE_NAME = 'vfk'
    VB_FOR_MAP = 'vfk_for_map'

    DB = {
        'domain' : 'localhost',
        'dbname' : 'vfk',
        'schema' : 'public',
        'port'   : 5432,
        'user'   : 'sa',
        'password' : 'superadmin----'
    }