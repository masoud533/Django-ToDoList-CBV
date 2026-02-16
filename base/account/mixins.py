from django.shortcuts import redirect

# Mixin to redirect authenticated users away from auth-only views
# (e.g. login or signup pages).
class RedirectAuthenticatedUserMixin:
    # Named URL to redirect authenticated users to.
    # Keeping this as a class attribute allows easy override per view.
    redirect_url = 'tasks:list'

    def dispatch(self, request, *args, **kwargs):

        # Intercept the request early to prevent authenticated users
        # from accessing this view.
        if request.user.is_authenticated:
            return redirect(self.redirect_url)

        # Proceed with the normal view lifecycle for unauthenticated users.
        return super().dispatch(request, *args, **kwargs)
