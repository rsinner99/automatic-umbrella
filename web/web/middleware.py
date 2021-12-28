from django.contrib.auth.models import AnonymousUser
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication


class DisableCSRFMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response


class JWTAuthenticationMiddleware(object):
    """
    Middleware for authenticating JSON Web Tokens in Authorize Header
    Inspects the token for the user_id,
    attempts to get that user from the DB & assigns the user on the
    request object. Otherwise it defaults to AnonymousUser.

    This will work with existing decorators like LoginRequired.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            user_jwt = JWTAuthentication().authenticate(Request(request))
            if user_jwt is not None:
                # store the first part of the tuple (user, obj)
                request.user = user_jwt[0]
        except Exception as exc:
            pass
        request.user = request.user or AnonymousUser()
        return self.get_response(request)
