def preprocess_function(examples):
    inputs = [f"jurídico: {text}" if area == "juridico" else f"médico: {text}" 
            for text, area in zip(examples['original'], examples['area'])]
    
    model_inputs = tokenizer(
    inputs,
    max_length=512,
    truncation=True,
    padding='max_length'
    )

    with tokenizer.as_target_tokenizer():
    labels = tokenizer(
        examples['traducao'],
        max_length=512,
        truncation=True,
        padding='max_length'
    )

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs