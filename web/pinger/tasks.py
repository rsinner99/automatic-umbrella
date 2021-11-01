from web.celery import app

@app.task(name='pinger.ping_host')
def ping_host(host: str, timeout=2):
    raise NotImplementedError()

@app.task(name='pinger.discover')
def discover(subnet: str, timeout=2):
    raise NotImplementedError()