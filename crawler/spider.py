from collections import deque
from crawler.helpers import *
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
        to_visit = self.perform_filtering(html_page)
        for link in to_visit:
            if link not in self.remaining_links:
                self.remaining_links.append(link)

    def perform_filtering(self, html_page):
        to_visit = set()
        # add links to to_visit if they satisfy these criteria
        # 1 - must be http or https
        http = [link for link in html_page.html_links if is_http(link)]
        # 2 - must be same domain
        same_domain = [link for link in http if is_same_domain(html_page.domain, link)]
        # 3 - must not be in urls_visited
        not_yet_visited = filter_visited_urls(self.urls_visited, same_domain) 
        to_visit = set(not_yet_visited)
        return to_visit

def main():
    return

if __name__ == '__main__':
   main() 

