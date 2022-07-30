import os
from datetime import datetime
import gzip

from classes.configuration import Configuration

class Logger(object):
    """
    This object logging events for import and processing NDIC informations
    """

    MAX_LOG_FILE_SIZE = 50000000#50 MB

    def get_timestamp_file_name():
        return datetime.now().strftime('%Y-%m-%d_%H-%M')

    def get_archived_log_file_name():
        return Configuration.LOGGER_VFK_PROCESSOR_FILE.replace('.log', '') + '_' + Logger.get_timestamp_file_name() + '.log.gz'

    def archive_log():
        if os.path.getsize(Configuration.LOGGER_VFK_PROCESSOR_FILE) > Logger.MAX_LOG_FILE_SIZE:
            file_in = open(Configuration.LOGGER_VFK_PROCESSOR_FILE, 'rb')
            file_out = gzip.open(Logger.get_archived_log_file_name(), 'wb')
            file_out.writelines(file_in)
            file_out.close()
            file_in.close()
            os.remove(Configuration.LOGGER_VFK_PROCESSOR_FILE)
        else:
            return False

    def create_log_file():
        if not os.path.exists(Configuration.LOGGER_VFK_PROCESSOR_FILE):
            open(Configuration.LOGGER_VFK_PROCESSOR_FILE, 'w').close()
        else:
            return False

    def insert_to_log_file(log_item):
        Logger.create_log_file()
        with open(Configuration.LOGGER_VFK_PROCESSOR_FILE, 'a') as log_file:
            log_file.writelines(log_item)
        Logger.archive_log()

    def add_log_item(message, message_type, source):
        Logger.insert_to_log_file('[{2}][{0}][{3}]: {1} \n'.format(
            datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z'), 
            message,
            message_type,
            source
        ))