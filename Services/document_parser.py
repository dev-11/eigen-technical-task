from nltk import word_tokenize, sent_tokenize


class DocumentParser:
    @staticmethod
    def split_to_sentences(text):
        return [sentence for sentence in sent_tokenize(text)]

    @staticmethod
    def split_to_words(text):
        return word_tokenize(text)
