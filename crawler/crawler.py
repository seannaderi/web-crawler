from urllib.request import urlopen
from bs4 import BeautifulSoup 

#generates soup object from a given url
def generate_soup(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def main():
    url = 'http://www.google.com/'
    soup = generate_soup(url)
    print(soup.prettify())


if __name__ == '__main__':
    main()
