def validate_pairs(df):
    problems = []
    for idx, row in df.iterrows():
        orig_len = len(row['original'].split())
        trad_len = len(row['traducao'].split())
    
        if max(orig_len, trad_len) / min(orig_len, trad_len) > 3:
            problems.append(idx)
        
        if row['original'].lower() == row['traducao'].lower():
            problems.append(idx)
    
    return df.drop(problems)

train_df = validate_pairs(train_df)