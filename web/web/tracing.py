import os
import MySQLdb

from django.conf import settings

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.dbapi import trace_integration

REPORTING_HOST = os.environ.get('TRACING_REPORTING_HOST')
REPORTING_PORT = os.environ.get('TRACING_REPORTING_PORT')

class TracingHeaderMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if settings.DEBUG:
            span = trace.propagation.get_current_span()
            for k, v in request.META.items():
                span.set_attribute(f"headers.{k}", v)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

def setup_tracing(service="umbrella"):
    # This call is what makes the Django application be instrumented
    DjangoInstrumentor().instrument()
    RequestsInstrumentor().instrument()
    trace_integration(MySQLdb, "connect", "mysql")

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