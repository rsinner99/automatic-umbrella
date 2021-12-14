import opentracing
from openstracing_instrumentation.request_context import get_current_span

from worker import DEBUG

def trace_params(trace_all=False, **additional_params):
    if DEBUG:
        trace_all = True
    def decorator(func):
        def wrapper(*args, **kwargs):
            if trace_all:
                span = get_current_span()
                with span:
                    if len(args) > 0:
                        span.set_tag('input.args', args)
                    for k, v in kwargs:
                        span.set_tag('input.{}'.format(k), v)
                    for k, v in additional_params:
                        span.set_tag(k, v)

            result = func(*args, **kwargs)
            if trace_all:
                span.set_tag('output', str(result))
            return result
        return wrapper
    return decorator


