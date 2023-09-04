import datetime as date
import time as time


# datetime module is suitable for working with
# date and time together,
# including date arithmetic and formatting.

# time module is focused on time-specific operations
# and is often used for timing and measuring elapsed time intervals.

sinceEpoch = time.time()

print("Seconds passed since January 1, 1970:", end=" ")
print(sinceEpoch, "or", "{:.2e}".format(sinceEpoch), end=" ")
print("in scientific notation")
print(date.date.today().strftime("%b %d %Y"))
