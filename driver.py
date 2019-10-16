import sys
import pdb
import json
import os

from lib import pipeline
from lib import page
from lib import snippet
from lib import section
from lib import decorator

if len(sys.argv) == 0:
    sys.exit(1)

config = pipeline.Config()
config.input_file_path = sys.argv[1]
config.sections_json_path = '/tmp/sections.json'
config.pages_json_path = '/tmp/pages.json'
config.snippets_json_path = '/tmp/snippets.json'
config.processed_input_path = '/tmp/output.html'

pipeline = pipeline.Pipe()

parser = page.Parser(config)
pipeline.add_step(parser)

parser = section.Parser(config)
pipeline.add_step(parser)

parser = snippet.Parser(config)
pipeline.add_step(parser)

parser = decorator.Parser(config)
pipeline.add_step(parser)

pipeline.execute('Section \d*?\.\d*?:')
