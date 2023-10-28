from Functions.data_collection import extract_data
from Functions.data_calculation import calculate_mean
from Functions.input import ask_user_for_input

import matplotlib.pyplot as plt

#Obtain the Ticker Symbol and Gather data
data = ask_user_for_input()

#Calculate SMA
sma_50 = calculate_mean(data , 50)
sma_200 = calculate_mean(data, 200)
#print(sma_50 , sma_200)


data['Signal'] = sma_50 - sma_200
print(data['Signal'])

data['Position'] = data['Signal'].apply(lambda x: 1 if x > 0 else -1 if x < 0 else 0)
data['Crossover'] = data['Position'].diff()

plt.figure(figsize=(14, 7))
data['adjclose'].plot(label='Adj Close')
sma_50.plot(label='50-day SMA', color='red')
sma_200.plot(label='200-day SMA', color='blue')

# Highlight golden crosses with green dots
plt.plot(data[data['Crossover'] == 2].index, sma_50[data['Crossover'] == 2], '^', markersize=10, color='g', lw=0, label='Golden Cross')

# Highlight death crosses with red dots
plt.plot(data[data['Crossover'] == -2].index, sma_50[data['Crossover'] == -2], 'v', markersize=10, color='r', lw=0, label='Death Cross')

#Show Plot
plt.title('Apple Inc. - SMA Crossover Trading Signals')
plt.legend(loc='best')
plt.show()
