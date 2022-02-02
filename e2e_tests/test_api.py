import os
import requests
import time

from trace_explorer.testsuite.base import Runner

BASE_URL = os.environ.get("BASE_URL", "localhost")

def get_token(username, password):
    data = {
        'username': username,
        'password': password
    }
    resp = requests.post(f"http://{BASE_URL}/api/token/", data=data)
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
        resp = requests.post(f"http://{BASE_URL}/api/task/generic_run", data=data, headers=self.header)
        assert resp.status_code == 200

        task_id = resp.json()['task_id']
        params = {
            'task': task_id
        }
        resp = requests.get(f"http://{BASE_URL}/api/task/result", params=params, headers=self.header)
        while resp.json()['status'] == 'PENDING':
            time.sleep(1)
            resp = requests.get(f"http://{BASE_URL}/api/task/result", params=params, headers=self.header)
        
        assert resp.json()['status'] == 'SUCCESS'