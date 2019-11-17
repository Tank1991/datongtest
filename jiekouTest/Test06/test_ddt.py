import  requests
import unittest
import ddt


data = [{"user":"admin","pwd":"11111","except":"True"},
        {"user":"admin2","pwd":"22222","except":"True"},
        {"user":"admin3","pwd":"33333","except":"True"},
        ]

@ddt.ddt
class Test(unittest.TestCase):

        @ddt.data(*data)
        def test_01(self,test_data):
                print("测试用例 ：%s" % test_data )

if __name__ == '__main__':
    unittest.main()












































