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
                    span = tracer.start_span(func.__name__)

                with span:
                    if len(args) > 0:
                        span.set_attribute('input.args', args)
                    for k, v in kwargs.items():
                        span.set_attribute('input.{}'.format(k), str(v))
                    for k, v in additional_params.items():
                        span.set_attribute(k, str(v))

                    result = func(*args, **kwargs)
                    span.set_attribute('output', str(result))

            else:
                result = func(*args, **kwargs)
            
            return result
        return wrapper
    return decorator
