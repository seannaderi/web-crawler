"""
This file will contains all of the functions that perform the traversal of the
domain
"""
from collections import deque

#the main crawling function, performing the BFS through the sites links
def crawl(url, links = None):
    if links = None:
        links = deque()
    #perform BFS passing around the queue
