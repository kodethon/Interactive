import sys
import pdb
sys.path.append('../../lib')

import logging
import interpreter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def count_whitespace(line):
    return line.count('    ')
    count = 0
    for c in line:
        if c != ' ':
            break
        count += 1
    return count

code = interpreter.Code(logger)
with open('../../lib/core/section.py', 'r') as f:
    contents = f.read()
    lines = contents.split("\n")
    for line in lines:
        if not code.add_line(line.strip(), "%spx" % count_whitespace(line)):
            pass
    print code.get()

