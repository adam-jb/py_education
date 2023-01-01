import unittest
import numpy as np

def Widget():
    ar = np.random.rand(50,50)
    return ar

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
        
    def test_default_widget_size(self):
        self.assertEqual(self.widget.shape, (50, 50))
        
    def tearDown(self):
        del self.widget


class NumbersTest(unittest.TestCase):
    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
                

if __name__ == '__main__':
    unittest.main()