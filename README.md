### **Web Scraper for Trustpilot Reviews**

This project is an asynchronous web scraping application to extract reviews from Trustpilot using their public API. The scraper fetches reviews for specified businesses, normalizes the data into a structured format, and saves the output in JSON and CSV files.

---

## **Features**

- Asynchronous scraping using `httpx` and `asyncio` for efficiency.
- API URL extraction from Trustpilot's HTML using `parsel`.
- Pagination support to scrape multiple pages of reviews.
- Data normalization with `pandas` for structured output.
- Saves data in **JSON** and **CSV** formats for easy analysis.
- Modular design for scalability and maintainability.

---

## **Project Structure**

```
web_scraper/
├── main.py                 # Entry point
├── scraping/
│   ├── __init__.py         # Package initializer
│   ├── api_utils.py        # API utility functions
│   ├── scraper.py          # Scraping logic
├── data_processing/
│   ├── __init__.py         # Package initializer
│   ├── transform.py        # Data transformation
│   ├── persistence.py      # Data saving utilities
├── config/
│   ├── settings.py         # Configuration constants
├── requirements.txt        # Dependencies
├── README.md               # Documentation
└── Dockerfile              # Docker setup
```

---

## **Setup and Installation**

### **1. Clone the repository**

```bash
git clone https://github.com/your-username/web_scraper.git
cd web_scraper
```

### **2. Install dependencies**

Make sure you have Python 3.8+ installed. Install required packages:

```bash
pip install -r requirements.txt
```

### **3. Run the scraper**

Run the scraper to fetch reviews:

```bash
python main.py
```

---

## **How It Works**

### **Modules**

1. **`scraping/api_utils.py`**:

   - Extracts the API URL for Trustpilot reviews from a business's web page.

2. **`scraping/scraper.py`**:

   - Handles review scraping for single or multiple URLs.
   - Supports pagination to fetch reviews from multiple pages.

3. **`data_processing/transform.py`**:

   - Converts the raw JSON data into a `pandas.DataFrame` for analysis.

4. **`data_processing/persistence.py`**:

   - Saves data into JSON and CSV formats.

5. **`config/settings.py`**:

   - Stores configuration constants like headers and maximum pages to scrape.

6. **`main.py`**:
   - Entry point for the application. Orchestrates scraping and saving data.

---

## **Output**

- **JSON File**: Contains all scraped reviews in a raw format (`companies_data.json`).
- **CSV Files**: One CSV file per URL, storing structured reviews data (e.g., `coursera.org_reviews.csv`).

---

## **Customization**

- **URLs**: Update the `urls` list in `main.py` to specify the businesses you want to scrape.
- **Max Pages**: Adjust the `max_pages` parameter in the `run` function to limit the number of pages scraped.
- **Headers**: Modify the request headers in `config/settings.py` if needed.

---

## **Dependencies**

The project uses the following libraries:

- **`httpx`**: For asynchronous HTTP requests.
- **`asyncio`**: For managing asynchronous tasks.
- **`parsel`**: For HTML parsing and data extraction.
- **`pandas`**: For data transformation and normalization.
- **`json`**: For handling raw JSON data.

Install all dependencies using `requirements.txt`.

---

## **Testing**

To ensure all components work as expected, implement unit and integration tests in the `tests/` directory.

---

## **Future Enhancements**

- Add support for proxy rotation and user-agent randomization.
- Implement retries with exponential backoff for better fault tolerance.
- Integrate database support (e.g., PostgreSQL or MongoDB) for storing reviews.
- Create a REST API using FastAPI to access scraped data programmatically.

---

## **Contributing**

Feel free to contribute to this project by:

- Reporting bugs
- Suggesting new features
- Submitting pull requests

---

## **License**

This project is licensed under the [MIT License](LICENSE).

---

## **Contact**

For questions or support, contact [your-email@example.com].
