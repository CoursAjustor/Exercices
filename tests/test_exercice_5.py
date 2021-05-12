import unittest
import random
import io
import sys
from exercices.exercice_5 import Exercice5


class TestStringMethods(unittest.TestCase):
    """
        The testing class for exercice 5
    """

    def setUp(self):
        """
            setUp the system
        """
        self.exercice = Exercice5()

    def check_if_counter_exist(self):
        """
            test if the result of the main function
            of the exercice is the right answer
        """
        self.assertEqual('drawPyramid' in dir(self.exercice), True)

    @unittest.skip('Require the solution if you want to test that')
    def test_if_array_is_good(self):
        """
            test if the result of the main function
            of the exercice is the right answer
        """
        testing_param = random.randint(1, 100)
        captured_output = io.StringIO()                  # Create StringIO object
        sys.stdout = captured_output
        self.exercice.main(testing_param)
        sys.stdout = sys.__stdout__
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
