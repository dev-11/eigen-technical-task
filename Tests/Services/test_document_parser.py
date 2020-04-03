import unittest
from Services import DocumentParser
from Tests.TestEnvironment import get_test_three_sentences, get_test_single_sentence


class DocumentParserTest(unittest.TestCase):
    def test_split_to_sentences_returns_single_sentence_for_single_sentence(self):
        test_sentence = get_test_single_sentence()
        service = DocumentParser()
        sentences = service.split_to_sentences(test_sentence)
        self.assertEqual(1, len(sentences))

    def test_split_to_sentences_returns_single_sentence_for_single_sentence(self):
        test_sentences = get_test_three_sentences()
        service = DocumentParser()
        sentences = service.split_to_sentences(test_sentences)
        self.assertEqual(3, len(sentences))

    def test_split_to_sentences_returns_empty_sentence_for_empty_sentence(self):
        test_sentences = ""
        service = DocumentParser()
        sentences = service.split_to_sentences(test_sentences)
        self.assertEqual(1, len(sentences))
        self.assertEqual("", sentences[0])

    def test_split_to_sentences_raises_error_for_None(self):
        test_sentences = None
        service = DocumentParser()
        self.assertRaises(TypeError, service.split_to_sentences, test_sentences)

    def test_split_to_words_returns_correct_list_for_single_sentence(self):
        test_sentences = get_test_single_sentence()
        service = DocumentParser()
        words = service.split_to_words(test_sentences)
        self.assertEqual(19, len(words))

    def test_split_to_words_returns_empty_list_for_empty_string(self):
        test_sentences = ""
        service = DocumentParser()
        words = service.split_to_words(test_sentences)
        self.assertEqual(0, len(words))

    def test_split_to_words_raises_error_for_None(self):
        test_sentences = None
        service = DocumentParser()
        self.assertRaises(AttributeError, service.split_to_words, test_sentences)
