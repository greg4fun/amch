from challenge import calculate_combinations
import random
import unittest


class calculate_combinationsTest(unittest.TestCase):

    def test1(self):
        arr1 = [1, 2, 3, 4]
        targsum = 6
        realsum = 2
        random.shuffle(arr1)
        self.assertEqual(calculate_combinations(arr1, targsum), realsum)

    def test2(self):
        arr1 = [-1, 2, -3, 4]
        targsum = 6
        realsum = 2
        random.shuffle(arr1)
        self.assertEqual(calculate_combinations(arr1, targsum), realsum)

    def test3(self):
        arr1 = ['A', 'B', 'C', 'D']
        targsum = 6
        realsum = 2
        random.shuffle(arr1)
        self.assertEqual(calculate_combinations(arr1, targsum), realsum)

    def test4(self):
        arr1 = ['1', '2', '3', '4']
        targsum = 6
        realsum = 2
        random.shuffle(arr1)
        self.assertEqual(calculate_combinations(arr1, targsum), realsum)

    def test5(self):
        arr1 = [-1, 2, -3, 4]
        targsum = 6
        realsum = 2
        random.shuffle(arr1)
        self.assertEqual(calculate_combinations(arr1, targsum), realsum)
if __name__ == "__main__":
    unittest.main()
