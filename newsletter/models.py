import uuid
from django.db import models

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    is_confirmed = models.BooleanField(default=False)
    confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False)
    unsubscribe_token = models.UUIDField(default=uuid.uuid4, editable=False)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email