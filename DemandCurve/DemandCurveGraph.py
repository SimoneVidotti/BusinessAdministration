import matplotlib.pyplot as plt
import numpy as np

# demand function (example: Q = 100 - 2P), P = price
def demand_function(p):
    F = 80 - (10/3) # example, replace this with your demand function
    return F * p # function * price

# Title print
print('\n', 'DEMAND CURVE GRAPH\n')

# Price (example: 20)
price = float(input('(Price)>  '))

# Array for prices from 0 to 50, modify this if you want set your prices
prices = np.arange(0, 100, 0.1) # random

# Calc Q for all prices
quantities = [demand_function(p) for p in prices] 

# Graph create
plt.plot(prices, quantities, linestyle='-', color='red')
plt.xlabel('Price')
plt.ylabel('Quantities')
plt.title('Demand curve')
plt.grid(True)
plt.show()