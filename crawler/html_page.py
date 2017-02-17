from urllib.request import urlopen
from bs4 import BeautifulSoup

class html_page:

    # page takes a url, and creates an html_page containing the static
    # assets and all of the links that can be follwed from that page
    # in seperate sets
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.static_assets = set()
        self.html_links = set()
    
    # generates soup object from a given url, setting the classes soup 
    # variable
    def generate_soup(url):
        html = urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        self.soup = soup

    # extracts all of the links from the classes soup object, populating the 
    # links set
    def populate_links(soup = self.soup):
       # for link in soup.find_all('a'):
       #     self.links.add(clean_up_link((link.get('href'))))
       # extremely unreadable, but im a sucker for one liners
       self.links.update([clean_up_link(link.get('href')) for link in soup.find_all('a')])

    # cleans up the link before adding it to the classes link set
    # clean up includes removing any queries, being consistent 
    # with relative and absolute urls
    def clean_up_link(link):
        return link 

    # gets all of the static assets from the page. These are defined
    # as follows:
    #
    # 1 - <script src = 'ONE.js'></script>
    # 2 - <link rel = 'stylesheet' href = 'TWO.css'>
    # 3 - <img src = 'THREE.jpg'>
    #
    def populate_static_assets(soup):
        return 

#def main():
#    url = 'http://bbc.co.uk/news/'
#    soup = generate_soup(url)
#    links = get_links(soup)
#    print(links)

