from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def get_semantic_similarity(word1, word2):
    if word1 == word2:
        return 0
    emb1 = model.encode(word1)
    emb2 = model.encode(word2)
    similarity = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
    return round(1 - similarity, 3)