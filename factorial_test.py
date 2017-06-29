import unittest
from factorial import fact

class TestFactorial(unittest.TestCase):
    """
     我们的基本测试类
     """
    def test_fact(self):
        """
         实际测试
         任何以 'test_' 开头的方法都被视为测试用例
          
         """
        res = fact(5)
        self.assertEqual(res, 120)    # assertEqual() 进行测试判断


if __name__ == '__main__':
    unittest.main()
