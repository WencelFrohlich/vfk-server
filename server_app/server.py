# -*- coding: utf-8 -*-

import os
import sys
import gzip


import io

from flask import Flask
from flask import request
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from classes.configuration import Configuration
from classes.logger import Logger
from classes.documentation import Documentation
from classes.importer import Importer
from classes.dbmanager import DbManager

from waitress import serve
import logging

app = Flask(__name__)
logging.basicConfig(filename=os.path.join(Configuration.LOGGER_FILE_LOCATION), level=logging.DEBUG)

class Server(object):
    def __init__(self, app):
        self.app = app
        self.config = Configuration
        self._create_app()
        self._get_help()
        self._post_file()
        self._delete_by_id()

    def _create_app(self):
        self.app.config.from_mapping(
            SECRET_KEY='5b7fcaf0-5436-11ec-bf63-0242ac130002',
            DATABASE=os.path.join(self.app.instance_path, 'flaskr.sqlite'),
        )
        try:
            os.makedirs(self.app.instance_path)
        except OSError:
            pass

    def _get_help(self):
        @self.app.route('/help')
        def get_help():
            return Documentation._get_help()

    def _post_file(self):
        @app.route('/{0}'.format('post_and_process_vfk'), methods=['GET', 'POST'])
        def post_file():
            if request.method == 'POST':
                f = request.files['file']
                filename = os.path.join(Configuration.UPLOADED_FILE_LOCATION, secure_filename(f.filename))
                f.save(filename)
                Importer(filename)
                result = DbManager().get_unique_vb()
                if len(result) > 0:
                    return 'File: {0} was saved successfully! Unique IDs are: {1}'.format(filename, str(result))

    def _delete_by_id(self):
        @app.route('/delete/<id>',methods=['DELETE'])
        def delete_by_id(id):
            if request.method == 'DELETE' and id:
                result = DbManager().delete_by_id(id)
                return str(result)
            else:
                return 'Chyba'
 
if __name__ == '__main__':
    try:
        os.environ['FLASK_APP'] = 'server.py'
        app = Server(app).app
        Logger.add_log_item('Server: {0} was successfully started!'.format(Configuration.APPLICATION_NAME), 'SUCCESS', 'SERVER')
        serve(app, host='0.0.0.0', port=6789)
    except:
        Logger.add_log_item('Server: {0} was terminated!'.format(Configuration.APPLICATION_NAME), 'ERROR', 'SERVER')
        sys.exit(0)
