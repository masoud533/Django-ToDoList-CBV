from django.shortcuts import redirect

class RedirectAuthenticatedUserMixin:
    redirect_url = 'tasks:list'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)