from web.celery import app

@app.task(name='storage.put_content')
def put_content(filename, content):
    raise NotImplementedError()

@app.task(name='storage.get_content')
def get_content(filename):
    raise NotImplementedError()

@app.task(name='storage.put_file')
def put_file(filename, filepath):
    raise NotImplementedError()