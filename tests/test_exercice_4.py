from exercices.exercice_4 import Exercice4
import unittest
import random

class TestStringMethods(unittest.TestCase):

  def setUp(self):
    self.exercice = Exercice4()

  def tearDown(self) -> None:
      return super().tearDown()

  def check_if_counter_exist(self):
    self.assertEqual('counterEven' in self.exercice, True)

  def test_if_array_is_good(self):
    testingParam = random.randint(1, 100)
    self.assertEqual(self.exercice.main(testingParam), range(1, testingParam+1, 2))

if __name__ == '__main__':
  unittest.main()