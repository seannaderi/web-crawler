"""
This file will contains all of the functions that perform the traversal of the
domain
"""
from collections import deque
from helpers import get_html_as_string
from html_page import HTML_page

# To hold all of the html_page instances that we get from the traversal
class spiders_web:

    def __init__(self, base_url):
        self.base_url = base_url
        # Tracks every url that we have visited to avoid looping
        self.urls_visited = set()
        self.urls_visited.add(base_url)
        self.html_pages = []

    def crawl(url, links = None):
        if links == None:
            links = deque()
            links.append(normalise_html_links(url))

        while len(links) is not 0:
            current_url = links.popleft()
            current_html_page = HTML_page(get_html_as_string(url))
            # if this has been successful, then we can say that we visited this url
            self.urls_visited.add(url)
            # normalise the links for the current html_page
            normalise_html_links(current_html_page.html_links) 
            self.html_pages.append(current_html_page)
            for link in current_html_page.html_links:
                if link not in urls_visited:
                    links.append(link)
                    urls_visited.append(link)

def main():
    return

if __name__ == '__main__':
   main() 

