from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse

from rest_framework_api_key.models import APIKey

from .forms import APIKeyRequestForm  # Adjust import as needed


class APIKeyRequestView(View):
    template_name = "api_key/request.html"

    def get(self, request):
        form = APIKeyRequestForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = APIKeyRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            name = form.cleaned_data.get("name", "")

            existing_key = APIKey.objects.filter(name=email).first()
            if existing_key:
                # Key already exists — no access to raw key string here
                messages.info(
                    request,
                    "An API key has already been generated for this email. "
                    "If you lost it, please contact support or revoke the old key and generate a new one."
                )
                return render(request, self.template_name, {"form": form})

            # Create new API key (returns object and raw key string)
            key_obj, key = APIKey.objects.create_key(name=email)

            # Prepare and send email with the key
            subject = "Your LaunchPad API Key"
            context = {"name": name, "key": key, "is_new": True}
            html_content = render_to_string("api_key/email.html", context)
            text_content = strip_tags(html_content)

            msg = EmailMultiAlternatives(subject, text_content, to=[email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, "Your new API key has been generated and sent to your email.")
            return redirect(reverse("api-key-request"))

        # If form invalid, re-render with errors
        return render(request, self.template_name, {"form": form})
