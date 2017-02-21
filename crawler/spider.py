from collections import deque
from crawler.helpers import get_html_as_string, filter_visited_urls
from crawler.html_page import HTML_page

# To hold all of the html_page instances that we get from the traversal
class spiders_web:
    
    # urls_visited and html_pages parameters used for testing purposes
    def __init__(self, base_html_page, urls_visited, html_pages = None):
        self.base_html_page = base_html_page 
        # A set that tracks every url that we have visited to avoid looping
        self.urls_visited = urls_visited
        self.remaining_links = deque()
        if html_pages:
            self.html_pages = html_pages
        else:
            self.html_pages = set([base_html_page])

    def loop(self, max_iterations = None):
        while len(self.remaining_links) is not 0:
            current_link = remaining_links.popleft()
            html_string = get_html_as_string(current_link)
            current_html_page = HTML_page(html_string)
            self.urls_visited.add(current_link)
            self.html_pages.add(current_html_page)
            crawl(current_html_page)

    # Can perform testing on the crawl function without needing to request
    # html from a live site
    def crawl(self, html_page):
        to_visit = filter_visited_urls(self.urls_visited, html_page.html_links)
        for link in to_visit:
            self.remaining_links.append(link)

    '''
    To go in the crawl function:
    we need to normalise urls at some stage, when is this?
    do a check to make sure we arent leaving the domain
    do a check to make sure the request is http or https

    All of this stuff can be tested if it's put in the crawl function
    '''

def main():
    return

if __name__ == '__main__':
   main() 

