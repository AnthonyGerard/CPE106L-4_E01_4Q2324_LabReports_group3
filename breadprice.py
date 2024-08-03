import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('breadprice.csv', index_col=0)

# Cleaning the data in csv by converting index to a datetime object
data.index = pd.to_datetime(data.index)
years = data.index

plt.figure(figsize=(15, 5))
plt.plot(years, data.mean(axis=1))
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.title('Average Bread Price For Each Year')
plt.grid(True)
plt.show()
