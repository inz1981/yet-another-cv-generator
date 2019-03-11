#!/usr/bin/env python
from jinja2 import FileSystemLoader, Environment
import os


class OutputWriter:

    def __init__(self):
        self.contents = dict()

    def generate_markdown_output(self, input_json: dict) -> dict:
        """
        Generates a markdown file of the input contents
        :param dict input_json: Input read into a dict
        :return: dict: the contents of the generated file
        """
        self.contents['filetype'] = "markdown"

        file_loader = FileSystemLoader(os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', 'templates', 'markdown')))
        env = Environment(loader=file_loader)

        template = env.get_template('markdown.jinja2')

        self.contents['contents'] = template.render(input=input_json)
        return self.contents

    def generate_html_output(self, input_json: dict) -> dict:
        """
        Generates a html file of the input contents
        :param dict input_json: Input read into a dict
        :return: dict: the contents of the generated file
        """
        self.contents['filetype'] = "html"

        def format_datetime(value: str, format="%B %Y") -> str:
            import datetime
            date = datetime.datetime.strptime(value, "%Y-%m-%d")
            return date.strftime(format)

        file_loader = FileSystemLoader(os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', 'templates', 'html')))
        env = Environment(loader=file_loader)
        env.filters['datetime'] = format_datetime
        template = env.get_template('html.html')

        self.contents['contents'] = template.render(input=input_json)
        return self.contents

    def save_outputfile(self, contents: dict, filepath: str):
        """
        Save the contents as an appropriate file with file extension
        :param contents: the data content to write
        :param filepath: the path to write the file
        :return:
        """
        with open(filepath, 'w') as filewrite:
            filewrite.write(contents['contents'])
