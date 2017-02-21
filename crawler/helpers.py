from urllib.request import urlopen
from urllib.parse import urlparse, urljoin, urlsplit

def get_html_as_string(url):
    return urlopen(url).read()

# Performs normalisation of every url before we continue the traversal
# This ensures that we know if we have visited this url before
def normalise_html_links(html_links):
    return 

# Returns only the urls we should visit
def filter_visited_urls(visited_urls, current_urls):
    return [url for url in current_urls if url not in visited_urls]

# Must supply leading '//' with current domain for netloc to be
# correctly recognised
def is_same_domain(domain, current_url):
    parsed = urlparse(current_url)
    current_domain = '{uri.netloc}'.format(uri=parsed)
    print(current_domain)
    return domain == current_domain 

# Returns true if the url uses http or https
def is_http(url):
    return urlparse(url)[0] == 'http' or urlparse(url)[0] == 'https'

def main():
    domain = 'www.google.com'
    current_domain = '//www.google.com'
    test_url = 'httxp://www.google.com/'
    print(is_same_domain(domain, current_domain))

if __name__ == '__main__':
    main()



