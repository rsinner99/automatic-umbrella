from producer.celery import app

@app.task(name='hello.say_hello')
def say_hello(name: str):
    pass
