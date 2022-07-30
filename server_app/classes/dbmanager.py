import os
import subprocess
import psycopg2

from classes.configuration import Configuration
from classes.logger import Logger

class DbManager(object):
    """
    This class manager SQL queries
    """

    def __init__(self):
        self.filepath = Configuration.VB_TABLE_NAME
        self.table_name = os.path.basename(self.filepath.split('.')[0])

    def _create_connection(self):
        self.connection = psycopg2.connect(
            host=Configuration.DB['domain'],
            database=Configuration.DB['dbname'],
            user=Configuration.DB['user'],
            password=Configuration.DB['password']
        )

    def _destroy_connection(self):
        if self.connection:
            self.connection.close()
        else:
            Logger.add_log_item('Problem with destroing connection', 'ERROR', 'POSTGRESQL')

    def _create_cursor(self):
        if self.connection:
            self.cursor = self.connection.cursor()
        else:
            Logger.add_log_item('Problem with creating cursor', 'ERROR', 'POSTGRESQL')

    def _commit_command(self):
        self.connection.commit()

    def _destroy_cursor(self):
        if self.cursor:
            self.cursor.close()
        else:
            Logger.add_log_item('Problem with destroing cursor', 'ERROR', 'POSTGRESQL')

    def _execute_sql(self, sql, command_name, is_delete=False):
        try:
            self.cursor.execute(sql)
            Logger.add_log_item('SQL command: "{0}" was successfull'.format(sql), 'SUCCESS', 'POSTGRESQL')
            if not is_delete:
                result = self.cursor.fetchall()
            else:
                result = self.cursor.rowcount
            return result
        except psycopg2.Error:
            Logger.add_log_item('Problem with running SQL: "{0}"'.format(command_name), 'ERROR', 'POSTGRESQL')

    def _self_format_result(self, result):
        ids = []
        if not result:
            return ids
        for item in result:
            ids.append(int(item[0]))
        return ids

    def get_unique_vb(self):
        self._create_connection()
        self._create_cursor()
        result = self._execute_sql(
            'SELECT DISTINCT id FROM "{0}"."{1}";'.format(Configuration.DB['schema'], str(self.table_name).lower()), 
            'Get unique rows of VB', False)
        self._destroy_cursor()
        self._destroy_connection()
        return self._self_format_result(result)

    def delete_by_id(self, id):
        self._create_connection()
        self._create_cursor()
        result = self._execute_sql('DELETE FROM "{0}"."{1}" WHERE "id" = {2};'.format(
            Configuration.DB['schema'], str(self.table_name).lower(), id), 
            'Delete VB by ID', True)
        self._commit_command()
        self._destroy_cursor()
        self._destroy_connection()
        return 'Count of deleted rows: {0}'.format(str(result))
