#coding:utf-8
import unittest

class IntegerArithmeticTestCase(unittest.TestCase):

    def add(self,a ,b ):
        return  a + b

    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
        unittest.main()

# E  代码没有走完，自己写的BUG
# F   代码走完了，开发的BUG




