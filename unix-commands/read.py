from sys import argv

filename = argv[1]
content = open(filename)
print(content.read())

content.close()
