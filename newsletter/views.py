from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from django.template.loader import render_to_string

from .models import NewsletterSubscriber
from .forms import NewsletterForm


def subscribe(request):
    form = NewsletterForm(request.POST or None)
    next_url = request.GET.get('next') or request.META.get('HTTP_REFERER') or '/'

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)

        if subscriber.is_confirmed:
            messages.info(request, "You're already subscribed to our newsletter.")
        else:
            confirm_url = request.build_absolute_uri(
                reverse('confirm_subscription', args=[subscriber.confirmation_token])
            )
            unsubscribe_url = request.build_absolute_uri(
                reverse('unsubscribe', args=[subscriber.unsubscribe_token])
            )

            # Render HTML email content
            html_message = render_to_string("newsletter/emails/confirm_subscription.html", {
                'email': email,
                'unsubscribe_url': unsubscribe_url,
                'confirm_url': confirm_url
            })

            subject = "Confirm your LaunchPad Africa Newsletter Subscription"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [email]

            # Send email with HTML alternative
            email_message = EmailMultiAlternatives(subject, '', from_email, to_email)
            email_message.attach_alternative(html_message, "text/html")
            email_message.send()

            messages.success(request, "A confirmation link has been sent to your email.")

        return redirect(next_url)

    # If GET request, just redirect (no form rendered here directly)
    return redirect('/')


def confirm_subscription(request, token):
    subscriber = get_object_or_404(NewsletterSubscriber, confirmation_token=token)
    subscriber.is_confirmed = True
    subscriber.save()
    return render(request, 'newsletter/confirmed.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import NewsletterSubscriber

def unsubscribe(request, token):
    try:
        subscriber = NewsletterSubscriber.objects.get(unsubscribe_token=token)
        
        if not subscriber.is_confirmed:
            messages.info(request, "You are already unsubscribed.")
        else:
            subscriber.is_confirmed = False
            subscriber.save()
            messages.success(request, "You have been unsubscribed successfully.")

        return render(request, 'newsletter/unsubscribed.html')

    except NewsletterSubscriber.DoesNotExist:
        # Handle invalid token
        messages.error(request, "Invalid or expired unsubscribe link.")
        return render(request, 'newsletter/unsubscribe_invalid.html')

