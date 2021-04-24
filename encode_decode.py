print('==== Welcome to Encoder ====')
word = input('Enter a word or sentence to Encode: ')
print(f"""\nEncoded input is:
========================
{word.encode('utf16')}
========================
""")
