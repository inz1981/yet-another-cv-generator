#!/usr/bin/env python
import os
import shutil
import unittest

import utils
from inout.loader import InputLoader
from inout.writer import OutputWriter


class TestWriteMarkdown(unittest.TestCase):

    def tearDown(self):
        test_build = os.path.join(utils.get_root_path(), 'build', 'testoutput')
        if os.path.exists(test_build) and os.path.isdir(test_build):
            shutil.rmtree(test_build)

    def test_write_complete_markdown(self):
        # Given the user wants to write the CV as markdown format
        inputdata = 'input_complete.json'
        my_writer = OutputWriter(filetype='markdown')
        my_loader = InputLoader()
        json_data = my_loader.load_json(utils.get_test_resources_path(
            inputdata))

        # When writing the markdown file
        my_writer.generate_output(json_data)
        outputfile = os.path.join(
            utils.get_test_build_dir(), 'test_write_complete_markdown.md')
        my_writer.save_outputfile(filepath=outputfile)

        # Then the contents of the markdown file is correct
        expected = utils.load_file_contents(utils.get_test_resources_path(
            'expected/markdown.md'))
        actual = utils.load_file_contents(outputfile)
        self.assertEqual(expected, actual)


class TestWriteHtml(unittest.TestCase):

    def tearDown(self):
        test_build = os.path.join(utils.get_root_path(), 'build', 'testoutput')
        if os.path.exists(test_build) and os.path.isdir(test_build):
            shutil.rmtree(test_build)

    def test_write_complete_html(self):
        # Given the user wants to write the CV as HTML format
        inputdata = 'input_complete.json'
        my_writer = OutputWriter(filetype='html')
        my_loader = InputLoader()
        json_data = my_loader.load_json(utils.get_test_resources_path(
            inputdata))

        # When writing the html file
        my_writer.generate_output(json_data)
        outputfile = os.path.join(utils.get_test_build_dir(),
                                  'test_write_complete_html.html')
        my_writer.save_outputfile(filepath=outputfile)

        # Then the contents of the html file is correct
        expected = utils.load_file_contents(utils.get_test_resources_path(
            'expected/html.html'))
        actual = utils.load_file_contents(outputfile)
        self.assertEqual(expected, actual)
