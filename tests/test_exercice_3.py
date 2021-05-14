import unittest
import random
from exercices.exercice_3 import Exercice3


class TestStringMethods(unittest.TestCase):
    """
        The testing class for exercice 3
    """

    def setUp(self):
        """
            setUp the system
        """
        self.exercice = Exercice3()

    def check_if_counter_exist(self):
        """
            test if the result of the main function
            of the exercice is the right answer
        """
        self.assertEqual('counter' in dir(self.exercice), True)

    def test_if_array_is_good(self):
        """
            test if the result of the main function
            of the exercice is the right answer
        """
        testing_param = random.randint(1, 100)
        self.assertEqual(self.exercice.main(
            testing_param), list(range(1, testing_param+1)))


if __name__ == '__main__':
    unittest.main()
