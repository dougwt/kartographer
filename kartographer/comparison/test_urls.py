"""Unit tests for comparison.urls."""

from django.test import TestCase
from django.core.urlresolvers import resolve


class URLTestCase(TestCase):
    """Tests for url resolution."""

    def test_home(self):
        """Ensure home url resolves to home view."""
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'home')

    def test_components(self):
        """Ensure components url resolves to components view."""
        resolver = resolve('/kart-components/')
        self.assertEqual(resolver.view_name, 'components')

    def test_reset(self):
        """Ensure reset url resolves to reset view."""
        resolver = resolve('/reset/')
        self.assertEqual(resolver.view_name, 'reset')

    def test_save(self):
        """Ensure save url resolves to save view."""
        resolver = resolve('/save/')
        self.assertEqual(resolver.view_name, 'save')

    def test_list_valid(self):
        """Ensure list url resolves to list view."""
        resolver = resolve('/l/fffff/')
        self.assertEqual(resolver.view_name, 'list')

    def test_top(self):
        """Ensure top url resolves to top view."""
        resolver = resolve('/top/')
        self.assertEqual(resolver.view_name, 'top')
