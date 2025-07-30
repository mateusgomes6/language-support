from pathlib import Path
from config.constantes import LEGAL_ACRONYMS

def gerenate_final_dataser():
    clean_jur_path = Path('./raw/juridico.txt')
    clean_med_path = Path('./raw/medico.txt')
    
    texts_jur = clean_jur_path.read_text(encoding='utf-8').splitlines()
    texts_med = clean_med_path.read_text(encoding='utf-8').splitlines()

    dataset = {
        'juridico': texts_jur,
        'medico': texts_med
    }

    output_path = Path('data/processed/final/dataset.json')
    output_path.write_text(json.dumps(dataset, ensure_ascii=False), encoding='utf-8')

    print(f"Dataset final gerado em {output_path}")

if __name__ == '__main__':
    gerenate_final_dataser()