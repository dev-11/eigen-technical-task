import unittest
from Services import DirectoryScanner


class DirectoryScannerTests(unittest.TestCase):
    def test_scan_new_files_finds_every_file_in_dir(self):
        dir_to_scan = 'Tests/TestEnvironment/'
        ds = DirectoryScanner([dir_to_scan],)
        result = ds.scan_files()
        self.assertEqual(len(result), 3)

        expected_file_list = [dir_to_scan + 'empty.txt',
                              dir_to_scan + 'multi_line.txt',
                              dir_to_scan + 'single_line.txt']

        self.assertEqual(sorted(expected_file_list), sorted(result))
