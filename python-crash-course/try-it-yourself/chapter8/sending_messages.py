messages = [
    "hello world",
    "welcome to python list",
    "almost finished with list",
    "working of web scraping next",
]
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages):
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
        print(current_message)


show_messages(messages)
send_messages(messages)

print()
print(messages)
print(sent_messages)
