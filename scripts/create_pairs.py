import pandas as pd
from sklearn.model_selection import train_test_split

def create_translation_pairs(termos, traducoes):
    df = pd.DataFrame({'original': termos, 'traducao': traducoes})

    df = df[df['original'].str.split().str.len() == df['traducao'].str.split().str.len()]

    train, val = train_test_split(df, test_size=0.2)
    return train, val