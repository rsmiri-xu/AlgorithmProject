class SemanticGraph:
    def __init__(self, words):
        self.words = words
        self.graph = {}
        for word in words:
            self.graph[word] = {}

    def add_edge(self, word1, word2, weight):
        self.graph[word1][word2] = weight
        self.graph[word2][word1] = weight