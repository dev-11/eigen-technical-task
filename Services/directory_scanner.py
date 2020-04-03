import os
import config


class DirectoryScanner:
    def __init__(self, directories):
        self._directories = directories

    def scan_files(self):
        files = []
        for current_dir in self._directories:
            for file in os.listdir(current_dir):
                if file[0] != '.' and '.' in file:  # skipping hidden files and focusing on files with ext
                    filename, extension = file.split('.')
                    if extension == config.TXT_FILE_EXTENSION:
                        files.append(current_dir + file)
        return files
