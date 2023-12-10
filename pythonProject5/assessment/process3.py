import os
import json
import csv
import argparse

# Function to process JSON files and generate CSV
def process_json_files(json_folder, output_file):
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            ['unit', 'trip_id', 'toll_loc_id_start', 'toll_loc_id_end', 'toll_loc_name_start', 'toll_loc_name_end',
             'toll_system_type', 'entry_time', 'exit_time', 'tag_cost', 'cash_cost', 'license_plate_cost'])
        for json_file in os.listdir(json_folder):
            json_path = os.path.join(json_folder, json_file)
            with open(json_path, 'r') as file:
                try:
                    json_data = json.load(file)
                    if 'route' in json_data:
                        route_data = json_data['route']
                        if 'tolls' in route_data:
                            tolls_data = route_data['tolls']
                            for toll in tolls_data:
                                unit = json_data.get('unit', '')
                                trip_id = json_file[:-5]
                                toll_loc_id_start = toll.get('toll_loc_id_start', '')
                                toll_loc_id_end = toll.get('toll_loc_id_end', '')
                                toll_loc_name_start = toll.get('toll_loc_name_start', '')
                                toll_loc_name_end = toll.get('toll_loc_name_end', '')
                                toll_system_type = toll.get('toll_system_type', '')
                                entry_time = toll.get('entry_time', '')
                                exit_time = toll.get('exit_time', '')
                                tag_cost = toll.get('tag_cost', '')
                                cash_cost = toll.get('cash_cost', '')
                                license_plate_cost = toll.get('license_plate_cost', '')
                                writer.writerow([unit, trip_id, toll_loc_id_start, toll_loc_id_end, toll_loc_name_start,
                                                 toll_loc_name_end,
                                                 toll_system_type, entry_time, exit_time, tag_cost, cash_cost,
                                                 license_plate_cost])
                except json.JSONDecodeError:
                    print(f"Error processing JSON file: {json_file}")
    print(f"CSV file generated: {output_file}")

# Main function
def main():
    # Argument parser
    parser = argparse.ArgumentParser(description='Process toll information stored in JSON files')
    parser.add_argument('--to_process', required=True, help='Path to the JSON responses folder')
    parser.add_argument('--output_dir', required=True, help='Path to the output folder')
    # Parse command line arguments
    args = parser.parse_args()
    # Output file path
    output_file = os.path.join("output", 'transformed_data.csv')
    # Process JSON files and generate CSV
    process_json_files("process3", "output")

if __name__ == "__main__":
    main()