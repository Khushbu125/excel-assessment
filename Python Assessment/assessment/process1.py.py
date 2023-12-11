import pandas as pd
import argparse
import pyarrow.parquet
from datetime import datetime, timedelta
import os

def extract_trips(input_file, output_dir):
    # Read Parquet file
    df = pd.read_parquet("test_data.parquet")

    # Sort data by unit and timestamp
    df.sort_values(['unit', 'timestamp'], inplace=True)

    for unit, unit_data in df.groupby('unit'):
        trip_number = 0
        trip_data = []

        for index, row in unit_data.iterrows():
            if not trip_data or (row['timestamp'] - trip_data[-1]['timestamp']).total_seconds() > 7 * 3600:
                # Start a new trip
                trip_number += 1
                trip_data = []

            trip_data.append({
                'latitude': row['latitude'],
                'longitude': row['longitude'],
                'timestamp': row['timestamp']
            })

            # Save trip to CSV
            trip_df = pd.DataFrame(trip_data)
            trip_filename = f"{unit}_{trip_number}.csv"
            trip_filepath = os.path.join(output_dir, trip_filename)
            trip_df.to_csv(trip_filepath, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract trips from GPS data in a Parquet file.")
    parser.add_argument("--to_process", required=True, help="Path to the Parquet file to be processed.")
    parser.add_argument("--output_dir", required=True, help="Folder to store the resulting CSV files.")
    args = parser.parse_args()

    extract_trips("process1","output")

