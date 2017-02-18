import unittest
import os
from crawler import html_page

class html_page_tests(unittest.TestCase):

    #set up for all of the soup test functions
    def setUp(self):
        current_dir = os.path.dirname(__file__)
        filename = os.path.join(current_dir, 'mocks/four_links.html') 
        with open(filename, 'r') as myfile:
            self.html_string = myfile.read().replace('\n', '')
        self.test_html_page = html_page.html_page(self.html_string)

    #tear down for all of the soup test functions
    def tearDown(self):
        return

    def test_html_class_parses_links(self):
        self.assertTrue('/third_link.html' in self.test_html_page.html_links)
    
    def test_html_class_parses_static_assets(self):
        self.assertTrue('/first_link.js' in self.test_html_page.static_assets['scripts'])
        self.assertTrue('/second_link.css' in self.test_html_page.static_assets['css'])
        self.assertTrue('/fourth_link.jpg' in self.test_html_page.static_assets['img'])
#creates the test suite, instantiating each instance to call a different
#test method
#def suite():
#    tests = ['test_3', 'test_2']
#    return unittest.TestSuite(map(test_soup, tests))

if __name__ == '__main__':
    unittest.main()
	

"""
Using the following asserts:

1) self.assertEqual(1,2)
2) self.assertTrue(1)
3) self.assertFalse(3)


"""
