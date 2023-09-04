from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import sys

def main():
    if len(sys.argv)!= 2:
        print("Usage: python load_csv.py <path to csv file>")
        sys.exit(1)
    
    df = load(sys.argv[1])
    # data_germany = df[df['country'] == 'Germany']
    data_germany = df.query("country == 'Germany'")
    years = data_germany.columns[1:]

    plt.plot(data_germany.columns[1:], data_germany.iloc[0, 1:])
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.xticks(years[::40], rotation=45)
    plt.title('Germany Life expectancy Projections')
    plt.grid()
    plt.show()






if __name__ == "__main__":
    main()