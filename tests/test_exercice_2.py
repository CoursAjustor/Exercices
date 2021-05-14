
"""
    test if the result of the main function
    of the exercice is the right answer
"""
import random
import unittest
from exercices.exercice_2 import sub


class TestStringMethods(unittest.TestCase):
    """
        The testing class for exercice 2
    """

    def test_function(self):
        """
            test if the result of the main function
            of the exercice is the right answer
        """
        a, b = random.randint(1, 100), random.randint(1, 100)
        self.assertEqual(sub(a, b), a-b)


if __name__ == '__main__':
    unittest.main()
