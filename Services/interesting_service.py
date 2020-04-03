class InterestingService:
    def __init__(self, weight):
        self._weight = weight

    def get_interesting_rating(self, word):
        custom_weight = 2 if '-' in word else 1
        return len(word) * self._weight * custom_weight
