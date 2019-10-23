import bs4
import pdb

def get_css_property_value(prop, line):
    try:
        soup = bs4.BeautifulSoup(line, 'html.parser')
        style = soup.div.attrs['style']
    except Exception as e:
        style = line

    styles = style.split(';')
    for style in styles:
        toks = style.split(':')
        if toks[0] != prop: continue
        return toks[1]
