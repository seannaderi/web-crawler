from urllib.request import urlopen
from bs4 import BeautifulSoup

class html_page:

    # page takes a url, and creates an html_page containing the static
    # assets and all of the links that can be follwed from that page
    # in seperate sets
    def __init__(self, url):
        self.url = url
        self.soup = self.generate_soup(url) 
        # dict structure for static assets:
        #
        # { 'scripts' : set()
        #   'css' : set()
        #   'img' : set() }
        #
        self.static_assets = {}
        self.populate_static_assets()
        self.html_links = set()
        self.populate_html_links
    
    # generates soup object from a given url, setting the classes soup 
    # variable
    def generate_soup(self, url):
        html = urlopen(url).read()
        return BeautifulSoup(html, 'html.parser')

    # extracts all of the links from the classes soup object, populating the 
    # links set
    def populate_html_links(self):
       # extremely unreadable, but im a sucker for one liners
       self.html_links = set([link.get('href') for link in self.soup.find_all('a')])

    # gets all of the static assets from the page. These are defined
    # as follows:
    #
    # 1 - <script src = 'ONE.js'></script>
    # 2 - <link rel = 'stylesheet' href = 'TWO.css'>
    # 3 - <img src = 'THREE.jpg'>
    #
    def populate_static_assets(self):
        self.static_assets['scripts'] = set([link.get('src') for link in self.soup.find_all('script')])
        self.static_assets['css'] = set([link.get('href') for link in self.soup.find_all('link') \
                                                          if 'stylesheet' in link.get('rel')])
        self.static_assets['img'] = set([link.get('src') for link in self.soup.find_all('img')]) 

def main():
    url = 'http://bbc.co.uk/news/'
    my_html_page = html_page(url)
    print(my_html_page)
    # print(my_html_page.html_links)
    # print(my_html_page.soup.prettify())


if __name__ == '__main__':
    main()
