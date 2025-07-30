from pathlib import Path

def load_terms():
    juridical_terms = Path('data/raw/juridico.txt').read_text().splitlines()
    medical_terms = Path('data/raw/medico.txt').read_text().splitlines()
    return juridical_terms, medical_terms