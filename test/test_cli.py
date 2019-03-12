#!/usr/bin/env python
import datetime
import os
import unittest
import utils
from yarg import main as yarg


class TestReadInput(unittest.TestCase):

    def test_generate_all_documents(self):
        # Given the user wants to generate all documents from cli
        args = [
            '-d', 'markdown', 'html',
            '-f', utils.get_test_resources_path('input_complete.json'),
            '-o', os.path.join(utils.get_test_build_dir())
        ]

        # When Yarg is executed and generating documents
        yarg(args=args)

        # Then the content is correct in the documents
        expected_html = utils.load_file_contents(
            utils.get_test_resources_path('expected/html.html'))
        expected_html = expected_html.replace(
            "{{ today() }}", datetime.datetime.today().date().strftime(
                "%Y-%m-%d"))
        expected_markdown = utils.load_file_contents(
            utils.get_test_resources_path('expected/markdown.md'))
        actual_html = utils.load_file_contents(os.path.join(
            utils.get_test_build_dir(), 'html.html'))
        actual_markdown = utils.load_file_contents(os.path.join(
            utils.get_test_build_dir(), 'markdown.md'))
        self.assertEqual(expected_html, actual_html)
        self.assertEqual(expected_markdown, actual_markdown)
