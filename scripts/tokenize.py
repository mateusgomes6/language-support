from transformers import AutoTokenizer
from nltk.tokenize import word_tokenize
import spacy

nlp_pt = spacy.load('pt_core_news_lg')
tokenizer_bert = AutoTokenizer.from_pretrained('neuralmind/bert-base-portuguese-cased')

def tokenize_legal(text):
    doc = nlp_pt(text)
    tokens = []
    for token in doc:
        if token.ent_type_ == 'LEGISLACAO':
            tokens.append('[LEI]')
        elif token.ent_type_ == 'JURISPRUDENCIA':
            tokens.append('[JUR]')
        else:
            tokens.append(token.text)
    return ' '.join(tokens)

def tokenize_medical(text):
    medical_terms = ['tumor benigno', 'hipertensão arterial']
    for term in medical_terms:
        text = text.replace(term, term.replace(' ', '_'))
    return word_tokenize(text, language='portuguese')