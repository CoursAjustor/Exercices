from exercices.exercice_3 import Exercice3
import unittest
import random

class TestStringMethods(unittest.TestCase):

  def setUp(self):
    self.exercice = Exercice3()

  def tearDown(self) -> None:
      return super().tearDown()

  def check_if_counter_exist(self):
    self.assertEqual('counter' in self.exercice, True)

  def test_if_array_is_good(self):
    testingParam = random.randint(1, 100)
    self.assertEqual(self.exercice.main(testingParam), range(1, testingParam+1))

if __name__ == '__main__':
  unittest.main()