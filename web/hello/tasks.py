from web.celery import app

@app.task(name='hello.say_hello')
def say_hello(name: str):
    raise NotImplementedError()


@app.task(name='hello.run_script_output_to_storage')
def run_script_output_to_storage(doc_id: int, peers: list or int, filename: str):
    raise NotImplementedError