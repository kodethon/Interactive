import subprocess
import pdb

class Code():

    def __init__(self, logger):
        self.interpreter = 'python'
        self.logger = logger
        self.code = ''

    def get(self):
        return self.code

    def add_line(self, line):
        path = '/tmp/foo.py'
        with open(path, 'w') as f:
            f.write(line)
        
        command = "timeout 10s %s %s" % (self.interpreter, path)
        self.logger.debug('Running command: %s' % command)
        results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stderr = results.stderr.read()
        pdb.set_trace()

        if 'NameError:' in stderr: return False
        if 'SyntaxError:' in stderr: return False
        
        self.code = "%s\n%s" % (self.code, line)
        return True

