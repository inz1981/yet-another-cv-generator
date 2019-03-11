#!/usr/bin/env python
import os
import sys


def get_root_path():
    return os.path.abspath(os.path.join(os.path.dirname(
        __file__), '..', '..'))


def add_src_path():
    srcpath = os.path.abspath(os.path.join(os.path.dirname(
        __file__), '..', '..', 'src'))
    if srcpath not in sys.path:
        sys.path.append(srcpath)


def get_test_resources_path(path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', path))


def load_file_contents(filepath):
    with open(filepath) as contents:
        return contents.read()


def get_test_build_dir():
    build = os.path.join(get_root_path(), 'build', 'testoutput')
    if not os.path.exists(build):
        os.makedirs(build)
    return build

add_src_path()
