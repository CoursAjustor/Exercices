"""
    The class who test the exercice 1 result
"""
import unittest
from exercices.exercice_1 import Exercice1


class TestStringMethods(unittest.TestCase):
    """
        The testing class for exercice 1
    """

    def setUp(self):
        """
            setUp the system
        """
        self.exercice = Exercice1()

    def test_lower(self):
        """
            test if the result of the main function
            of the exercice is the right answer
        """
        self.assertEqual(self.exercice.main(18), 'non')

    def test_upper(self):
        """
            test if the result of the main function
            of the exercice is the right answer
        """
        self.assertEqual(self.exercice.main(21), 'oui')


if __name__ == '__main__':
    unittest.main()
