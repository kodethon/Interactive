import bs4
import re
import pdb
import os
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Task():
    def __init__(self, config, logging, html):
        self.html = html 
        self.logger = logging.getLogger(os.path.basename(__file__))
        self.config = config
        self.pages_json_path = config.pages_json_path
    
    def with_input_path(self, input_path):
        with open(input_path) as f:
            self.soup = bs4.BeautifulSoup(f, 'html.parser')

        with open(input_path) as f:
            self.file_contents = f.read()

    def is_page_start(self, line):
        match = re.search('overflow:hidden', line)
        if not match: return False
        return True

    def build_pages(self, line, line_num):
        if self.is_page_start(line):
            self.Pages.append({
                'line_number' : line_num,
                'offset_top' : self.html.get_css_property_value(line, 'top'),
                'offset_left' : self.html.get_css_property_value(line, 'left')
            })       
    
    def execute(self, input_data = None):
        self.Pages = []

        line_num = -1
        lines = self.file_contents.split("\n")
        for line in lines:
            line_num += 1

            self.buildPages(line, line_num)

        return self.Pages

    def fetch_cache(self):
        with open(self.pages_json_path, 'r') as f:
            contents = f.read()
            return json.loads(contents)

    def cached(self):
        return os.path.exists(self.pages_json_path)

    def cache(self):
        if not os.path.exists(pages_json_path):
            with open(self.pages_json_path, 'r') as f:
                f.write(json.dumps(self.Pages))
                return True
        return False
            
