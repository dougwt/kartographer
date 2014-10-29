"""Unit tests for comparison.models."""

from django.http import HttpRequest
from django.test import TestCase

from .models import ConfigList, ConfigListItem, KartConfig


class KartConfigTestCase(TestCase):
    """Tests for KartConfig model."""
    fixtures = [
        'racer.json',
        'racerstats.json',
        'body.json',
        'tire.json',
        'glider.json',
    ]

    def test_valid(self):
        """Test for invalid Racer id."""
        test_kart_ids = (1, 1, 1, 1)
        self.assertTrue(KartConfig(test_kart_ids).valid)

    def test_invalid_racer(self):
        """Test for invalid Racer id."""
        test_kart_ids = (99, 1, 1, 1)
        self.assertFalse(KartConfig(test_kart_ids).valid)

    def test_invalid_body(self):
        """Test for invalid Body id."""
        test_kart_ids = (1, 99, 1, 1)
        self.assertFalse(KartConfig(test_kart_ids).valid)

    def test_invalid_tire(self):
        """Test for invalid Tire id."""
        test_kart_ids = (1, 1, 99, 1)
        self.assertFalse(KartConfig(test_kart_ids).valid)

    def test_invalid_glider(self):
        """Test for invalid Glider id."""
        test_kart_ids = (1, 1, 1, 99)
        self.assertFalse(KartConfig(test_kart_ids).valid)


class ConfigListTestCase(TestCase):
    """Tests for ConfigList and ConfigListItem models."""
    fixtures = [
        'racer.json',
        'racerstats.json',
        'body.json',
        'tire.json',
        'glider.json',
    ]

    def test_create(self):
        """Test ConfigList.create and ConfigListItem.create."""
        # Initialize mock request
        mock_request = HttpRequest()
        mock_request.META = {
            'HTTP_X_REAL_IP': '127.0.0.1',
            'REMOTE_ADDR': '172.31.233.133',
        }

        # Create a ConfigList
        self.assertEqual(len(ConfigList.objects.all()), 0)
        config_list = ConfigList.create(mock_request)
        config_list.save()
        self.assertEqual(len(ConfigList.objects.all()), 1)

        # Create multiple ConfigListItems
        self.assertEqual(len(ConfigListItem.objects.all()), 0)
        test_kart_ids = (
            (8, 19, 2, 2),  # Shyguy
            (9, 2, 14, 2),  # Koopa Troopa
        )
        for kart in test_kart_ids:
            config = KartConfig(kart)
            ConfigListItem.create(
                config_list,
                config.racer,
                config.body,
                config.tire,
                config.glider
            ).save()
        self.assertEqual(len(ConfigListItem.objects.all()), 2)

        # Now try to load the ConfigList by url_hash
        self.assertEqual(
            ConfigList.objects.get(url=config_list.url),
            config_list
        )

        # Ensure it contains the 2 ConfigListItems
        result = ConfigListItem.objects.filter(list_id=config_list.id)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].racer.id, 8)
        self.assertEqual(result[1].racer.id, 9)
