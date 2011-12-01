# Test file.
# Copyright (C) 2011 David Guerrero
# This file is distributed under the license terms of the LICENSE file.
# David Guerrero <dguerrer@polytch.unice.fr>, 2011.

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
