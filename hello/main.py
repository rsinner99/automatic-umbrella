from time import sleep

from config import app


@app.task(name='hello.say_hello')
def say_hello(name: str):
    sleep(5) 
    return f"Hello {name}"


# create celery app
app.register_task(say_hello)

# start worker
if __name__ == '__main__':
    app.worker_main()