"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(frame):
 
    frame.dropna(inplace=True)
    frame.columns = frame.columns.str.strip()
    frame = frame[frame['MIN'] > 0]

    return frame

def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv("cleanbrogdonstats.csv")
    frame = cleanStats(frame)
    HoopStatsView(frame)

if __name__ == "__main__":
    main()
