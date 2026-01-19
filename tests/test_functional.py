import unittest

from algorithms.factorial import factorial
from algorithms.fibonacci import fib_dp
from algorithms.sorts import selection_sort, bubble_sort
from algorithms.mergesort import merge_sort
from algorithms.stats_search import stats_summary
from algorithms.palindromes import count_pal_substrings

class FunctionalTests(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(fib_dp(0), 0)
        self.assertEqual(fib_dp(10), 55)

    def test_sorts(self):
        self.assertEqual(selection_sort([3,1,2], True), [1,2,3])
        self.assertEqual(bubble_sort([3,1,2], False), [3,2,1])

    def test_mergesort(self):
        self.assertEqual(merge_sort([5,4,3,2,1], True), [1,2,3,4,5])

    def test_stats(self):
        s = stats_summary([1,2,2,3,4,9])
        self.assertEqual(s["smallest"], 1)
        self.assertEqual(s["largest"], 9)
        self.assertEqual(s["median"], 2.5)

    def test_palindromes(self):
        self.assertEqual(count_pal_substrings("aaa"), 6)

if __name__ == "__main__":
    unittest.main()