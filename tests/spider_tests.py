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
        self.test_base_html_page = HTML_page('www.test.com', self.html_string)
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

    def test_crawl_adds_all_links_not_visited(self):
        links = ['/second_link.html', '/fourth_link.html']
        for link in links:
            self.test_spiders_web.urls_visited.add(link)
        self.test_spiders_web.crawl(self.test_base_html_page)
        self.assertTrue('/first_link.html' in self.test_spiders_web.remaining_links)
        self.assertTrue('/third_link.html' in self.test_spiders_web.remaining_links)

    def test_crawl_doesnt_visit_different_domain(self):
        pass

    def test_crawl_only_visits_http(self):
        pass
        
if __name__ == '__main__':
    unittest.main()

