from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_api_key.models import APIKey
from core.models import APIKeyMeta, Startup, Sector

class StartupAPITest(APITestCase):
    def setUp(self):
        # Create a Sector instance for the foreign key
        self.sector = Sector.objects.create(name="Tech")

        # Create API key and metadata
        self.api_key_obj, self.key = APIKey.objects.create_key(name="Test Key")
        APIKeyMeta.objects.create(api_key=self.api_key_obj, email="test@example.com")

        # Create sample Startup linked to Sector
        Startup.objects.create(
            name="Test Startup",
            description="Test description",
            location="Test Location",
            sector=self.sector
        )

        # URL for the startup list endpoint
        self.url = reverse("startup-list")

    def test_access_without_api_key(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_access_with_valid_api_key(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Api-Key {self.key}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Optional: Check that our startup is in the response
        data = response.json()
        self.assertTrue(any(item['name'] == "Test Startup" for item in data))

    def test_request_count_increment(self):
        # Perform a request with the API key
        self.client.get(self.url, HTTP_AUTHORIZATION=f"Api-Key {self.key}")

        # Refresh meta to get updated count
        meta = APIKeyMeta.objects.get(api_key=self.api_key_obj)
        self.assertEqual(meta.request_count, 1)

    def test_revoked_api_key(self):
        # Revoke the API key
        self.api_key_obj.revoked = True
        self.api_key_obj.save()

        # Attempt access with revoked key
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Api-Key {self.key}")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
