from worker import app
import os, time

from store import Storage
from debug_tracing import trace_params

class FileStorage(Storage):
    name = 'files'

@app.task(name='storage.put_content')
@trace_params(trace_all=True)
def put_content(content: str, filename: str):
    if not isinstance(content, str):
        raise TypeError(f'content is of type {type(content)}, but expected "str"')
    if not isinstance(filename, str):
        raise TypeError(f'filenameis of type {type(filename)}, but expected "str"')
    store = FileStorage()
    path = f'/tmp/{filename}'
    with open(path, 'w') as f:
        f.write(str(content))
    obj = store.fput(filename, path)
    if not obj:
        raise ConnectionError('Content could not be stored in MinIO')
    os.remove(path)
    result = {
        'object_name': obj.object_name,
        'version_id': obj.version_id,
        'location': obj.location
    }
    return result

@app.task(name='storage.get_content')
@trace_params(trace_all=True)
def get_content(filename: str):
    if not isinstance(filename, str):
        raise TypeError('filename is not of type "str"')
    store = FileStorage()
    path = f'/tmp/{filename}'
    store.fget(filename, path)
    with open(path, 'r') as f:
        content = f.read()
    os.remove(path)

    return {
        'filename': filename,
        'content': content
    }

@app.task(name='storage.list_files')
@trace_params(trace_all=True)
def list_files(prefix=None, include_version=False):
    time.sleep(2)
    store = FileStorage()
    result = store.list(prefix=None, include_version=False)
    return {
        'files': result
    }

@app.task(name='scripts.run_script')
def run_script(doc_id, peers):
    raise NotImplementedError()
