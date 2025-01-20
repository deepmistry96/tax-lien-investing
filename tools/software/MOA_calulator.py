#! /usr/bin/python3
import argparse

# Set up argument parser
#parser = argparse.ArgumentParser(description='Calculate max and min profit based on ARV')
#parser.add_argument('--arv', type=int, help='After Repair Value (ARV)', default=900000)

# Parse arguments
#args = parser.parse_args()
#ARV = args.arv
ARV = 198000

#basic variables
FMV = 280,000
repair_costs = 35000
wholesale_costs = (ARV * .20)
max_profit = .31
min_profit = .21 
anticipated_profit = min_profit

# updates
anticipated_profit = .20
repair_costs = 22000
ARV = 198000



# final multiplier
percentage_costs = .11 + .035 + .02 + anticipated_profit



print("For ARV of: {}".format(str(ARV)))


# anticipated_profit = max_profit
# print("Max profit percentage of {}% the MAO is: {}".format(str(max_profit*100), str(ARV - (ARV*anticipated_profit) - repair_costs - wholesale_costs)))

print("Min profit percentage of {}% the MAO is: {}".format(str(anticipated_profit*100), str(ARV - (ARV*percentage_costs) - repair_costs - wholesale_costs)))
