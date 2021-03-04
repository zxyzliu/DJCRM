from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class AdminLoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organisor:
            return redirect("leads:allList")
        return super().dispatch(request, *args, **kwargs)
