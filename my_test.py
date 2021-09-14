import unittest

class MyTest(unittest.TestCase):

    def test_passes(self):
        self.assertTrue(True) 
        
    def test_passes_again(self):
        pass 


if __name__ == '__main__':
    unittest.main()
