import os
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

REPORTING_HOST = os.environ.get('TRACING_REPORTING_HOST')
REPORTING_PORT = os.environ.get('TRACING_REPORTING_PORT')

def setup_tracing(service="umbrella"):
    CeleryInstrumentor().instrument()
    RequestsInstrumentor().instrument()

    trace.set_tracer_provider(
    TracerProvider(
            resource=Resource.create({SERVICE_NAME: service})
        )
    )
    tracer = trace.get_tracer(__name__)

    # create a JaegerExporter
    jaeger_exporter = JaegerExporter(
        # configure agent
        agent_host_name=REPORTING_HOST,
        agent_port=int(REPORTING_PORT),
        # optional: configure also collector
        # collector_endpoint='http://localhost:14268/api/traces?format=jaeger.thrift',
        # username=xxxx, # optional
        # password=xxxx, # optional
        # max_tag_value_length=None # optional
    )

    # Create a BatchSpanProcessor and add the exporter to it
    span_processor = BatchSpanProcessor(jaeger_exporter)

    # add to the tracer
    trace.get_tracer_provider().add_span_processor(span_processor)


def initialize_tracing(service="worker"):
    tracer = setup_tracing(service)
