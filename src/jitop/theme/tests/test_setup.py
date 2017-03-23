# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from jitop.theme.testing import JITOP_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that jitop.theme is properly installed."""

    layer = JITOP_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if jitop.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'jitop.theme'))

    def test_browserlayer(self):
        """Test that IJitopThemeLayer is registered."""
        from jitop.theme.interfaces import (
            IJitopThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IJitopThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = JITOP_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['jitop.theme'])

    def test_product_uninstalled(self):
        """Test if jitop.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'jitop.theme'))

    def test_browserlayer_removed(self):
        """Test that IJitopThemeLayer is removed."""
        from jitop.theme.interfaces import \
            IJitopThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IJitopThemeLayer, utils.registered_layers())
