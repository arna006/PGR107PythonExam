def redact_words(original_filename, sensitive_words_filename, redacted_filename):
    try:
        with open(original_filename, 'r') as original_file:
            original_text = original_file.read()

        with open(sensitive_words_filename, 'r') as sensitive_words_file:
            sensitive_words = sensitive_words_file.read().splitlines()

        for word in sensitive_words:
            original_text = original_text.replace(word, '*' * len(word))

        with open(redacted_filename, 'w') as redacted_file:
            redacted_file.write(original_text)

        print("Redacted text saved successfully!")
    except FileNotFoundError:
        print("The files could not be found. Please check again.")

redact_words('original.txt', 'sensitive_words.txt', 'redacted.txt')
