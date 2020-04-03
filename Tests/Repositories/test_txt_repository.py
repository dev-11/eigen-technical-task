import unittest
from Repositories import TxtRepository


class TxtRepositoryTests(unittest.TestCase):

    def test_get_headers_returns_headers(self):
        txt_file = 'Tests/TestEnvironment/empty.txt'
        repo = TxtRepository()
        result = repo.read_file(txt_file)
        self.assertEqual(0, len(result))

    def test_get_metadata_raisesStopIteration_on_missing_description_row(self):
        txt_file = 'Tests/TestEnvironment/single_line.txt'
        repo = TxtRepository()
        result = repo.read_file(txt_file)
        self.assertEqual(1, len(result))

    def test_get_metadata_returns_description_row(self):
        txt_file = 'Tests/TestEnvironment/multi_line.txt'
        repo = TxtRepository()
        result = repo.read_file(txt_file)
        self.assertEqual(3, len(result))
