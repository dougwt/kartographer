"""Unit tests for comparison.urls."""

from django.test import TestCase
from django.core.urlresolvers import resolve


class URLTestCase(TestCase):

    def test_home(self):
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'home')

    def test_components(self):
        resolver = resolve('/kart-components/')
        self.assertEqual(resolver.view_name, 'components')

    def test_reset(self):
        resolver = resolve('/reset/')
        self.assertEqual(resolver.view_name, 'reset')

    def test_save(self):
        resolver = resolve('/save/')
        self.assertEqual(resolver.view_name, 'save')

    def test_top(self):
        resolver = resolve('/top/')
        self.assertEqual(resolver.view_name, 'top')

    def test_list_valid(self):
        resolver = resolve('/l/fffff/')
        self.assertEqual(resolver.view_name, 'list')
