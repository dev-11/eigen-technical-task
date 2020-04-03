import unittest
from Services import WordCountingService
from Tests.TestEnvironment.mocks import get_test_single_sentence, mocked_interesting_service, mocked_document_service,\
    mocked_interesting_service_with_low_interesting_rate, get_test_duplicated_sentence
import Tests.TestEnvironment.test_config as config


class WordCountingServiceTest(unittest.TestCase):
    def test_populate_populates_word_count_with_single_words(self):
        test_sentence = get_test_single_sentence()
        document_name = "document_name"
        service = WordCountingService(mocked_document_service(), mocked_interesting_service(), config)
        service.populate(test_sentence, document_name)
        data = service.get_word_count()
        self.assertEqual(19, len(data))

    def test_populate_leaves_word_count_empty_as_interesting_threshold_is_too_low_for_every_word(self):
        test_sentence = get_test_single_sentence()
        document_name = "document_name"
        service = WordCountingService(mocked_document_service(), mocked_interesting_service_with_low_interesting_rate(),
                                      config)
        service.populate(test_sentence, document_name)
        data = service.get_word_count()
        self.assertEqual(0, len(data))

    def test_populate_populates_word_count_for_duplicated_sentence(self):
        test_sentence = get_test_duplicated_sentence()
        document_name = "document_name"
        service = WordCountingService(mocked_document_service(), mocked_interesting_service(), config)
        service.populate(test_sentence, document_name)
        data = service.get_word_count()
        self.assertEqual(19, len(data))
        for d in data:
            self.assertEqual(2, d['count'])
