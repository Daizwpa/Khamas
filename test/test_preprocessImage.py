
from Controller.PreprocessImage import PreProcess
import unittest
from utils.image_core import imSave
# python -m unittest discover -s test -p "test_*.py"
import numpy as np


class test_PreProcess(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # run once before all test cases ###
        pass

    @classmethod
    def tearDownClass(cls):  # run once after all test cases ###
        pass

    def setUp(self):  # run before each test case ###
        self.path = "C:\\Users\\User\\Pictures\\8.png"
        self.processor = PreProcess(1200, 1200, 2)

    def tearDown(self):  # run after each test case ###
        pass

    def test_process(self):
        image = self.processor.process(self.path)
        assert image is not None
        print(np.shape(image))
        imSave(image=image, path="C:\\Users\\User\\Desktop\\image.jpg")
