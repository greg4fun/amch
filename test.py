from challenge import calculate_combinations
import random
import unittest


class calculate_combinationsTest(unittest.TestCase):

    arr1=[1,2,3,4]
    targsum=6
    realsum=2
    def test4(self):
        random.shuffle(self.arr1)
        self.assertEqual(calculate_combinations(self.arr1,self.targsum),self.realsum)

if __name__ == "__main__":
    unittest.main()

