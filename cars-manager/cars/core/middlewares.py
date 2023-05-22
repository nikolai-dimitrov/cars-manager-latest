from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout


class ActiveUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            return
        if hasattr(request.user, 'profile'):
            if not request.user.profile.is_banned:
                return
            if request.user.profile.is_banned:
                logout(request)
