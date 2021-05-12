from exercices.exercice_4b import Exercice4b
import unittest
import random

class TestStringMethods(unittest.TestCase):

  def setUp(self):
    self.exercice = Exercice4b()

  def tearDown(self) -> None:
      return super().tearDown()

  def check_if_counter_exist(self):
    self.assertEqual('counterOdd' in self.exercice, True)

  def test_if_array_is_good(self):
    testingParam = random.randint(1, 100)
    self.assertEqual(self.exercice.main(testingParam), range(2, testingParam+1, 2))

if __name__ == '__main__':
  unittest.main()