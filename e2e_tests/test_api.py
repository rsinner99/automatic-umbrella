import requests
import time

from tracing_rca.testsuite.base import Runner

BASE_URL = "http://192.168.84.7/"

def get_token(username, password):
    data = {
        'username': username,
        'password': password
    }
    resp = requests.post(BASE_URL + "api/token/", data=data)
    if resp.status_code == 200:
        return resp.json()['access']
    else:
        raise Exception('Token generation failed')


class PingTaskApiTest(Runner):
    def setUp(self):
        token = get_token('test', 'test1234test')
        self.header = {
            'Authorization': 'Bearer ' + token
        }

    def test_task(self):
        data = {
            "taskname":"hello.say_hello",
            "name":"TestPostman"
        }
        resp = requests.post(BASE_URL + "api/task/generic_run", data=data, headers=self.header)
        assert resp.status_code == 200

        task_id = resp.json()['task_id']
        params = {
            'task': task_id
        }
        resp = requests.get(BASE_URL + "api/task/result", params=params, headers=self.header)
        while resp.json()['status'] == 'PENDING':
            time.sleep(1)
            resp = requests.get(BASE_URL + "api/task/result", params=params, headers=self.header)
        
        assert resp.json()['status'] == 'SUCCESS'