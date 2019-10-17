import bs4
import pdb
import os
import ast
import json

class Task():

    def __init__(self, config, logging, html):
        self.html = html 
        self.logger = logging.getLogger(os.path.basename(__file__))
        self.config = config
        self.snippets_json_path = config.snippets_json_path

        with open(config.input_file_path) as f:
            self.file_contents = f.read()

    def execute(self, sections):
        self.Snippets = []
        lines = self.file_contents.split("\n")

        for section in sections:
            snippet = ''
            indents = []
            for i in xrange(section['start_line'], section['end_line']):
                line = lines[i]
                element = bs4.BeautifulSoup(line, 'html.parser')
                text = element.text.strip()
                if len(text) == 0: continue 

                tmp = snippet + "\n" + text
                try:
                    ast.parse(tmp)
                except SyntaxError as e:
                    if len(snippet) > 0:
                        self.Snippets.append({
                            'style' : element.find('div').attrs['style'],
                            'start_line' : i,
                            'code' : snippet
                        })
                        snippet = ''
                        indents = []
                    continue

                indents.append(self.html.get_css_property_value('left', line))
                snippet = tmp
         
        return self.Snippets

    def fetch_cache(self):
        with open(self.snippets_json_path, 'r') as f:
            contents = f.read()
            return json.loads(contents)

    def cached(self):
        return os.path.exists(self.snippets_json_path)
    
    def cache(self):
        if not os.path.exists(self.snippets_json_path):
            with open(self.snippets_json_path, 'w') as f:
                f.write(json.dumps(self.Snippets))
                return True
        return False
