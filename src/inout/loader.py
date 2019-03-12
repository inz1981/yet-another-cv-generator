#!/usr/bin/env python
import json
import yaml


class InputLoader:
    """ Class to handle the loading of files into data structures
    """

    def __init__(self):
        pass

    def load_yaml(self, filepath: str) -> dict:
        """
        Load a yaml file given a path to the file
        :param filepath: path to the file
        :return: dict contents of the yaml file
        """
        with open(filepath, 'r') as ystream:
            try:
                contents = yaml.load(ystream)
                return contents
            except yaml.YAMLError as exc:
                print(exc)

    def load_json(self, filepath: str) -> dict:
        """
        Load a json file given a path to the file
        :param filepath: path to the file
        :return: dict contents of the json file
        :rtype: dict
        """
        with open(filepath) as json_file:
            return json.load(json_file)
