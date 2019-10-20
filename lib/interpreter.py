import subprocess
import pdb
import ast

class Code():

    def __init__(self, logger):
        self.interpreter = 'python'
        self.logger = logger

        self.indent_to_tabs = {}
        self.lines = []

    def get(self):
        return "\n".join(self.lines)

    def is_valid_line(self, line):
        try:
            ast.parse(line)
        except SyntaxError as e:
            return not 'invalid syntax' in e

        results = self.run_code(line)
        stderr = results.stderr.read()

        if 'NameError:' in stderr: return False
        if 'SyntaxError:' in stderr: return False

        return True

    def run_code(self, code):
        path = '/tmp/foo.py'
        with open(path, 'w') as f:
            f.write(code)
        
        command = "timeout 10s %s %s" % (self.interpreter, path)
        self.logger.debug('Running command: %s' % command)
        return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)       

    def get_indent_to_tabs(self, indent):
        indent = float(indent.replace('px', ''))
        return self.indent_to_tabs[indent]

    def register_indent(self, indent):
        indent = float(indent.replace('px', ''))
        if indent not in self.indent_to_tabs:
            self.indent_to_tabs[indent] = len(self.indent_to_tabs)

    def add_line(self, line, indent):
        if not self.is_valid_line(line): return False 
        
        self.register_indent(indent)
        self.lines.append("\t" * self.get_indent_to_tabs(indent) + line)

        return True

