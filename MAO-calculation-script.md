#reference-and-tools

ARV subtracted by:
- repair costs  (variable)
- legal fees (~ 1%)
- holding costs (~ 3%)
- sales costs (~ 3%)
- anticipated profit (~ 10%-20%)
- "fudge" factor (~ 4%)
- wholesale margin (5k+)

```
ARV = 900000
repair_costs = 35000
wholesale_costs = 20000

transaction_multiplier = .11

max_profit = .31
min_profit = .21 

anticipated_profit = max_profit



print( "max profit:" + str(ARV - (ARV*anticipated_profit) - repair_costs - wholesale_costs))


anticipated_profit = min_profit

print( "min profit:" + str(ARV - (ARV*anticipated_profit) - repair_costs - wholesale_costs - (ARV * transaction_multiplier))




```