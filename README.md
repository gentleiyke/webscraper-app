### **Web Scraper for Trustpilot Reviews**

In this project, I built an asynchronous web scraping application that can be used to extract reviews from Trustpilot using their public API, the scraper efficiently retrieves reviews for specified businesses, processes the data into a structured format, and allows you to download the output in JSON and CSV formats. This project is designed to make extracting, processing, and analysing Trustpilot reviews simple and efficient and will welcome feedbacks.

---

## **Features**

- Asynchronous Scraping: Leveraged `httpx` and `asyncio` for high-performance data retrieval.
- Dynamic API URL Extraction: Extracts review API URLs from Trustpilot's HTML using `parsel`.
- Pagination Support: Handles multiple pages of reviews to ensure comprehensive scraping.
- Data Normalisation: Processes raw data into structured formats using `pandas`.
- Saves data in **JSON** and **CSV** formats for easy analysis.
- Multi-Format Output: Saves scraped data as `JSON` (raw data) and `CSV` (structured data).
- Interactive Interface: Built with `Streamlit` for user-friendly interaction.

---

## **Project Structure**

```
web_scraper/
├── app.py                 # Streamlit App
├── scraping/
│   ├── api_utils.py        # API utility functions
│   ├── scraper.py          # Scraping logic
├── data_processing/
│   ├── transform.py        # Data transformation utilities
│   ├── persistence.py      # Data saving utilities
├── config/
│   ├── settings.py         # Configuration constants
├── requirements.txt        # Project dependencies
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
   - Interactive user interface for scraping, processing, and downloading review data.

Live Demo: https://webscraper-app.streamlit.app/

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

Install all dependencies using:

```
pip install -r requirements.txt
```

---

## **How to Use**

- **Clone the Repository**

```
git clone https://github.com/your-username/webscraper-app.git
cd webscraper-app
```

- **Install Dependencies**

```
pip install -r requirements.txt
```

- **Run the Streamlit App**

```
streamlit run app.py
```

- **Interact with the App**

  - Enter the Trustpilot URLs for businesses you want to scrape.
  - Specify the maximum number of review pages to scrape.
  - Download the output in JSON or CSV format.

---

**Use Cases**

- Customer Sentiment Analysis: Extract customer reviews to analyze sentiment and identify trends.
- Market Research: Gather feedback on competitors and market positioning.
- Product Improvement: Use structured feedback to enhance products and services.
- Data Enrichment: Generate datasets for machine learning or data science projects.

---

**Future Improvement Ideas**

- Add support for multi-language reviews.
- Integrate visualisation tools for in-app data analysis.

---

## **Contact**

For questions or collaborations, contact ikemefulaoriaku@gmail.com.
