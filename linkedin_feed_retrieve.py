from crawlbase import StorageAPI
import json

# Initialize Crawlbase Storage API with your access token
storage_api = StorageAPI({ 'token': 'YOUR_API_TOKEN' })

RID = 'your_request_identifier'

# Function to retrieve data from Crawlbase storage
def retrieve_data(rid):
    response = storage_api.get(rid)
    if response['status_code'] == 200:
        return json.loads(response['body'].decode('latin1'))
    else:
        print("Failed to retrieve the data. Status code:", response['status_code'])
        return None

if __name__ == '__main__':
    retrieved_data = retrieve_data(RID)
    print(json.dumps(retrieved_data, indent=2))