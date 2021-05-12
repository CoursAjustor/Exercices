from exercices.exercice_5 import Exercice5
import unittest
import random
import io
import sys

class TestStringMethods(unittest.TestCase):

  def setUp(self):
    self.exercice = Exercice5()

  def tearDown(self) -> None:
      return super().tearDown()

  def check_if_counter_exist(self):
    self.assertEqual('drawPyramid' in self.exercice, True)

  @unittest.skip('Require the solution if you want to test that')
  def test_if_array_is_good(self):
    testingParam = random.randint(1, 100)
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput
    self.exercice.main(testingParam)
    sys.stdout = sys.__stdout__
    self.assertEqual(True, True)

if __name__ == '__main__':
  unittest.main()