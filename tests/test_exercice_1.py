from exercices.exercice_1 import Exercice1
import unittest

class TestStringMethods(unittest.TestCase):

  def setUp(self):
    self.exercice = Exercice1()

  def tearDown(self) -> None:
      return super().tearDown()

  def test_lower(self):
    self.assertEqual(self.exercice.main(18), 'non')

  def test_upper(self):
    self.assertEqual(self.exercice.main(21), 'oui')

if __name__ == '__main__':
  unittest.main()