import os
import requests
# import dotenv
#
# # Load environment variables from .env file
# load_dotenv()

# API configuration
api_key = os.getenv('TOLLGURU_API_KEY')
api_url = os.getenv('TOLLGURU_API_URL')


# Function to upload GPS track CSV and get toll information
def upload_gps_track(csv_path):
    url = f"https://apis.tollguru.com/toll/v2/gps-tracks-csv-upload?mapProvider=osrm&vehicleType=5AxlesTruck/toll/v2/gps-tracks-csv-upload"
    params = {
        "vehicleType": "5AxlesTruck",
        "mapProvider": "osrm"
    }
    headers = {
        "Content-Type": "text/csv",
        "x-api-key": "pFtFN69ptBQHr3jgDBTQ4QqhFLddhpLH"
    }

    with open(csv_path, 'rb') as file:
        response = requests.post(url, params=params, data=file, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None


# Process CSV files
def process_csv_files(csv_folder, output_folder):
    csv_files = os.listdir(csv_folder)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for csv_file in csv_files:
        csv_path = os.path.join(csv_folder, csv_file)
        json_response = upload_gps_track(csv_path)
        if json_response:
            output_path = os.path.join(output_folder, f"{csv_file}.json")
            with open(output_path, 'w') as output_file:
                output_file.write(json_response)
                print(f"Successfully processed: {csv_file}")
        else:
            print(f"Failed to process: {csv_file}")


# Main function
def main():
    import argparse

    # Argument parser
    parser = argparse.ArgumentParser(description='Process CSV files and interact with TollGuru API')
    parser.add_argument('--to_process', required=True, help='Path to the CSV folder')
    parser.add_argument('--output_dir', required=True, help='Path to the output folder')

    # Parse command line arguments
    args = parser.parse_args()

    # Process CSV files
    process_csv_files("process2","output")




if __name__ == "__main__":
    main()

