#! /usr/bin/python3

ARV = 900000
repair_costs = 35000
wholesale_costs = 20000

transaction_multiplier = .11

max_profit = .31
min_profit = .21 

anticipated_profit = max_profit



print( "max profit:" + str(ARV - (ARV*anticipated_profit) - repair_costs - wholesale_costs))


anticipated_profit = min_profit

print( "min profit:" + str(ARV - (ARV*anticipated_profit) - (ARV * transaction_multiplier) - repair_costs - wholesale_costs ))