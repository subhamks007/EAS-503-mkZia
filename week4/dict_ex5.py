######################################################
# dict_ex5.py
# Simulate two dice. Print the total, theoretical/expected probability, and simulated probability
# input: the number of simulations
# https://socratic.org/questions/what-is-the-expected-value-of-the-sum-of-two-rolls-of-a-six-sided-die
# Total     Simulated Percent     Expected Percent 

# 2                      2.76                 2.78
# 3                      5.57                 5.56
# 4                      8.34                 8.33
# 5                      11.1                11.11
# 6                     13.83                13.89
# 7                     16.68                16.67
# 8                      13.9                13.89
# 9                      11.1                11.11
# 10                     8.36                 8.33
# 11                     5.57                 5.56
# 12                     2.79                 2.78


import random

def simulate_two_dice(no_simulations):

	sim_dict = {}
	for no in range(no_simulations):
		dice1 = random.randint(1,6)
		dice2 = random.randint(1,6)

		total = dice1 + dice2

		if total not in sim_dict:
			sim_dict[total] = 0

		sim_dict[total] += 1

	return sim_dict

from pprint import pprint
pprint(simulate_two_dice(1000))