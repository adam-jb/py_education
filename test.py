from unittest import TestCase
from main import Calculator
from unittest.mock import patch, Mock



class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)

    def test_sum(self):
        answer = self.calc.sum(3, 4)
        self.assertEqual(answer, 7)



# instead of reading in the actual func, this makes a dummy called 'sum' which always returns 9
class TestCalculator2(TestCase):
    @patch('main.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 9)




# MockBlog is a variable name and you can call it whatever you want
class TestBlog(TestCase):
    @patch('main.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        # set predefined json to return as part of the mock
        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable  end  of the  western  spiral  arm  of  the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]
        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)




def mock_sum(a, b):
    # mock sum function without the long running time.sleep
    return a + b

class TestCalculator3(TestCase):
    @patch('main.Calculator.sum', side_effect=mock_sum)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 5)
        self.assertEqual(sum(7,3), 10)















