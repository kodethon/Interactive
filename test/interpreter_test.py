import sys
import pdb
sys.path.append('../lib')

import logging
import interpreter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

code = interpreter.Code(logger)
code.add_line('a b', '5px')
code.add_line('a = 1', '5px')
code.add_line('b = 2', '10px')
code.add_line('def abc():', '5px')
code.add_line('a', '20px')

print code.get()
