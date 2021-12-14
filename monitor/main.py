from network_graph import run
from worker import app

from debug_tracing import trace_params

OUT_FILE = "docker-graph.svg"

@app.task(name="monitor.build_network_graph")
@trace_params(trace_all=True)
def build_network_graph():
    run.generate_graph(True, OUT_FILE)
    with open(OUT_FILE, 'r') as f:
        content = f.read()
    return content
