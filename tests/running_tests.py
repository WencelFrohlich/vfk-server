import os
import requests
import time
import json

class TestLogger():
    def passed(message):
        print('[TEST]   "{0}" was passed'.format(message))

    def failed(message):
        print('[TEST]   "{0}" was failed'.format(message))

class Tests():
    TESTS = {
        'GET_HELP' : {
            'name' : 'Test HELP get method',
            'method' : 'get',
            'url' : 'http://0.0.0.0:6789/help'
        },
        'POST_VFK_FILE' : {
            'name' : 'Test posting and processing VFK file',
            'method' : 'post',
            'url' : 'http://0.0.0.0:6789/post_and_process_vfk',
            'files' : [
                '/home/enviwork/Dokumenty/ukol_vfk/vfk_files/624217_ZPMZ_00929_vfk.vfk', 
                '/home/enviwork/Dokumenty/ukol_vfk/vfk_files/654175_ZPMZ_00131_vfk.vfk',
                '/home/enviwork/Dokumenty/ukol_vfk/vfk_files/684007_ZPMZ_00331_vfk.vfk',
                '/home/enviwork/Dokumenty/ukol_vfk/vfk_files/709433_1668EX_229716210010.VFK',
            ]
        },
        'DELETE_BY_ID' : {
            'name' : 'Test deleting VB row by ID',
            'method' : 'delete',
            'url' : 'http://0.0.0.0:6789/delete/',
            'ids' : [74220723999, 74220724999, 74220725999, 74220813999, 74220832999, 74220833999, 74220834999, 74220857999, 74220866999, 74220867999]
        }
    }

class TestsRunner():
    def __init__(self):
        self._kill_server()
        self._run_server()
        self._run_tests()
        self._kill_server()

    def _kill_server(self):
        try:
            os.system('pkill -f "{0}"'.format('server.py'))
        except:
            print('problem with killing test')

    def _run_tests(self):
        for key, value in Tests.TESTS.items():
            if value['method'] == 'get':
                self._get(value['url'], value['name'])
            elif value['method'] == 'post':
                self._post(value['url'], value['name'], value['files'])
            elif value['method'] == 'delete':
                self._delete(value['url'], value['name'], value['ids'])

    def _run_server(self):
        try:
            os.system('python3 server_app/server.py &')
            time.sleep(2)
        except:
            print('Problem with running test')

    def _get(self, url, name):
        try:
            request = requests.get(url)
            if request.ok:
                TestLogger.passed(name)
            else:
                TestLogger.failed(name)
        except:
            TestLogger.failed(name)

    def _post(self, url, name, files):
        for file in files:
            try:
                files = {'file': open(file,'rb')}
                request = requests.post(url, files=files)
                if request.ok:
                    TestLogger.passed(name)
                else:
                    print(request.status_code)
                    TestLogger.failed(name)
            except:
                TestLogger.failed(name)

    def _delete(self, url, name, ids):
        for id in ids:
            try:
                request = requests.delete(url + str(id))
                if request.ok:
                    TestLogger.passed(name + ": {0} with response message: '{1}'".format(str(id), request.text))
                else:
                    print(request.status_code)
                    TestLogger.failed(name + ": {0} with response message: '{1}'".format(str(id), request.text))
            except:
                TestLogger.failed(name + ": {0} with response message: '{1}'".format(str(id), request.text))

if __name__ == '__main__':
    TestsRunner()