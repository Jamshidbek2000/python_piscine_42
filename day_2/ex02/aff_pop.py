from load_csv import load
import matplotlib.pyplot as plt
import sys

# Convert the values to numeric by handling 'M' and 'k' suffixes
def convert_value(value):
    if 'M' in value:
        return float(value[:-1]) * 1e6
    elif 'k' in value:
        return float(value[:-1]) * 1e3
    else:
        return float(value)

def main():
    if len(sys.argv) != 2:
        print("Usage: python load_csv.py <path to csv file>")
        sys.exit(1)

    try:
        country1 = 'Belgium'
        country2 = 'France'

# Load dataFrame from .csv file
        data_frame = load(sys.argv[1])

# Get data for Particular country
        country1_data = data_frame[data_frame['country'] == country1]
        country2_data = data_frame[data_frame['country'] == country2]

# Get years until 2050
        years = country2_data.columns[1:]
        years = [int(year) for year in years if int(year) < 2050]

        germany_population = country1_data.iloc[0, 1:251]
        uzbekistan_population = country2_data.iloc[0, 1:251]
        
        d1 = [convert_value(data) for data in germany_population]
        d2 = [convert_value(data) for data in uzbekistan_population]


        plt.plot(years, d1)
        plt.plot(years,d2)
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.title('Life Expectancy Over Years')

        plt.grid()
        plt.legend([country1, country2, 'ccc'])

        plt.show()

    except Exception as e:
            print(e)



if __name__ == "__main__":
    main()