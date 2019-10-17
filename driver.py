import sys
import pdb
import json
import os
import logging

from lib.util import html

from lib import pipeline
from lib.core import page
from lib.core import snippet
from lib.core import section
from lib.core import decorator

if len(sys.argv) == 0:
    sys.exit(1)

logging.basicConfig(level=logging.INFO)

config = pipeline.Config()
config.input_file_path = sys.argv[1]
config.sections_json_path = '/tmp/sections.json'
config.pages_json_path = '/tmp/pages.json'
config.snippets_json_path = '/tmp/snippets.json'
config.processed_input_path = '/tmp/output.html'

pipeline = pipeline.Pipe(logging)

task = page.Task(config, logging, html)
pipeline.add_step(task)
'''
task = section.Task(config, logging)
pipeline.add_step(task)

task = snippet.Task(config, logging, html)
pipeline.add_step(task)

task = decorator.Task(config, logging, html)
pipeline.add_step(task)
'''
pipeline.execute('Section \d*?\.\d*?:')
