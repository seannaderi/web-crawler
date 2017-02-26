from urllib.request import urlopen
from urllib.parse import urlparse, urljoin, urlsplit

def get_html_as_string(url):
    return urlopen(url).read()

# Current_html_page_url should contain scheme as well as domain and potentially path 
# html_links must be an iterable
def normalise_html_links(current_html_page_url, html_links):
    normalised_links = set()
    for link in html_links:
        normalised_links.add(urljoin(current_html_page_url, link)) 
    return normalised_links

# Returns only the urls we should visit
def filter_visited_urls(visited_urls, current_urls):
    return [url for url in current_urls if url not in visited_urls]

# Must supply leading '//' with current domain for netloc to be
# correctly recognised
def is_same_domain(domain, current_url):
    parsed = urlparse(current_url)
    current_domain = '{uri.netloc}'.format(uri=parsed)
    return domain == current_domain 

# Returns true if the url uses http or https
def is_http(url):
    scheme = urlparse(url)[0]
    return scheme == 'http' or scheme == 'https' or scheme == ''

def remove_query_params(url):
    return urljoin(url, urlparse(url).path)

def main():
    domain = 'www.google.com'
    test_url = 'www.different_domain.com'
    print(is_same_domain(domain, test_url))
#    print(normalise_html_links('https://www.google.com/why/why/why', ['https://www.what.com/'

if __name__ == '__main__':
    main()



