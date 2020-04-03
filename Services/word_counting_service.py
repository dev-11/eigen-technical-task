import config


class WordCountingService:
    def __init__(self, parser_service, interesting_service):
        self._word_count = []
        self._parser_service = parser_service
        self._interesting_service = interesting_service

    def populate(self, sentence, document_name):
        words = self._parser_service.split_to_words(sentence)
        for word in words:
            interesting_rating = self._interesting_service.get_interesting_rating(word.lower())

            if interesting_rating >= config.INTERESTING_RATING_THRESHOLD:

                word_in_list = next((x for x in self._word_count if x["word"] == word.lower()), None)

                if word_in_list is not None:
                    word_in_list["count"] += 1
                    if document_name in word_in_list:
                        word_in_list[document_name].append(sentence)
                    else:
                        word_in_list[document_name] = [sentence]
                else:
                    self._word_count.append({
                        "word": word.lower(),
                        "interesting_rating": interesting_rating,
                        "count": 1,
                        document_name: [sentence]
                    })

    def get_word_count(self):
        return self._word_count
