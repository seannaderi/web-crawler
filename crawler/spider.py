"""
This file will contains all of the functions that perform the traversal of the
domain
"""
from collections import deque
from helpers import *

# To hold all of the html_page instances that we get from the traversal
class spiders_web:

    def __init__(self, base_url):
        self.base_url = base_url
        # Tracks every url that we have visited to avoid looping
        self.urls = set()
        self.urls.add(base_url)
        self.html_pages = []

    # The entry point of the web traversal
    # The BFS works as standard, apart from before adding any url to the back 
    # of the queue, we first check that we havent seen it before in the urls
    # set, which tracks all visited urls
    def crawl(url, links = None):
        if links == None:
            links = deque()
        # perform BFS passing around the queue

def main():
    return

if __name__ == '__main__':
   main() 

