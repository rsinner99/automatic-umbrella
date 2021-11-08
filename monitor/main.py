from network_graph import run
from worker import app

OUT_FILE = "docker-graph.svg"

@app.task(name="monitor.build_network_graph")
def build_network_graph():
    run.generate_graph(True, OUT_FILE)
    with open(OUT_FILE, 'r') as f:
        content = f.read()
    return content
