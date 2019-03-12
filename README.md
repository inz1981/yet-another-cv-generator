#  yet-another-resume-generator (Yarg!) <img src="img/yarg.png" alt="Yarg!" width="50" height="50">

[![build status](
  http://img.shields.io/travis/inz1981/yet-another-resume-generator/master.svg?style=flat)](
 https://travis-ci.org/inz1981/yet-another-resume-generator)
[![coverage status](
  https://codecov.io/gh/inz1981/yet-another-resume-generator/branch/master/graph/badge.svg)](
 https://codecov.io/gh/inz1981/yet-another-resume-generator)


Yarg! is `Yet another resume generator` that creates your CV based on structured input data.

### Requirements

Python3 and pip installed

    python3 -m venv .venv
    . ./venv/bin/activate
    pip install -r requirements.txt

#### Usage

    $ ./src/yarg.py -h
    usage: yarg.py [-h] [-d {markdown,html} [{markdown,html} ...]] -f INPUT_FILE
                   [-o OUTPUT_DIR]

    Yarg! is Yet another resume generator that creates your CV based on structured
    input data.

    optional arguments:
      -h, --help            show this help message and exit
      -d {markdown,html} [{markdown,html} ...], --docformat {markdown,html} [{markdown,html} ...]
                            the document format, one of ['markdown', 'html']
      -f INPUT_FILE, --file INPUT_FILE
                            the input YAML file to read from
      -o OUTPUT_DIR, --outdir OUTPUT_DIR
                            the output dir to write documents, default current
                            working directory



The input is a YAML file with the resumé information. An example is in
`examples/yarg.yaml`

To generate HTML and Markdown documents of the input:

    $ ./src/yarg.py -d markdown html -f examples/yarg.yaml -o build/
