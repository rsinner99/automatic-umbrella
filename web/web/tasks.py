from .celery import app

@app.task(name='common.run_script_output_to_storage')
def run_script_output_to_storage(doc_id: int, peers: list or int, filename: str):
    raise NotImplementedError