import os

class Config():
    def __init__(self):
        self.file_path = ''

class Step():
    def __init__(self, obj):
        self.obj = obj

    def execute(input_data):
        self.obj.execute(input_data) 

    def fetch_cache(self):
        return self.obj.fetch_cache() 

    def is_cached(self):
        return self.obj.is_cached()

    def cache(self):
        return self.obj.cache()

class Pipe():
   
    def __init__(self, logging):
        self.steps = []
        self.logger = logging.getLogger(os.path.basename(__file__))

    def add_step(self, step):
        self.steps.append(step)

    def execute(self, input_data):
        for step in self.steps:
            if step.cached():
                self.logger.info("Fetching cached data for %s" % step.__class__)
                input_data = step.fetch_cache()
            else:
                self.logger.info("Executing %s" % step.__class__)
                input_data = step.execute(input_data)
                step.cache()
