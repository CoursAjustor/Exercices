"""
    The class who test the exercice 1 result
"""
import unittest
import random
from exercices.exercice_1 import sum


class TestStringMethods(unittest.TestCase):
    """
        The testing class for exercice 1
    """

    def test_function(self):
        """
            test if the result of the main function
            of the exercice is the right answer
        """
        testing_param1 = random.randint(1, 100)
        testing_param2 = random.randint(1, 100)

        self.assertEqual(sum(testing_param1, testing_param2),
                         testing_param1 + testing_param2)


if __name__ == '__main__':
    unittest.main()
