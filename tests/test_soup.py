import unittest
from .context import crawler

class test_soup(unittest.TestCase):
    #set up for all of the soup test functions
    def setUp(self):
        return

    #tear down for all of the soup test functions
    def tearDown(self):
        return

    def test_1(self):
        pass
    
    def test_2(self):
        pass

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
