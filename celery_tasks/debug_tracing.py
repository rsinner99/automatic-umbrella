import traceback
import opentracing
from opentracing import logs, tags
from opentracing_instrumentation.request_context import get_current_span

from worker import DEBUG

def trace_params(trace_all=False, new_span=False, **additional_params):
    if DEBUG:
        trace_all = True
    def decorator(func):
        def wrapper(*args, **kwargs):
            if trace_all:
                span = get_current_span()
                if new_span:
                    span = opentracing.tracer.start_span(func.__name__, child_of=span)
                with span:
                    if len(args) > 0:
                        span.set_tag('input.args', args)
                    for k, v in kwargs.items():
                        span.set_tag('input.{}'.format(k), v)
                    for k, v in additional_params.items():
                        span.set_tag(k, v)
            try:
                result = func(*args, **kwargs)
                if trace_all:
                    span.set_tag('output', str(result))
                return result
            except Exception as e:
                span.set_tag(tags.ERROR, True)
                span.log_kv({
                    logs.EVENT: 'error',
                    logs.ERROR_KIND: type(e),
                    logs.ERROR_OBJECT: e,
                    logs.MESSAGE: str(e),
                    logs.STACK: traceback.format_exc()
                })
        return wrapper
    return decorator


