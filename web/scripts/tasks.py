from web.celery import app

@app.task(name='scripts.run_script')
def run_script(doc_id: int, peer_id):
    raise NotImplementedError()
