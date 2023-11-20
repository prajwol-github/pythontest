#Goto github.com/prajwol-github/pythontest for more details regarding the code.

from html.parser import HTMLParser
import webbrowser
class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href': self.links.append(attr[1])

html_file_path = input("Enter path to HTML file: ")
# To read HTML File
try:
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
except FileNotFoundError:
    print("File not found. Please provide a valid HTML file path.")
    exit()
    
# Create a parser and feed it the HTML content
parser = LinkParser()
parser.feed(html_content) 


# Open the links in the default web browser
for link in parser.links:
    webbrowser.open(link, new=2) # Open link in the default browser


#Code by PS
