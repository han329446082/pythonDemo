import unittest


class MyTest01(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def test01(self):
        self.assertEqual(1 + 2, 3)

    def test02(self):
        self.assertGreater(2, 1)

    def tearDown(self):
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()
