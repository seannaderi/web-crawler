import unittest
import os
import sys
from crawler.html_page import HTML_page 

class html_page_tests(unittest.TestCase):
    
    # Makes html_page class with four_links.html for testing
    def setUp(self):
        current_dir = os.path.dirname(__file__)
        filename = os.path.join(current_dir, 'mocks/four_links.html') 
        with open(filename, 'r') as myfile:
            self.html_string = myfile.read().replace('\n', '')
        self.test_html_page = HTML_page(self.html_string)

    def tearDown(self):
        return
    
    def test_html_class_is_created(self):
        self.assertTrue(self.test_html_page is not None)

    def test_html_class_parses_links(self):
        self.assertTrue('/third_link.html' in self.test_html_page.html_links)
    
    def test_html_class_parses_scripts(self):
        self.assertTrue('/first_link.js' in self.test_html_page.static_assets['scripts'])
       
    def test_html_class_parses_css(self):
        self.assertTrue('/second_link.css' in self.test_html_page.static_assets['css'])

    def test_html_class_parses_imgs(self):
        self.assertTrue('/fourth_link.jpg' in self.test_html_page.static_assets['img'])

    def test_html_class_correctly_splits_static_assets(self):
        self.assertFalse('/fourth_link.jpg' in self.test_html_page.static_assets['scripts'])
        self.assertFalse('/second_link.css' in self.test_html_page.static_assets['img'])
        self.assertFalse('/first_link.js' in self.test_html_page.static_assets['css'])
 
if __name__ == '__main__':
    unittest.main()
