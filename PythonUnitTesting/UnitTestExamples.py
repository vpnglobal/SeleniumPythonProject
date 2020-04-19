# import unit test module of python
import unittest
from Examples import Example


class MyTestCase (unittest.TestCase):
#method should be prefixed with keyword 'test'
    @classmethod        #Use annotation @classmethod
    def setUpClass(cls):
        print("This will run before all the methods")
    @classmethod
    def tearDownClass(cls):
        print("This will run once after all the method ")
    def setUp(self):
        print("This will run before every method")

    def tearDown(self):
        print("This will after every method")

    def test_add(self):
        result = Example.add(self,10,20)
        self.assertEqual(result,30)

    def test_sub(self):
        result = Example.sub(self,30,20)
        self.assertEqual(Example.sub(self,30,20),10)
        self.assertEqual(Example.sub(self,50,60),-10)

# if __name__ == '__main__':
#     unittest.main ()
