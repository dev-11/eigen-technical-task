import re


class DocumentParser:
    @staticmethod
    def split_to_sentences(text):
        return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<= \.| \?)\s', text)

    @staticmethod
    def split_to_words(text):
        return text.split()
