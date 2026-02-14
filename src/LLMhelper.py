import random

def get_semantic_similarity(word1, word2):
    if word1 == word2:
        return 0
    related = [("سیب", "میوه"), ("ماشین", "خودرو"), ("کتاب", "درس")]
    if (word1, word2) in related or (word2, word1) in related:
        return round(random.uniform(0.1, 0.3), 2)
    return round(random.uniform(0.6, 0.9), 2)