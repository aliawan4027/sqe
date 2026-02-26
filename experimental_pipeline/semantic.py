# semantic.py
"""
Semantic similarity module using SentenceTransformer.
"""
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_similarity(text1, text2):
    emb1 = model.encode([text1])
    emb2 = model.encode([text2])
    return float(cosine_similarity(emb1, emb2)[0][0])