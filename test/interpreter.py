import sys
sys.path.append('../lib')

import logging
import interpreter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

code = interpreter.Code(logger)
code.add_line('a b')
code.add_line('a = 1')
code.add_line('b = 2')
code.add_line('def abc()')
code.add_line('a')

print code.get()
