#!/usr/bin/env python
import unittest
import shutil
from testutils.utils import *
from output.outputwriter import OutputWriter
from input.inputloader import InputLoader


class TestWriteMarkdown(unittest.TestCase):

    def tearDown(self):
        test_build = os.path.join(get_root_path(), 'build', 'testoutput')
        if os.path.exists(test_build) and os.path.isdir(test_build):
            shutil.rmtree(test_build)

    def test_write_complete_markdown(self):
        # Given the user wants to write the CV as markdown format
        inputdata = 'resources/markdown_complete.json'
        my_writer = OutputWriter()
        my_loader = InputLoader()
        json_data = my_loader.load_json(get_test_resources_path(inputdata))

        # When writing the markdown file
        generated_md = my_writer.generate_markdown_output(json_data)
        outputfile = os.path.join(
            get_test_build_dir(), 'test_write_complete_markdown.md')
        my_writer.save_outputfile(contents=generated_md, filepath=outputfile)

        # Then the contents of the markdown file is correct
        expected = load_file_contents(get_test_resources_path(
            'resources/expected/markdown.md'))
        actual = load_file_contents(outputfile)
        self.assertEqual(expected, actual)


class TestWriteHtml(unittest.TestCase):

    def tearDown(self):
        test_build = os.path.join(get_root_path(), 'build', 'testoutput')
        if os.path.exists(test_build) and os.path.isdir(test_build):
            shutil.rmtree(test_build)

    def test_write_complete_html(self):
        # Given the user wants to write the CV as HTML format
        inputdata = 'resources/markdown_complete.json'
        my_writer = OutputWriter()
        my_loader = InputLoader()
        json_data = my_loader.load_json(get_test_resources_path(inputdata))

        # When writing the html file
        generated_html = my_writer.generate_html_output(json_data)
        outputfile = os.path.join(get_test_build_dir(),
                                  'test_write_complete_html.html')
        my_writer.save_outputfile(contents=generated_html, filepath=outputfile)

        # Then the contents of the html file is correct
        expected = load_file_contents(get_test_resources_path(
            'resources/expected/html.html'))
        actual = load_file_contents(outputfile)
        self.assertEqual(expected, actual)
