from web.celery import app

@app.task(name='storage.put_content')
def put_content(content, filename):
    raise NotImplementedError()

@app.task(name='storage.get_content')
def get_content(filename):
    raise NotImplementedError()

@app.task(name='storage.list_files')
def list_files(prefix=None):
    raise NotImplementedError()