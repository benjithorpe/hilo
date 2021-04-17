from sys import argv

script, target, destination = argv
target_contents = open(target)

destination_contents = open(destination, 'w')
destination_contents.write(target_contents.read())

# close the files
target_contents.close()
destination_contents.close()

