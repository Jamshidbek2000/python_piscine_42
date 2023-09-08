from load_csv import load
import matplotlib.pyplot as plt
import sys


def convert_value(value):
    """
    Convert a string representing a numerical value with
    'M' (millions) or 'k' (thousands) suffix to a float.

    Args:
        value (str): The string value to convert.

    Returns:
        float: The numerical value as a float.
    """
    if 'M' in value:
        return float(value[:-1]) * 1e6
    elif 'k' in value:
        return float(value[:-1]) * 1e3
    else:
        return float(value)


def round_int(num, to) -> int:
    """
    Round a number to the nearest multiple of a specified value.

    Args:
        num (float): The number to be rounded.
        to (int): The value to which the number should be rounded.

    Returns:
        int: The rounded integer value.
    """
    return round(num / to) * to


def generate_ticks(min, max, num_of_ticks) -> list:
    """
    Generate a list of evenly spaced tick values within a specified range.

    Args:
        min (float): The minimum value of the range.
        max (float): The maximum value of the range.
        num_of_ticks (int): The number of tick values to generate.

    Returns:
        list: A list of tick values.
    """
    result = []

    min = int(min)
    max = int(max)

    diff = max - min
    len_of_tick = diff // num_of_ticks
    zeros = len(str(min))

    for i in range(num_of_ticks):
        result.append(round_int(min + i * len_of_tick, 10 ** zeros))

    result.append(round_int(max, 10 ** zeros))
    result = list(dict.fromkeys(result))
    return result


def main():
    """
    Main function to load CSV data,
    process it,
    and create a plot of life expectancy over years for two countries.
    """
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

        country1_population = country1_data.iloc[0, 1:251]
        country2_population = country2_data.iloc[0, 1:251]

        d1 = [convert_value(data) for data in country1_population]
        d2 = [convert_value(data) for data in country2_population]

        plt.plot(years, d1)
        plt.plot(years, d2)
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.title('Life Expectancy Over Years')

        plt.grid()
        plt.legend([country1, country2, 'ccc'])

        max_pop = int(max(max(d1), max(d2)))
        min_pop = int(min(min(d1), min(d2)))

        ticks = generate_ticks(min_pop, max_pop, 8)
        formatt = [str(int((pop / (10 ** (len(str(min_pop)) - 1)))))
                   + "M" for pop in ticks]

        plt.yticks(ticks, formatt)
        plt.show()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
