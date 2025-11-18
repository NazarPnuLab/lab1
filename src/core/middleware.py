from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class EnsureCORSHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Handle preflight OPTIONS requests first
        if request.method == "OPTIONS":
            response = HttpResponse(status=204)
            # Do not set Access-Control-Allow-Origin here to avoid duplicates with nginx
            response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS, PATCH"
            response["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Requested-With, Accept, Origin"
            response["Access-Control-Max-Age"] = "86400"
            return response
        
        # Normal requests: do not alter CORS headers; let nginx handle Allow-Origin
        response = self.get_response(request)
        return response


class DisableCSRFForAPI(MiddlewareMixin):
    """
    Disable CSRF for API endpoints even for authenticated users
    """
    def process_request(self, request):
        if request.path.startswith('/api/'):
            setattr(request, '_dont_enforce_csrf_checks', True)
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith('/api/'):
            setattr(request, '_dont_enforce_csrf_checks', True) 