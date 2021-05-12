
"""
    test if the result of the main function
    of the exercice is the right answer
"""
import unittest
from exercices.exercice_2 import Exercice2


class TestStringMethods(unittest.TestCase):
    """
        The testing class for exercice 2
    """

    def setUp(self):
        """
            setUp the system
        """
        self.exercice = Exercice2()

    def test_big_lower(self):
        """
            test if the result of the main function
            of the exercice is the right answer
        """
        self.assertEqual(self.exercice.main(15), 'non')

    def test_lower(self):
        """
            test if the result of the main function
            of the exercice is the right answer
        """
        self.assertEqual(self.exercice.main(18), 'oui sauf EU')

    def test_upper(self):
        """
            test if the result of the main function
            of the exercice is the right answer
        """
        self.assertEqual(self.exercice.main(21), 'oui')


if __name__ == '__main__':
    unittest.main()
