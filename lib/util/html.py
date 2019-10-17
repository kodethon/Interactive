def get_css_property_value(self, prop, line):
    soup = bs4.BeautifulSoup(line, 'html.parser')
    style = soup.div.attrs['style']
    styles = style.split(';')
    for style in styles:
        toks = style.split(':')
        if toks[0] != prop: continue
        return toks[1]
