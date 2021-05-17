def reverse_words_order_and_swap_cases(sentence):
    final_sentence = ""

    for letter in sentence:
        if letter.isupper():
            letter = letter.lower()
        elif letter.islower():
            letter = letter.upper()
        final_sentence += letter
    return ' '.join(final_sentence.split()[::-1])


sentence = "aWESOME is cODING"
reverse_words_order_and_swap_cases(sentence)


def count(string):
    letter_count = {}

    for letter in string:
        if letter in letter_count:
            letter_count[letter] = letter_count[letter] + 1
        else:
            letter_count[letter] = 1

    print(letter_count)


count("hello world")
