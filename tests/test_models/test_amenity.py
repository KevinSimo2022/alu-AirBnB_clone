#!/usr/bin/python3
"""Unittest for the amenity class"""

import unittest
from models.amenity import Amenity
import datetime


class testAmenity(unittest.TestCase):
    """tests for methods and instances"""

    ameni = Amenity()

    def test_class(self):
        """check class"""
        abs = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.ameni)), abs)

    def test_inheritance(self):
        """check if it inherited"""
        self.assertIsInstance(self.ameni, Amenity)

    def test_attrs(self):
        """check the attributes"""
        self.assertTrue(hasattr(self.ameni, 'id'))
        self.assertTrue(hasattr(self.ameni, 'created_at'))
        self.assertTrue(hasattr(self.ameni, 'name'))
        self.assertTrue(hasattr(self.ameni, 'updated_at'))

    def test_type(self):
        """check the attribute type"""
        self.assertIsInstance(self.ameni.id, str)
        self.assertIsInstance(self.ameni.name, str)
        self.assertIsInstance(self.ameni.updated_at, datetime.datetime)
        self.assertIsInstance(self.ameni.created_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
