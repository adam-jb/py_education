import unittest

def check_integer(x):
    if not isinstance(x, int):
        raise TypeError('Input must be an integer')

def Widget(x):
    return x*2

# checking with unittest class
class TestCheckInteger(unittest.TestCase):
    
    def setUp(self):
        self.widget = Widget(3)    
    
    def test_check_integer(self):
        self.assertIsInstance(Widget(3), int)
        self.assertEqual(Widget(10), 20)
        check_integer(self.widget)
        
    def tearDown(self):
        del self.widget    


if __name__ == '__main__':
    main()
