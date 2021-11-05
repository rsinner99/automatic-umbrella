from web.celery import app

@app.task(name="monitor.build_network_graph")
def build_network_graph():
    raise NotImplementedError()