import re
import unicodedata

def clean_text(text):
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')

    text = re.sub(r'\bArt\.?\s*\d+º?', ' Artigo ', text, flags=re.IGNORECASE)
    text = re.sub(r'\bParágrafo\s*\w+', ' Parágrafo ', text, flags=re.IGNORECASE)

    text = re.sub(r'\b[A-Z]{2,5}\s*\d+', ' ', text)

    words = text.split()
    words = [w.upper() if w in SIGLAS_JURIDICAS else w.lower() for w in words]

    return ' '.join(words).strip()