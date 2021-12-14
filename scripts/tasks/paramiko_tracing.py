from paramiko import SSHClient

from debug_tracing import trace_params

class TracingSSHClient(SSHClient):
    
    @trace_params(trace_all=True, new_span=True)
    def connect(self, *args, **kwargs):
        return super().connect(*args, **kwargs)

    @trace_params(trace_all=True, new_span=True)
    def exec_command(self, *args, **kwargs):
         return super().exec_command(*args, **kwargs)
