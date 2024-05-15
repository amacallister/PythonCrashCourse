"""Import the high and low temperatures from Death Valley in 2021."""

import csv
from datetime import datetime

import matplotlib.pyplot as plt

FILENAME = "data/death_valley_2021_simple.csv"
with open(FILENAME, encoding="utf-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high/low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot.
TITLE = "Daily high and low temperatures, - 2021\nDeath Valley, CA"
ax.set_title(TITLE, fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()
