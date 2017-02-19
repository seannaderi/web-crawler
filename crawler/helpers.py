#from urllib.parse import urljoin
from urllib.request import urlopen

def get_html_as_string(url):
    return urlopen(url).read()

# Performs normalisation of every url before we continue the traversal
# This ensures that we know if we have visited this url before
def normalise_url(base_url, url):
    return 


# makes sure that the link is absolute and not a relative link
# def make_link_absolute(link):
#     base = 'http://google.com'
#     full = urljoin(base, link)
#     return full

