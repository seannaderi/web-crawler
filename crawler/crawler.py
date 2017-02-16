from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import deque

#generates soup object from a given url
def generate_soup(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

#extracts all of the links from a soup object, returns a set
def get_links(soup):
    links = set()
    for link in soup.find_all('a'):
        links.add(link.get('href'))
    return links

#the main crawling function, performing the BFS through the sites links
def crawl(url, links = None):
    if links = None:
        links = deque()
    #perform BFS passing around the queue


def main():
    url = 'http://bbc.co.uk/news/'
    soup = generate_soup(url)
    links = get_links(soup)
    print(links)


"""
main flow of work...

1) take url from user, create initial soup object
2) get all the links from the soup, including any static objects, defined by ()
3) add each link to the back of the queue
4) for each link, get the soup, and repeat steps 2-3 until the queue is empty

We will perfrom BFS, always following the links at the front of the queue and appending
new links to the back of the queue
"""


if __name__ == '__main__':
    main()
