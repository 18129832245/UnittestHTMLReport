import unittest
from mathfunc import *


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    """
    @classmethod
    def setUpClass(cls):
        print("This setUpClass() method only called once.")

    @classmethod
    def tearDownClass(cls):
        print("This tearDownClass() method only called once too.")

    # 用于每次测试之前配置环境变量
    def setUp(self):
        print("do something before test.Prepare environment.")

    # 用于每次测试之后恢复环境变量
    def tearDown(self):
        print("do something after test.Clean up.")
    """

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        """
        skip装饰器一共有三个
        unittest.skip(reason):无条件跳过
        unittest.skipIf(condition, reason):当condition为True时跳过
        unittest.skipUnless(condition, reason):当condition为False时跳过
        """

        # self.skipTest('Do not run it')
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))


if __name__ == '__main__':
    unittest.main()
