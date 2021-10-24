import os

from config import app
from store import Storage

class FileStorage(Storage):
    name = 'files'

@app.task(name='storage.put_content')
def put_content(filename: str, content: str):
    store = FileStorage()
    path = f'/tmp/{filename}'
    with open(path, 'w') as f:
        f.write(content)
    object = store.fput(filename, path)
    os.remove(path)
    result = {
        'object_name': object.object_name,
        'version_id': object.version_id,
        'location': object.location
    }
    return result

@app.task(name='storage.get_content')
def get_content(filename: str):
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
def list_files(prefix=None, include_version=False):
    store = FileStorage()
    result = store.list(prefix=None, include_version=False)
    return {
        'files': result
    }