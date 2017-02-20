#from urllib.parse import urljoin
from urllib.request import urlopen

def get_html_as_string(url):
    return urlopen(url).read()

# Performs normalisation of every url before we continue the traversal
# This ensures that we know if we have visited this url before
def normalise_html_links(html_links):
    return 

# Returns only the urls we should visit
def filter_visited_urls(visited_urls, current_urls):
    return [url for url in current_urls if url not in visited_urls]
    

