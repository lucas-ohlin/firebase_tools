from google.cloud import storage

### Downloads a file from Firebase Storage

def download_gcs_file(bucket_name, blob_name, file_name):
    try:
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)

        blob.download_to_filename(file_name)
        print(f"File {blob_name} downloaded to {file_name}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    bucket_name = "project_id.appspot.com" # Your project id / bucket name
    blob_name = "data/reports.json"        # Your file location
    file_name = "reports.json"             # Name to save too

    download_gcs_file(bucket_name, blob_name, file_name)
