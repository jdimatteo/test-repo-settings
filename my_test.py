import unittest

class MyTest(unittest.TestCase):

    def test_passes(self):
        # comment
        self.assertTrue(True) 

    def test_foo(self):
        # comment
        self.assertTrue(False) 

    def test_bar(self):
        # comment
        self.assertEqual(1, 2) 

    def test_zap(self):
        # comment
        self.assertEqual(blah()) 

if __name__ == '__main__':
    unittest.main()
