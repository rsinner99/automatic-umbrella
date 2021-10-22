from time import sleep

from config import app


@app.task(name='hello.say_hello')
def say_hello(name: str):
    sleep(5) 
    return f"Hello {name}"
