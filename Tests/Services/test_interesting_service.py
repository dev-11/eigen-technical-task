import unittest
from Services import InterestingService


class InterestingServiceTest(unittest.TestCase):
    def test_single_char_returns_rating_one(self):
        weight = 1
        service = InterestingService(weight)
        rating = service.get_interesting_rating("a")
        self.assertEqual(1, rating)

    def test_interesting_char_returns_double_rating(self):
        weight = 1
        service = InterestingService(weight)
        rating = service.get_interesting_rating("-")
        self.assertEqual(2, rating)

    def test_empty_string_returns_zero_rating(self):
        weight = 1
        service = InterestingService(weight)
        rating = service.get_interesting_rating("")
        self.assertEqual(0, rating)

    def test_None_object_raises_exception(self):
        weight = 1
        service = InterestingService(weight)
        self.assertRaises(TypeError, service.get_interesting_rating, None)
