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
        self.sections_json_path = config.sections_json_path

        with open(config.input_file_path) as f:
            self.soup = bs4.BeautifulSoup(f, 'html.parser')

        with open(config.input_file_path) as f:
            self.file_contents = f.read()

    def build_section_titles(self, pattern, line, section_title):
        # If the key already exists in the table, keep it's relative order
        key = re.findall(pattern, line)[0]
        if key in self.PositionTable:
            position = self.PositionTable[key]
            self.SectionTitles[position] = section_title
        else:
            self.SectionTitles.append(section_title) 
            self.PositionTable[key] = len(self.SectionTitles)

    def build_section_starts(self, section_title, line_num):
        self.SectionStarts[section_title] = line_num
        pass

    def build_sections(self):
        sections = []
        length = len(self.SectionTitles)
        for i in xrange(0, length):
            section_title = self.SectionTitles[i]
            start_line = self.SectionStarts[section_title]

            if i < length - 1: 
                end_line = self.SectionStarts[self.SectionTitles[i + 1]]
            else:
                end_line = len(lines)

            sections.append({
                'title' : section_title,
                'start_line' : start_line,
                'end_line' : end_line
            })
        return sections
    
    def execute(self, pattern):
        self.SectionTitles = [] # List of sections in order
        self.PositionTable = {} # Position of each section in self.SectionTitles
        self.SectionStarts = {}

        line_num = -1
        lines = self.file_contents.split("\n")
        for line in lines:
            line_num += 1

            self.buildPages(line, line_num)

            match = re.search(pattern, line)
            if not match: continue 

            # Determine the section title
            soup = bs4.BeautifulSoup(match.string, 'html.parser')
            section_title = soup.text.strip()

            self.build_section_titles(pattern, line, section_title)
            self.build_section_starts(section_title, line_num) 

        return self.build_sections() 

    def fetch_cache(self):
        with open(self.sections_json_path, 'r') as f:
            contents = f.read()
            return json.loads(contents)

    def cached(self):
        return os.path.exists(self.sections_json_path)
    
    def cache(self):
        if not os.path.exists(self.sections_json_path):
            with open(self.sections_json_path, 'w') as f:
                f.write(json.dumps(self.build_sections()))
                return True
        return False
