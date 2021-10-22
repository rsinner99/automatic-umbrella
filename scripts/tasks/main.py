import paramiko

from config import app
from utils import get_doc, get_peer_and_account, connect
import run

DOC_TYPE_BASH = 'sh'
DOC_TYPE_PYTHON = 'py'

@app.task(name='scripts.run_script')
def run_script(doc_id: int, peer_id):
    result = {
        'output': None,
        'error': None
    }
    doc = get_doc(doc_id)
    peer = get_peer_and_account(peer_id)
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


