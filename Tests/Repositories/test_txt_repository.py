import unittest
from Repositories import TxtRepository


class TxtRepositoryTests(unittest.TestCase):

    def test_read_file_returns_empty_result_for_empty_file(self):
        txt_file = 'Tests/TestEnvironment/empty.txt'
        repo = TxtRepository()
        result = repo.read_file(txt_file)
        self.assertEqual(0, len(result))

    def test_read_file_returns_single_line_result_for_single_line_file(self):
        txt_file = 'Tests/TestEnvironment/single_line.txt'
        repo = TxtRepository()
        result = repo.read_file(txt_file)
        self.assertEqual(1, len(result))

    def test_read_file_returns_every_line_for_multiple_lines_file(self):
        txt_file = 'Tests/TestEnvironment/multi_line.txt'
        repo = TxtRepository()
        result = repo.read_file(txt_file)
        self.assertEqual(3, len(result))
