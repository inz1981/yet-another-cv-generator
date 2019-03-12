#!/usr/bin/env python
import argparse
import os
from inout.loader import InputLoader
from inout.writer import OutputWriter


def arguments() -> argparse.Namespace:
    """
    Argument parser handling function
    :return: the argparse namespace
    """
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

    return parser.parse_args()


def generate(yargs: argparse.Namespace):
    """
    Generate all documents based on the input arguments
    :param yargs: argparse namespace
    :return: None
    """
    iol = InputLoader()
    input_data = iol.load_yaml(filepath=yargs.input_file)
    writedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    for docformat in yargs.docformat:
        print("generate {}".format(docformat))
        iow = OutputWriter(filetype=docformat)
        iow.generate_output(input_json=input_data)
        wrote = iow.save_outputfile(filepath=writedir)
        print("Wrote document: {}".format(wrote))


if __name__ == '__main__':
    args = arguments()
    generate(args)
