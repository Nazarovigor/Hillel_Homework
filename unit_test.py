import unittest


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Start running suite')

    def setUp(self):
        print('Start running test case')

    def test_my_first_test_case(self):
        self.assertTrue(1 != 1 )

    def test_2(self):
        self.assertTrue(all([True, 1, 'Some']))

    def tearDown(self):
        print('End running test case')

    @classmethod
    def tearDownClass(cls):
        print('End running suite')


if __name__ == '__main__':
    unittest.main()
