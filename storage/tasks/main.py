from config import app
from store import Storage

class FileStorage(Storage):
    name = 'files'

@app.task(name='storage.put_content')
def put_content(filename, content):
    store = FileStorage()
    object = store.put(filename, content, -1)
    result = {
        'object_name': object.object_name,
        'version_id': object.version_id,
        'location': object.location
    }
    return result

@app.task(name='storage.get_content')
def get_content(filename):
    store = FileStorage()
    result = store.get(filename)
    return result