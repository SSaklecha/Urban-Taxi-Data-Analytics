import requests
import pandas as pd
from google.cloud import storage
from datetime import datetime

def get_data(request):
    """
    HTTP-triggered Cloud Function that fetches NYC taxi data,
    converts it to a Parquet file with a filename that includes the current month and year,
    and uploads it to a Google Cloud Storage bucket.
    """
    # Define the API endpoint and parameters.
    api_url = "https://data.cityofnewyork.us/resource/2upf-qytp.json"
    params = {
        '$limit': 5000,  # Adjust as needed; implement pagination for larger datasets.
    }

    # Fetch data from the NYC Open Data API.
    response = requests.get(api_url, params=params)
    if response.status_code != 200:
        return f"Error fetching data: {response.status_code}", 500
    data = response.json()

    # Convert JSON data to a pandas DataFrame.
    df = pd.DataFrame(data)

    # Get current month and year for the filename.
    now = datetime.now()
    month_year = now.strftime("%Y_%m")
    local_filename = f"/tmp/yellow_taxi_data_{month_year}.parquet"
    
    # Save the DataFrame to a Parquet file using PyArrow.
    df.to_parquet(local_filename, engine='pyarrow')

    # Set your Google Cloud Storage bucket name.
    bucket_name = "YOUR_BUCKET_NAME"  # Replace with your actual bucket name.

    # Initialize a Cloud Storage client.
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    
    # Define the blob name using the same month-year format.
    blob = bucket.blob(f"yellow_taxi_data_{month_year}.parquet")
    blob.upload_from_filename(local_filename)

    return f"Successfully uploaded {local_filename} to bucket {bucket_name}.", 200
