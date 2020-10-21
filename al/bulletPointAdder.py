#! python3
# bulletPointAdder.py - Adds wikipedia bullet points to the
# start of each line of text on the clipboard
# and removes trailing whitespaces on both sides.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):  # loop through all indexes in the "lines" list
    # add star to each string in "lines" list
    lines[i] = '* ' + lines[i].strip()

text = '\n'.join(lines)
pyperclip.copy(text)
