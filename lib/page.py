import bs4
import re
import pdb
import os
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Parser():
    def __init__(self, config):
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

    def get_offset_top(self, line):
        soup = bs4.BeautifulSoup(line, 'html.parser')
        style = soup.div.attrs['style']
        styles = style.split(';')
        for style in styles:
            toks = style.split(':')
            if toks[0] != 'top': continue
            return toks[1]

    def build_pages(self, line, line_num):
        if self.is_page_start(line):
            self.Pages.append({
                'line_number' : line_num,
                'offset_top' : self.get_offset_top(line)
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
            
