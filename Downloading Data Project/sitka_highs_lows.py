"""Import the high and low temperatures from Sitka, Alaska in 2021."""

import csv
from datetime import datetime

import matplotlib.pyplot as plt

FILENAME = "data/sitka_weather_2021_simple.csv"
with open(FILENAME, encoding="utf-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high/low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

print(f"Highs: {highs}")
print(f"Dates: {dates}")

# Plot the high and low temperatures.
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot.
ax.set_title("Daily high and low temperatures, - 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()
