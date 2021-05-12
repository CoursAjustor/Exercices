from exercices.exercice_2 import Exercice2
import unittest

class TestStringMethods(unittest.TestCase):

  def setUp(self):
    self.exercice = Exercice2()

  def tearDown(self) -> None:
      return super().tearDown()

  def test_big_lower(self):
    self.assertEqual(self.exercice.main(15), 'non')

  def test_lower(self):
    self.assertEqual(self.exercice.main(18), 'oui sauf EU')

  def test_upper(self):
    self.assertEqual(self.exercice.main(21), 'oui')

if __name__ == '__main__':
  unittest.main()