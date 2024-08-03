import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean_data(file_path):
	df pd.read_csv(file_path)
  df = df.dropna(subset=["Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
  df[ 'Year'] df['Year'].astype(int)

	for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']: 
		df[month] = df[month].astype(float)

	return of

def plot average_price_per_year(df):
	df['Avg Price'] = df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']].mean(axis=1)
	avg price per year = df.groupby("Year')['Avg Price'].mean()

plt.figure(figsize=(10, 6))
plt.plot(avg_price_per_year.index, avg_price_per_year.values, marker='o')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.title('Average Price of Bread per Year')
plt.grid(True)
plt.show()

def main():
	file path = 'breadprice.csv |
	df load_and_clean_data(file path) 	plot_average_price_per_year(df)

if __name__ == "__main__": 
	main()
