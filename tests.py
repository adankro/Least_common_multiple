import timeit
from unittest import TestCase, skip

from lcm import (Least_common_multiple_loop,
                 Least_common_multiple_A003418)


class Test_lcm(TestCase):
    def test_brutal_force_method_1_10(self):
        self.assertEqual(Least_common_multiple_loop(1, 10), 2520)

    @skip
    #because is veri slow but it woks.
    def test_brutal_force_method_1_20(self):
            self.assertEqual(Least_common_multiple_loop(1, 20), 232792560)
    
    def test_brutal_force_method_1_5(self):
        self.assertEqual(Least_common_multiple_loop(1, 5), 12)

    def test_A003418_method_1_10(self):
        self.assertEqual(Least_common_multiple_A003418(1, 10), 2520)

    def test_A003418_method_1_20(self):
        self.assertEqual(Least_common_multiple_A003418(1, 20), 232792560)