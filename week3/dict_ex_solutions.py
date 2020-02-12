##############################################################
# dict_ex1.py
# Load people.tsv into a dictionary. Prompt user for filename

## populating a dictionary from a file
filename = input('What is the name of the file? ')
header = None
data_array = []

with open(filename, 'r') as fp:
    for line in fp:
        if header is None:
            header = line.strip().split('\t')
            continue

        data_array.append(dict(zip(header, line.strip().split('\t'))))

from pprint import pprint
pprint(data_array)