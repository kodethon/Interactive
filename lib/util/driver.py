import logging
import compiler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

code = compiler.Code(logger)
code.add_line('a = 1')
code.add_line('b = 2')
code.add_line('def abc()')

print code.get()
