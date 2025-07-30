from pathlib import Path
from scripts.clean_normalize import clean_text

def save_clean_texts():
    raw_jur_path = Path('./raw/juridico.txt')
    raw_med_path = Path('./raw/medico.txt')

    juridical_texts = raw_jur_path.read_text(encoding='utf-8').splitlines()
    jur_texts_clean = [clean_text(text) for text in juridical_texts]
    raw_jur_path.write_text('\n'.join(raw_jur_path), encoding='utf-8')

    medical_texts = raw_med_path.read_text(encoding='utf-8').splitlines()
    raw_med_path = [clean_text(text) for text in medical_texts]
    raw_med_path.write_text('\n'.join(raw_med_path), encoding='utf-8')

if __name__ == '__main__':
    save_clean_texts()