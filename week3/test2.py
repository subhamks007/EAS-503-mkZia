##############################################################
# dict_ex1.py
# Load people.tsv into a dictionary. 
# Prompt user for filename

filename = 'people.tsv'

with open(filename) as file:
	header = None
	for line in file:
		line = line.strip()
		if header is None:
			header = line.split('\t')
		


