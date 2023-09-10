#!/usr/bin/python3
import os
import unittest
from os import path
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
""" testing the file storage"""


class TestCaseFileStorage(unittest.TestCase):
    """ class for test cases """

    def setUp(self):
        """ setting up the various
            components for the test """
        self.dir_path = 'file.json'
        self.my_model = FileStorage()

    def tearDown(self):
        """ dispose json file """
        if path.exists(self.dir_path):
            os.remove(self.dir_path)

    def test_all(self):
        """ check type return by all function """
        self.assertEqual(type(self.my_model.all()), dict)

    def test_new(self):
        test_model = BaseModel()
        self.my_model.new(test_model)
        len_dict = len(self.my_model.all())
        self.assertGreater(len_dict, 0)

    def test_save(self):
        """ save content to file
         and create if not exist"""
        self.my_model.save()
        self.assertEqual(path.exists(self.dir_path), True)

    def test_reload(self):
        model = FileStorage()
        self.my_model.reload()
        len_dict = len(model.all())
        self.assertGreater(len_dict, 0)
