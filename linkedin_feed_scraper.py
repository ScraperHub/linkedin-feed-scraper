from crawlbase import CrawlingAPI
import json

# Initialize Crawlbase API with your access token
crawling_api = CrawlingAPI({ 'token': 'YOUR_API_TOKEN' })

URL = 'https://www.linkedin.com/feed/update/urn:li:activity:7022155503770251267'

options = {
    'scraper': 'linkedin-feed',
    'async': 'true'
}

# Function to make a request using Crawlbase API
def make_crawlbase_request(url):
    response = crawling_api.get(url, options)
    if response['status_code'] == 200:
        return json.loads(response['body'].decode('latin1'))
    else:
        print("Failed to fetch the page. Status code:", response['status_code'])
        return None

def scrape_feed(url):
    try:
        json_response = make_crawlbase_request(url)
        if json_response:
            return json_response
    except Exception as e:
        print(f"Request failed: {e}")

    return None

if __name__ == '__main__':
    scraped_data = scrape_feed(URL)
    print(json.dumps(scraped_data, indent=2))