from worker import app
from time import sleep
from celery import group



@app.task(name='hello.say_hello')
def say_hello(name: str):
    sleep(5) 
    return f"Hello {name}"

@app.task(name='storage.put_content')
def put_content(content, filename):
    raise NotImplementedError()

@app.task(name='scripts.run_script')
def run_script(doc_id, peers):
    raise NotImplementedError()


@app.task(name='hello.run_script_output_to_storage')
def run_script_output_to_storage(doc_id: int, peers: list or int, filename: str):
    if isinstance(peers, int):
        peers = [peers]

    task_list = []
    children = []
    for peer_id in peers:
        out_name = f"{filename}_doc{doc_id}_peer{peer_id}.txt"
        sig1 = run_script.s(doc_id, peer_id) # create signature
        sig2 = put_content.s(out_name)
        chain = ( sig1 | sig2 )
        ar1 = sig1.freeze() # without freeze(), the subtask id is not accessible at this point
        ar2 = sig2.freeze()
        task_list.append(chain)
        children.append({'task_id': [ar1.id, ar2.id], 'peer': peer_id, 'doc': doc_id})
    g = group(task_list).apply_async()
    return {
        'task_id': g.id,
        'children': children
    }

