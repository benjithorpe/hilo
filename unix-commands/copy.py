from sys import argv

script, target, destination = argv
target_file = open(target)

destination_file = open(destination, 'w')
destination_file.write(target_file.read())

# close the files
target_file.close()
destination_file.close()

