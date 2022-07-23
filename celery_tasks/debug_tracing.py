import traceback
from opentelemetry import trace
from opentelemetry.trace.propagation import get_current_span

from worker import DEBUG

def trace_params(trace_all=False, new_span=False, **additional_params):
    if DEBUG:
        trace_all = True
    def decorator(func):
        def wrapper(*args, **kwargs):
            if trace_all:
                span = get_current_span()
                if new_span:
                    tracer = trace.get_tracer_provider().get_tracer(__name__)
                    span = tracer.start_span(func.__name__, child_of=span)
                with span:
                    if len(args) > 0:
                        span.set_attribute('input.args', args)
                    for k, v in kwargs.items():
                        span.set_attribute('input.{}'.format(k), v)
                    for k, v in additional_params.items():
                        span.set_attribute(k, v)
            try:
                result = func(*args, **kwargs)
                if trace_all:
                    span.set_attribute('output', str(result))
                return result
            except Exception as e:
                span.add_event({
                    "event": 'error',
                    "kind": type(e),
                    "object": e,
                    "message": str(e),
                    "stack": traceback.format_exc()
                })
        return wrapper
    return decorator


