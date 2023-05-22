from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from functools import wraps


def unauthenticated_required(view_f):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')

        return view_f(request, *args, **kwargs)

    return wraps(view_f)(wrapped_view)


def profile_required(view_f):
    def wrapped_view(request, *args, **kwargs):
        if not hasattr(request.user, 'profile'):
            raise PermissionDenied()
        if not request.user.profile.is_activated:
            raise PermissionDenied()

        return view_f(request, *args, **kwargs)

    return wraps(view_f)(wrapped_view)


def staff_required(view_f):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied()

        return view_f(request, *args, **kwargs)

    return wraps(view_f)(wrapped_view)
