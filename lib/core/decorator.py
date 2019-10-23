import os
import pdb
import json
import bs4

class Task():
    
    def __init__(self, config, logging, html):
        self.html = html
        self.config = config
        self.logger = logging.getLogger(os.path.basename(__file__))
        self.processed_input_path = config.processed_input_path

        with open(config.input_file_path) as f:
            self.soup = bs4.BeautifulSoup(f, 'html.parser')

        with open(config.input_file_path) as f:
            self.file_contents = f.read()

        with open(config.pages_json_path) as f:
            data = f.read()
            self.pages = json.loads(data)

        self.buttons = ''

    def add_button(self, snippet):
        style = snippet['style']
        code = snippet['code']
        page = self.find_page(snippet['start_line'])

        button = self.soup.new_tag('button') 
        button.string = 'Run'
        button.attrs['style'] = self.create_style(page, style)

        self.buttons += unicode(button)

    def create_style(self, page, style):
        top = self.html.get_css_property_value('top', style)
        top_abs = float(top.replace('px', ''))
        top_rel = float(page['offset_top'].replace('px', ''))
        style = style.replace(top, "top:%spx" %  str(top_abs + top_rel))

        left = self.html.get_css_property_value('left', style)
        left_abs = float(left.replace('px', ''))
        left_rel = float(page['offset_left'].replace('px', ''))
        style = style.replace(left, "top:%spx" %  str(left_abs + left_rel))

        return style

    def find_page(self, line_number):
        length = len(self.pages) - 1
        i = 0
        j = length
        while i <= j:
            index = int((i + j) / 2)
            
            page = self.pages[index]
            cur_line_number = page['line_number']

            if line_number < cur_line_number:
                if index == 0: return page

                prev_page = self.pages[index - 1]
                if line_number >= prev_page['line_number']:
                    return prev_page

                j = index - 1
            else:
                if index == length: return page

                next_page = self.pages[index + 1]
                if line_number <= next_page['line_number']:
                    return page

                i = index + 1
             

    def execute(self, snippets):
        for snippet in snippets:
            self.add_button(snippet)

    def fetch_cache(self):
        with open(self.processed_input_path, 'r') as f:
            return f.read()

    def cached(self):
        return os.path.exists(self.processed_input_path)

    def cache(self):
        if not os.path.exists(self.processed_input_path):
            with open(self.processed_input_path, 'w') as f:
                f.write(self.file_contents + self.buttons)
                return True
        return False
