from worker import app
import paramiko
from celery import group


from utils import get_doc, get_peer_and_account, connect
import run


DOC_TYPE_BASH = 'sh'
DOC_TYPE_PYTHON = 'py'

@app.task(name='scripts.run_script')
def run_script(doc_id: int, peers: list or int):
    if isinstance(peers, list):
        if len(peers) > 1:
            task_list = []
            children = []
            for peer_id in peers:
                sig = run_script.s(doc_id, peer_id) # create signature
                ar = sig.freeze() # without freeze(), the subtask id is not accessible at this point
                task_list.append(sig)
                children.append({'task_id': ar.id, 'peer': peer_id, 'doc': doc_id})
            g = group(task_list).apply_async()
            return {
                'task_id': g.id,
                'children': children
            }
        else:
            peers = peers[0]

    result = {
        'output': None,
        'error': None
    }
    doc = get_doc(doc_id)
    peer = get_peer_and_account(peers)
    script = doc.get('content')

    ssh = connect(peer)
    if isinstance(ssh, list):
        result['error'] = ssh
        return result

    file_type = doc.get('type', None)
    if not file_type:
        result['error'] = 'File type is not set.'
    elif file_type == DOC_TYPE_BASH:
        result = run.run_bash(ssh, script)
    elif file_type == DOC_TYPE_PYTHON:
        result = run.run_python(ssh, script)
    else:
        result['error'] = f'Invalid file type: "{file_type}".'

    return result

@app.task(name='storage.put_content')
def put_content(content, filename):
    raise NotImplementedError()
