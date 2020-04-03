from unittest.mock import Mock
from Services import InterestingService, DocumentParser
from Tests.TestEnvironment import test_config


def mocked_interesting_service():
    service = InterestingService(test_config.DEFAULT_INTERESTING_WEIGHT)
    service.get_interesting_rating = Mock(name='get_interesting_rating')
    service.get_interesting_rating.return_value = 10
    return service


def mocked_interesting_service_with_low_interesting_rate():
    service = InterestingService(test_config.DEFAULT_INTERESTING_WEIGHT)
    service.get_interesting_rating = Mock(name='get_interesting_rating')
    service.get_interesting_rating.return_value = 1
    return service

def mocked_document_service():
    service = DocumentParser()
    service.split_to_sentences = Mock(name='split_to_sentences')
    service.split_to_sentences.return_value = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua']
    return service


def get_test_single_sentence():
    return """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
    dolore magna aliqua."""


def get_test_duplicated_sentence():
    return """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
    dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
    labore et dolore magna aliqua."""


def get_test_three_sentences():
    return """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
    dolore magna aliqua. Id interdum velit laoreet id donec ultrices tincidunt. Augue ut lectus arcu bibendum at 
    varius."""
