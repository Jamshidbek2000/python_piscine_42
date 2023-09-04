
from time import sleep
from tqdm import tqdm
import shutil


def ft_tqdm(lst: range) -> None:
    print("List:", lst)
    total = len(lst)  # Get the total number of items in the range
    for item in lst:
        yield item  # Yield the current item in the range
        # Calculate and display progress bar
        progress = (item + 1) / total
        bar_length = shutil.get_terminal_size().columns - 30
        bar = "█" * int(bar_length * progress)
        spaces = " " * (bar_length - len(bar))
        print(f"{progress * 100:.0f}%[{bar}{spaces}]\
            {int(item + 1)}/{total}", end="\r")
    print()  # Print a newline at the end to clear the progress bar


for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()
