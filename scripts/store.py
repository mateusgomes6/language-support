tokenized_dataset.save_to_disk('./dataset_preprocessado')

train_df.to_csv('./dataset_treinamento.csv', index=False)
val_df.to_csv('./dataset_validacao.csv', index=False)