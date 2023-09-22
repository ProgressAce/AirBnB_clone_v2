#!/usr/bin/python3
"""Module for testing the console."""

import unittest
import sys
from console import HBNBCommand


class TestCmdCreate(unittest.TestCase):
    """ Testing the console's create command."""

    def setUp(self):
        """ Set up test space."""

        HBNBCommand().cmdloop()

    def test_zero_arg(self):
        """ Create object with no additional arguments."""

        sys.__stdin__ = 'create State'
        self.assertEqual(sys.__stdout__, '')
