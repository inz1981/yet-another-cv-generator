#!/usr/bin/env python
import argparse
import logging
import os
import sys
from inout.loader import InputLoader
from inout.writer import OutputWriter
from helpers.logger import setup_logging


def arguments(args) -> argparse:
    """
    Argument parser handling function
    :return: the argparse
    """
    cwd = os.getcwd()
    io = OutputWriter()
    parser = argparse.ArgumentParser(
        description='Yarg! is Yet another resume generator that creates your '
                    'CV based on structured input data.')
    parser.add_argument(
        '-d', '--docformat', nargs='+',
        help='the document format, one of {}'.format(
            io.supported_filetypes),
        dest='docformat', default='html', choices=io.supported_filetypes)
    parser.add_argument('-f', '--file', dest='input_file', required=True,
                        help='the input YAML file to read from')
    parser.add_argument(
        '-o', '--outdir', dest='output_dir', required=False,
        help='the output dir to write documents, default current working '
             'directory', default=cwd)

    return parser.parse_args(args)


def generate(yargs: argparse):
    """
    Generate all documents based on the input arguments
    :param yargs: argparse
    :return: None
    """
    logger = logging.getLogger(__name__)
    iol = InputLoader()
    input_data = iol.load_yaml(filepath=yargs.input_file)

    for docformat in yargs.docformat:
        logger.info("generate %s", docformat)
        iow = OutputWriter(filetype=docformat)
        iow.generate_output(input_json=input_data)
        wrote = iow.save_outputfile(filepath=yargs.output_dir)
        logger.info("Wrote document: %s", wrote)


def main(args):
    generate(arguments(args))


if __name__ == '__main__':
    setup_logging()
    main(sys.argv[1:])
