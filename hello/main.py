from time import sleep

from worker import app


@app.task(name='hello.say_hello')
def say_hello(name: str):
    sleep(5) 
    return f"Hello {name}"

@app.task(name='storage.put_content')
def put_content(content, filename):
    raise NotImplementedError()

@app.task(name='scripts.run_script')
def run_script(doc_id, peers):
    raise NotImplementedError()
