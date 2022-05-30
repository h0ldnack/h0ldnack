import json
import os
from bs4 import BeautifulSoup as BS
import pathlib
import typing as T
from rich.pretty import pprint
import glob

def extract_data_better(html_file: str):
    assert os.path.isfile(html_file)
    headers = ["h2", "h3", "h4", "h5", "h5"]
    with open(html_file) as f:
        html_data = BS(f, 'lxml')
        title = html_data.title.get_text()
        if title == '':
            # Uses the first h1 tag if title is empty
            title = html_data.find("h1").get_text()

        # Extract code blocks
        code_blocks = list(map(lambda x: x.get_text().strip(), html_data.find_all("code")))

        # Extract links
        # TODO: Could make this smarter if I keep all "real" links in a reference section, like wikipedia
        # Inline links just point to the reference
        # Would allow for easily creating an index of all external links on my site
        def a(link: str):
            href = link["href"]
            t = link.get_text()
            return (t, href)
            
        links = list(map(a, html_data.find_all("a")))
        
        for script in html_data(["script", "style", "code"] + headers):
            script.extract()

        t = html_data.body.get_text()
        lines = t.split("\n")
        slines = list(map(lambda x: x.strip(), lines))
        body = [line for line in slines if line.strip()]
            
    result = {"title": title, "body": body, "code": code_blocks, "links": links}
    return result 
            
def extract_data(html_file: str):
    assert os.path.isfile(html_file)
    with open(html_file) as f:
        html_data = BS(f, 'lxml')
        title = html_data.title.get_text()
        for script in html_data(["script", "style"]):
            script.extract()
        t = html_data.body.get_text()
        lines = t.split("\n")
        slines = list(map(lambda x: x.strip(), lines))
        clines = [line for line in slines if line.strip()]
        
    result = {"title": title, "body": clines}
    return result 
            
def main():
    
    html_files = glob.glob('./**/*.html', recursive=True)
    html_paths = list(map(lambda x: x[2:], html_files))
    html_datas = list(map(extract_data_better, html_files))
    pprint(html_datas)
    
if __name__ == "__main__":
    main()
