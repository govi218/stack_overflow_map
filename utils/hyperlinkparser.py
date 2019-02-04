from html.parser import HTMLParser

class HyperlinkParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
    
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                    self.links.append(value)
    
    def print_links(self):
        print(self.links)