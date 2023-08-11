from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


class logoutmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # exclude register and login from the excludedlinks when not authorised, stored them in a list
        allowed_urls = [reverse("login"), reverse("register"), reverse("logout")]
        if not request.user.is_authenticated and request.path not in allowed_urls:
            messages.error(request, "You must first login !")
            return redirect("login")

        return response
