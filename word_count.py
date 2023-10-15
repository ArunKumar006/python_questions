def count_word(sentence):
    words=sentence.split()
    return len(words)

input_val=input("enter the sentence")
wc=count_word(input_val)
print(f"sentence containing {wc} words")