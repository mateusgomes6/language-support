from scripts.clean_normalize import clean_text
from pathlib import Path

def process():
    clean_juridico = Path('data/processed/cleaned/juridico.txt').read_text().splitlines()
    
    processed_terms = [f"JUR_{termo}" for termo in clean_juridico]
    
    Path('data/processed/tokenized/juridico.txt').write_text('\n'.join(processed_terms))