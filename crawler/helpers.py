#from urllib.parse import urljoin
from urllib.request import urlopen

def get_html_as_string(url):
    return urlopen(url).read()

# makes sure that the link is absolute and not a relative link
# def make_link_absolute(link):
#     base = 'http://google.com'
#     full = urljoin(base, link)
#     return full

#def main():
#    link = '/whatever.fuckwit'
#    print(make_link_absolute(link)
#
#if __name__ == '__main__':
#    main()
