"""Global options for analysis
"""
from pathlib import Path
import os
from typing import Optional, List, Set, Dict

# Hardware options
N_CORES: int = 2  # max number of CPU cores to use
RAM_CORENLP: str = "16G"  # max RAM allocated for parsing using CoreNLP

# Directory locations
os.environ[
    "CORENLP_HOME"
] = "/home/mai/stanfordnlp_resources/coreNLP/"  # location of the CoreNLP models
DATA_FOLDER: str = "data/"
MODEL_FOLDER: str = "models/"
OUTPUT_FOLDER: str = "outputs/"

# Parsing and analysis options
STOPWORDS: Set[str] = set(
    Path("resources", "StopWords_Generic.txt").read_text().lower().split()
)  # Set of stopwords from https://sraf.nd.edu/textual-analysis/resources/#StopWords
PHRASE_THRESHOLD: int = 10  # threshold of the phraser module (smaller -> more phrases)
PHRASE_MIN_COUNT: int = 10  # min number of times a bigram needs to appear in the corpus to be considered as a phrase
W2V_DIM: int = 300  # dimension of word2vec vectors
W2V_WINDOW: int = 5  # window size in word2vec
W2V_ITER: int = 20  # number of iterations in word2vec
N_WORDS_DIM: int = 500  # max number of words in each dimension of the dictionary
DICT_RESTRICT_VOCAB = None # change to a fraction number (e.g. 0.2) to restrict the dictionary vocab in the top 20% of most frequent vocab

# Inputs for constructing the expanded dictionary
DIMS: List[str] = ["integrity", "teamwork", "innovation", "respect", "quality"]
SEED_WORDS: Dict[str, List[str]] = {
    "integrity": [
        "integrity",
        "ethic",
        "ethical",
        "accountable",
        "accountability",
        "trust",
        "honesty",
        "honest",
        "honestly",
        "fairness",
        "responsibility",
        "responsible",
        "transparency",
        "transparent",
    ],
    "teamwork": [
        "teamwork",
        "collaboration",
        "collaborate",
        "collaborative",
        "cooperation",
        "cooperate",
        "cooperative",
    ],
    "innovation": [
        "innovation",
        "innovate",
        "innovative",
        "creativity",
        "creative",
        "create",
        "passion",
        "passionate",
        "efficiency",
        "efficient",
        "excellence",
        "pride",
    ],
    "respect": [
        "respectful",
        "talent",
        "talented",
        "employee",
        "dignity",
        "empowerment",
        "empower",
    ],
    "quality": [
        "quality",
        "customer",
        "customer_commitment",
        "dedication",
        "dedicated",
        "dedicate",
        "customer_expectation",
    ],
}


# Create directories if not exist
Path(DATA_FOLDER, "processed", "parsed").mkdir(parents=True, exist_ok=True)
Path(DATA_FOLDER, "processed", "unigram").mkdir(parents=True, exist_ok=True)
Path(DATA_FOLDER, "processed", "bigram").mkdir(parents=True, exist_ok=True)
Path(DATA_FOLDER, "processed", "trigram").mkdir(parents=True, exist_ok=True)
Path(MODEL_FOLDER, "phrases").mkdir(parents=True, exist_ok=True)
Path(MODEL_FOLDER, "phrases").mkdir(parents=True, exist_ok=True)
Path(MODEL_FOLDER, "w2v").mkdir(parents=True, exist_ok=True)
Path(OUTPUT_FOLDER, "dict").mkdir(parents=True, exist_ok=True)
Path(OUTPUT_FOLDER, "scores").mkdir(parents=True, exist_ok=True)
Path(OUTPUT_FOLDER, "scores", "temp").mkdir(parents=True, exist_ok=True)
Path(OUTPUT_FOLDER, "scores", "word_contributions").mkdir(parents=True, exist_ok=True)
