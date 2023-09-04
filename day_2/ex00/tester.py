import sys
from load_csv import load
import matplotlib.pyplot as plt

def main():
    if len(sys.argv) < 2:
        print("Usage: python tester.py <path_to_database>")
        sys.exit(1)
    try:
        db = load(sys.argv[1])
        num_rows, num_columns = db.shape
        print(f"Loading dataset of dimensions ({num_rows}, {num_columns})")
        print(db.head(3))
    except FileNotFoundError as e:
        print(e)
    except PermissionError:
        print("You don't have permission to open the file")
    except Exception as e:
        print("An error occurred:", e)
    


if __name__ == "__main__":
    main()