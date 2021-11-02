import os
import opentracing
from jaeger_client import Config

REPORTING_HOST = os.environ.get('TRACING_REPORTING_HOST')
REPORTING_PORT = os.environ.get('TRACING_REPORTING_PORT')

tracer_map = {}

def get_tracer(service='worker'):
    global tracer_map
    tracer = tracer_map.get(service, None)
    if tracer:
        return tracer
    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
             'reporting_host': REPORTING_HOST,
             'reporting_port': REPORTING_PORT,
            },
            'logging': True,
        },
        service_name=service,
        validate=True,
     )

    if config._initialized:
        tracer = config.new_tracer() # create additional tracers (e.g. to create spans for database requests or git/docs)
    else:
        tracer = config.initialize_tracer()
    tracer_map[service] = tracer
    return tracer

