#!/usr/bin/env python
import json
import unittest

import utils
from inout.loader import InputLoader


class TestReadInput(unittest.TestCase):

    def test_load_yamlfile(self):
        # Given the user has configured a resume file
        yamlfile = 'input.yaml'
        my_loader = InputLoader()

        # When parsing the file
        actual = my_loader.load_yaml(utils.get_test_resources_path(yamlfile))

        # Then the contents are read successfully
        expected = my_loader.load_json(utils.get_test_resources_path(
            'expected/exp_yaml_output.json'))
        expected = json.dumps(expected, sort_keys=True, indent=2)
        actual = json.dumps(actual, sort_keys=True, indent=2)
        self.assertEqual(actual, expected)

    def test_load_unknown_yamlfile(self):
        # Given the user has not configured a resume file
        yamlfile = 'imaginary.yaml'
        my_loader = InputLoader()

        # When parsing the file
        # Then an error is thrown
        with self.assertRaises(FileNotFoundError):
            my_loader.load_yaml(yamlfile)

    def test_load_unknown_jsonfile(self):
        # Given the user has no json file
        jsonfile = 'imaginary.json'
        my_loader = InputLoader()

        # When parsing the file
        # Then an error is thrown
        with self.assertRaises(FileNotFoundError):
            my_loader.load_json(jsonfile)
