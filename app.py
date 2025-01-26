import streamlit as st
import streamlit.components.v1 as components
import asyncio
from scraping.scraper import scrape_multiple_urls
from data_processing.transform import reviews_to_dataframe
from data_processing.persistence import save_to_json, save_to_csv
import pandas as pd
import json

# Add Custom HTML and CSS
custom_css = """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f8f9fa;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            text-align: center;
            padding: 20px;
            background-color: #00b67a;
            color: #ffffff;
            border-radius: 10px;
        }
        .header h1 {
            margin: 0;
            font-size: 2.5rem;
        }
        .section {
            background: #ffffff;
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            font-size: 1rem;
            color: #ffffff;
            background-color: #00b67a;
            border: none;
            border-radius: 5px;
            text-decoration: none;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #008856;
        }
    </style>
"""

# Inject the CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

# Create the HTML structure
html_structure = """
<div class="container">
    <div class="header">
        <h1>Trustpilot Reviews Scraper</h1>
        <p>Scrape and download reviews from Trustpilot in just a few clicks!</p>
    </div>
    <div class="section">
        <h2>Enter URLs and Scrape Options</h2>
        <p>Provide the Trustpilot URLs (one per line) and specify the maximum number of pages to scrape.</p>
    </div>
</div>
"""

# Render the HTML structure
components.html(html_structure, height=300)

# Streamlit UI for input
urls = st.text_area("Enter Trustpilot URLs (one per line)", height=150)
max_pages = st.number_input("Maximum Pages to Scrape", min_value=1, max_value=50, value=10)

if st.button("Start Scraping"):
    if urls.strip():
        url_list = urls.splitlines()
        st.write("Scraping reviews... Please wait.")
        try:
            # Asynchronous scraping logic
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            companies_data = loop.run_until_complete(scrape_multiple_urls(url_list, max_pages=max_pages))

            save_to_json(companies_data, "companies_data.json")
            st.success("Scraping completed! Data ready.")

            json_data = json.dumps(companies_data, indent=2).encode('utf-8')
            st.download_button(
                label="Download All Data as JSON",
                data=json_data,
                file_name="companies_data.json",
                mime="application/json",
            )

            url_to_df = reviews_to_dataframe(companies_data)
            for url, df in url_to_df.items():
                st.subheader(f"Results for {url}")
                st.dataframe(df.head())

                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label=f"Download CSV for {url.split('/')[-1]}",
                    data=csv,
                    file_name=f"{url.split('/')[-1]}_reviews.csv",
                    mime="text/csv",
                )
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter at least one URL.")
