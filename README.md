### **Web Scraper for Trustpilot Reviews**

This project is an asynchronous web scraping application to extract reviews from Trustpilot using their public API. The scraper fetches reviews for specified businesses, normalises the data into a structured format, and saves the output in JSON and CSV files which you can download.

---

## **Features**

- Asynchronous scraping using `httpx` and `asyncio` for efficiency.
- API URL extraction from Trustpilot's HTML using `parsel`.
- Pagination support to scrape multiple pages of reviews.
- Data normalisation with `pandas` for structured output.
- Saves data in **JSON** and **CSV** formats for easy analysis.

---

## **Project Structure**

```
web_scraper/
├── app.py                 # Streamlit App
├── scraping/
│   ├── api_utils.py        # API utility functions
│   ├── scraper.py          # Scraping logic
├── data_processing/
│   ├── transform.py        # Data transformation
│   ├── persistence.py      # Data saving utilities
├── config/
│   ├── settings.py         # Configuration constants
├── requirements.txt        # Dependencies
├── README.md               # Documentation
```

---

## **Modules**

1. **`scraping/api_utils.py`**:

   - Extracts the API URL for Trustpilot reviews from a business's web page.

2. **`scraping/scraper.py`**:

   - Handles review scraping for single or multiple URLs.
   - Supports pagination to fetch reviews from multiple pages.

3. **`data_processing/transform.py`**:

   - Normalise reviews JSON data
   - Converts the raw JSON data into a Pandas DataFrame for easy analysis.

4. **`data_processing/persistence.py`**:

   - Saves data into JSON and CSV formats.

5. **`config/settings.py`**:

   - Stores headers and maximum pages to scrape configuration constants.

6. **`app.py`**:
   - Streamlit app landing page.

---

## **Output**

- **JSON File**: Contains all scraped reviews in a raw JSON format.
- **CSV Files**: One CSV file per URL, storing structured reviews data.

---

## **Dependencies**

I used the following libraries this project:

- **`httpx[http2]`**: For asynchronous HTTP/2 requests.
- **`parsel`**: For HTML parsing and data extraction.
- **`pandas`**: For data transformation and normalization.
- **`json5`**: For reading and writing JSON files.
- **`streamlit`**: For creating an interactive web interface.

---

## **Contact**

For questions or collaborations, contact ikemefulaoriaku@gmail.com.
