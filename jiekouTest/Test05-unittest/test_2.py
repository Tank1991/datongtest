#coding;utf-8
import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("在一个类里面，只有kaishi     才执行的")


    def setUp(self):
        print("登录前要执行的！")

    def testAdd(self):  # test method names begin with 'test'
        print("测试用例 11111")
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        print("测试用例 22222")
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

    def tearDown(self):
        print("最后执行的方法")
    @classmethod
    def tearDownClass(cls):
        print("在一个类里面，只有最后才执行的")

if __name__ == '__main__':
        unittest.main()






