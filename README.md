# 📰 LinkedIn Feeds Scraper with Crawlbase

## 📝 Description

This repository provides a Python-based solution to extract data from public LinkedIn feed posts using the [Crawlbase Crawling API](https://crawlbase.com/crawling-api-avoid-captchas-blocks).

It includes:

- A feed scraper that sends an asynchronous request to a LinkedIn post.
- A retrieval script that fetches the final structured post data using the request ID (RID).

📖 Read the full tutorial: [How to Scrape LinkedIn](https://crawlbase.com/blog/how-to-scrape-linkedin/)

## 🔧 Tools Used

- [`crawlbase`](https://pypi.org/project/crawlbase/) – for using Crawling and Storage APIs
- `json` – for working with structured data
- `Python 3.6+`

## 📦 Installation

Install the required Python package:

```bash
pip install crawlbase
```

## 🚀 Scraper: LinkedIn Feed Post Scraper

**File:** `linkedin_feed_scraper.py`

### ✅ What It Does

- Sends an asynchronous request to a public LinkedIn feed post.
- Returns a `rid` (request ID) used to retrieve the final data.

### ⚙️ How to Run

1. Replace `YOUR_API_TOKEN` with your Crawlbase token.
2. Set the LinkedIn feed post `URL`.

```bash
python linkedin_feed_scraper.py
```

### 🧪 Sample Output

```json
{
	"rid": "977b3381ab11f938d6522775"
}
```

## 📄 Retrieval: Get Feed Data

**File:** `linkedin_feed_retrieve.py`

### ✅ What It Does

- Uses the rid from the previous script to fetch and print the full post data.

### ⚙️ How to Run

- Replace `YOUR_API_TOKEN` and `RID` in the script.

```bash
python linkedin_feed_retrieve.py
```

### 🧪 Sample Output

```json
{
  "feeds": [
    {
      "text": "#AlphabetInc is eliminating 12,000 jobs, its chief executive said in a staff memo The cuts mark the latest to shake the #technology sector and come days after rival Microsoft Corp said it would lay off 10,000 workers. Full report - https://lnkd.in/dfxXc2N4",
      "images": [
        "https://media.licdn.com/dms/image/C4D22AQHvTzTp5mnMcg/feedshare-shrink_2048_1536/0/1674212335928?e=2147483647&v=beta&t=Aq3WKkxF1Q5ZwGB6ax6OOWRtCW7Vlz8KDdpBvvK4K_0"
      ],
      "videos": [],
      "datetime": "1y",
      "postUrl": "https://in.linkedin.com/company...",
      ...
    },
    ...
  ]
}
```

## 📌 To-Do

- Support for scraping multiple company pages
- Export company data to CSV/JSON
- Add CLI options for input/output
- Implement retry and error-handling logic

## 💡 Why Scrape LinkedIn Company Pages?

- Research competitors and market trends
- Monitor public-facing company updates
- Build datasets for lead generation and analytics
