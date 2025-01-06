def word_counter(text):
    words = text.split()
    return len(words)


text = """seu texto aqui"""
quantity_words = word_counter(text)
print(f"Quantidade de palavras: {quantity_words}")