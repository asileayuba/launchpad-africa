from rest_framework_api_key.permissions import BaseHasAPIKey
from rest_framework_api_key.models import APIKey
from core.models import APIKeyMeta

class HasAPIKeyWithCount(BaseHasAPIKey):
    model = APIKey

    def has_permission(self, request, view):
        has_key = super().has_permission(request, view)
        if has_key:
            api_key = request.auth  # This is the APIKey instance
            if api_key:
                try:
                    meta = api_key.meta  # Access related APIKeyMeta
                    meta.request_count += 1
                    meta.revoked = api_key.revoked  # Sync revoked status from APIKey model
                    meta.save()
                    print(f"Updated APIKeyMeta: {meta.email}, count: {meta.request_count}, revoked: {meta.revoked}")
                except APIKeyMeta.DoesNotExist:
                    print(f"No APIKeyMeta for APIKey: {api_key.name}")
        return has_key
