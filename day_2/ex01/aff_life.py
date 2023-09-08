from load_csv import load
import matplotlib.pyplot as plt
import sys


def main():
    """
    Load and visualize life expectancy data for Germany from a CSV file.

    This function loads a CSV file containing life expectancy data
    for different countries and visualizes the life expectancy projections
    specifically for Germany over the years.

    Command Line Usage:
        python load_csv.py <path_to_csv_file>

    Args:
        None

    Raises:
        ValueError:
        If command line is not provided with the expected number of arguments.
        FileNotFoundError:
        If the specified CSV file path does not exist.
        ValueError:
        If the loaded data does not contain the expected columns.
        Exception:
        Any other unhandled exceptions that might
        occur during data loading or plotting.
    """

    if len(sys.argv) != 2:
        print("Usage: python load_csv.py <path to csv file>")
        sys.exit(1)

    try:
        df = load(sys.argv[1])
        data_germany = df.query("country == 'Germany'")
        years = data_germany.columns[1:]

        # years, years with data on that year
        plt.plot(data_germany.columns[1:], data_germany.iloc[0, 1:])
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.xticks(years[::40], rotation=45)
        plt.title('Germany Life expectancy Projections')
        plt.grid()
        plt.show()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
