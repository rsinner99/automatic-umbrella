import paramiko
import requests
import io

from paramiko_tracing import TracingSSHClient
from settings import API_URL

SUCCESS = 200

def get_doc(doc_id: int):
    resp = requests.get(API_URL + f'scripts/doc/{doc_id}/')
    if resp.status_code == SUCCESS:
        return resp.json()
    else:
        raise Exception(resp.content)

def get_peer_and_account(peer_id: int):
    resp = requests.get(API_URL + f'scripts/peer/{peer_id}/')
    if resp.status_code == SUCCESS:
        return resp.json()
    else:
        raise Exception(resp.content)

def connect(peer: dict):
    errors = []
    ssh = TracingSSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    host = peer.get('hostname', None)
    if not host:
        host = peer.get('ip_address', None)
    username = peer.get('username', None)
    port = peer.get('ssh_port', 22)
    pkey = peer.get('private_key', None)
    conn = None
    if pkey:
        try:
            mock_file = io.StringIO.StringIO(pkey)
            pkey = paramiko.RSAKey.from_private_key(mock_file)
            passphrase = peer.get('passphrase', '')
            ssh.connect(host, port=port, username=username, password=passphrase, pkey=pkey)
        except Exception as e:
            errors.append(e)
    
    if errors or not pkey:
        try:
            password = peer.get('password')
            ssh.connect(host, port=port, username=username, password=password)
        except Exception as e:
            errors.append(e)
            return errors
    
    return ssh
