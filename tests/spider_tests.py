import unittest
import os
import sys
from crawler.html_page import HTML_page
from crawler.spider import spiders_web 

class spider_tests(unittest.TestCase):

    def setUp(self):
        current_dir = os.path.dirname(__file__)
        filename = os.path.join(current_dir, 'mocks/spider_test.html')
        with open(filename, 'r') as myfile:
            self.html_string = myfile.read().replace('\n', '')
        self.test_base_html_page = HTML_page(self.html_string)
        self.test_urls_visited = set()
        self.test_spiders_web = spiders_web(self.test_base_html_page, self.test_urls_visited)
 
    def tearDown(self):
        return
    
    def test_crawl_wont_revisit_urls(self):
        links = ['/first_link.html', '/second_link.html', '/third_link.html',
                '/fourth_link.html']
        for link in links:
            self.test_spiders_web.urls_visited.add(link)
        self.test_spiders_web.crawl(self.test_base_html_page)
        self.assertTrue(len(self.test_spiders_web.remaining_links) == 0)
        
if __name__ == '__main__':
    unittest.main()

