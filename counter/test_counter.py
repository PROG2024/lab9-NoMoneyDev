"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""

import unittest
from counter import Counter

class Test(unittest.TestCase):
    def setUp(self):
        self.counter = Counter()

    def test_singleton(self):
        new_counter = Counter()
        self.assertIs(new_counter, self.counter)

    def test_count_sharing(self):
        new_counter = Counter()
        self.counter.increment()
        self.assertEqual(new_counter.count, self.counter.count)

    def test_new_counter_after_increment(self):
        self.counter.increment()
        self.counter.increment()
        new_counter = Counter()
        self.assertEqual(new_counter.count, self.counter.count)
