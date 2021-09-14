import unittest

class MyTest(unittest.TestCase):

    def test_passes(self):
        self.assertTrue(True) 
        
    def test_fails(self):
        self.assertTrue(True==False) 


if __name__ == '__main__':
    unittest.main()
