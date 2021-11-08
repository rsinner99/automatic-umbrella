from web.celery import app

@app.task(name='calc.estimate_pi')
def estimate_pi(interval=1000):
    raise NotImplementedError()