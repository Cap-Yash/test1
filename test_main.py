from unittest import TestCase
import main

class Test(TestCase):
    def test_add(self):
        print("test executed")
        assert main.add(5,5)==10
