from web.celery import app

@app.task(name='hello.say_hello')
def say_hello(name: str):
    raise NotImplementedError()
