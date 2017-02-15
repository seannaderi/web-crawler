from urllib.request import urlopen
from bs4 import BeautifulSoup 

url = 'http://www.google.com/'

html_stuff = urlopen(url).read()

soup = BeautifulSoup(html_stuff, 'html.parser')

print(soup.prettify())
