#!/usr/bin/env python
from jinja2 import FileSystemLoader, Environment
import os


class OutputWriter:

    def __init__(self, filetype='html'):
        self.supported_filetypes = ['markdown', 'html']
        self.templates_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', 'resources', 'templates'))
        self._filetype = filetype
        self.output_data = None
        self.contents = dict()

    @property
    def filetype(self) -> str:
        """
        Get the filetype to be generated
        :return: str: file type
        """
        return self._filetype

    @filetype.setter
    def filetype(self, filetype: str):
        """
        Set the filetype to be generated
        :param filetype: file type
        :return: str: file type
        """
        if filetype not in self.supported_filetypes:
            raise NotImplementedError(
                '({}) is not a supported file type, choose from {}'.format(
                    filetype, self.supported_filetypes))
        self._filetype = filetype

    def generate_output(self, input_json: dict) -> str:
        """
        Generates a html file of the input contents
        :param dict input_json: Input read into a dict
        :return: the contents of the generated file
        """
        import datetime

        def format_datetime(value: str, dateformat="%B %Y") -> str:
            """
            Help function used as filter for Jinja rendering, converting
            date into a string. e.g: 2018-01-02 -> 1 January 2018
            :param value: the date string, e.g. 2018-01-02
            :param dateformat: output date format
            :return: text representation of date, e.g. 1 January 2018
            """
            date = datetime.datetime.strptime(value, "%Y-%m-%d")
            return date.strftime(dateformat)

        def today():
            """
            Help function used as filter for Jinja rendering, getting the
            today's date
            :return: date, e.g. 2019-03-10
            """
            return datetime.datetime.today().date()

        file_loader = FileSystemLoader(os.path.join(
            self.templates_path, self.filetype))
        env = Environment(loader=file_loader)
        env.filters['datetime'] = format_datetime
        template = env.get_template('{}.jinja2'.format(self.filetype))
        template.globals['today'] = today

        self.contents = template.render(input=input_json)
        return self.contents

    def save_outputfile(self, filepath: str) -> str:
        """
        Save the contents as an appropriate file with file extension
        :param contents: the data content to write
        :param filepath: the path to write the file
        :return: the path to the file written
        """
        if not self.contents:
            raise ValueError("No output content available to write")
        if self.filetype == 'html':
            ext = '.html'
        elif self.filetype == 'markdown':
            ext = '.md'
        else:
            raise NotImplementedError(
                '({}) is not a supported file type, choose from {}'.format(
                    self.filetype, self.supported_filetypes))
        fwrite = os.path.join(filepath, "{}{}".format(self.filetype, ext))
        with open(fwrite, 'w') as filewrite:
            filewrite.write(self.contents)
        return fwrite
