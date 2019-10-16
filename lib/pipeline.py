import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
   
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def execute(self, input_data):
        for step in self.steps:
            logger.info('hee')
            if step.cached():
                input_data = step.fetch_cache()
            else:
                input_data = step.execute(input_data)
                step.cache()
