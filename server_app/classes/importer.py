import os
import subprocess

from classes.configuration import Configuration
from classes.logger import Logger

class Importer(object):
    """
    This class create system command for import and convert VFK file into DB table
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.table_name = os.path.basename(self.filepath.split('.')[0])
        self._create_command()
        self._run_command()

        
    def _create_command(self):
        self.cmd = '{0} -append -f "PostgreSQL" PG:"host={1} user={2} dbname={3} password={4}" {5} -nln "{6}" {7} -skipfailures '.format(
            Configuration.OGR2OGR_PATH,
            Configuration.DB['domain'],
            Configuration.DB['user'],
            Configuration.DB['dbname'],
            Configuration.DB['password'],
            self.filepath,
            'vfk',#self.table_name,
            Configuration.VB_LAYER_NAME
        )

    def _run_command(self):
        if not self.cmd:
            return False
        env = os.environ.copy()
        env["PGPASSWORD"] = Configuration.DB['password']
        result = subprocess.run(self.cmd, check=True, shell=True, env=env, capture_output=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            Logger.add_log_item('Import file: {0} into table: {1} was successfull!'.format(self.filepath, self.table_name), 'SUCCESS', 'IMPORTER')
        else:
            Logger.add_log_item('Import file: {0} into table: {1} was failed!'.format(self.filepath, self.table_name), 'ERROR', 'IMPORTER')
    
