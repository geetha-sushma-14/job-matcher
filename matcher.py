import spacy
import torch
from sentence_transformers import SentenceTransformer, util

# Load spaCy model for preprocessing
nlp = spacy.load("en_core_web_sm")

# Load a pre-trained sentence embedding model (SBERT)
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def preprocess_text(text):
    """Clean and preprocess text using spaCy."""
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

def get_embedding(text):
    """Convert text to embeddings."""
    return embedding_model.encode(text, convert_to_tensor=True)

def match_resume_to_jobs(resume_text, job_descriptions):
    """
    Compare resume with multiple job descriptions using cosine similarity.
    
    Args:
    - resume_text (str): Resume text
    - job_descriptions (dict): {"job1": "description1", "job2": "description2", ...}

    Returns:
    - Sorted job matches based on similarity score.
    """
    resume_text = preprocess_text(resume_text)
    resume_embedding = get_embedding(resume_text)

    results = []
    for job_title, job_desc in job_descriptions.items():
        job_desc = preprocess_text(job_desc)
        job_embedding = get_embedding(job_desc)
        similarity = util.pytorch_cos_sim(resume_embedding, job_embedding).item()
        results.append((job_title, similarity))

    # Sort jobs by similarity score (descending order)
    results.sort(key=lambda x: x[1], reverse=True)
    return results
