import sys
import pdb
sys.path.append('../../lib')

import logging
import interpreter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

code = interpreter.Code(logger)
code.add_line('a b', '5px')
code.add_line('a = 1', '5px')
code.add_line('b = 2', '5px')
code.add_line('def abc():', '5px')
code.add_line('"""', '10px')
code.add_line('comment', '10px')
code.add_line('comment', '10px')
code.add_line('comment', '10px')
code.add_line('comment', '10px')
code.add_line('"""', '10px')
code.add_line('a = 1', '10px')
code.add_line('abc a', '10px')
code.add_line('abc b', '10px')
code.add_line('abc c', '10px')
code.add_line('abc d', '10px')
code.add_line('abc e', '10px')

