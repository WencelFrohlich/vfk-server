import os

class Configuration(object):
    """
    This class contains option for running simple VFK processor server
    """

    APPLICATION_NAME = 'VFK processor server'
    BASE_LOCATION = os.path.join(os.getcwd(), 'server_app')
    LOGGER_FILE_LOCATION = os.path.join(BASE_LOCATION, 'server.log')
    LOGGER_VFK_PROCESSOR_FILE = os.path.join(BASE_LOCATION, 'vfk_processor.log')

    HTML_TEMPLATES_LOCATION = os.path.join(BASE_LOCATION, 'html_templates', 'help.html')
    UPLOADED_FILE_LOCATION = os.path.join(BASE_LOCATION,'uploaded_files')
    UPLOADED_FILE_EXENTSIONS = ['vfk']

    OGR2OGR_PATH = '/usr/bin/ogr2ogr'

    VB_LAYER_NAME = 'ZVB'
    VB_TABLE_NAME = 'vfk'

    DB = {
        'domain' : 'localhost',
        'dbname' : 'vfk',
        'schema' : 'public',
        'port'   : 5432,
        'user'   : 'sa',
        'password' : 'superadmin----'
    }