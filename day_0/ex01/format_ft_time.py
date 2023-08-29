import datetime as date
import time as time

sinceEpoch = time.time()

print("Seconds passed since January 1, 1970:", end=" ")
print(sinceEpoch, "or", "{:.2e}".format(sinceEpoch), end=" ")
print("in scientific notation")
print(date.date.today().strftime("%b-%d-%y"))
