import streamlit as st
import asyncio
from scraping.scraper import scrape_multiple_urls
from data_processing.transform import reviews_to_dataframe
from data_processing.persistence import save_to_json, save_to_csv
import pandas as pd
import json
import streamlit.components.v1 as components

# Custom CSS and HTML for Trustpilot-themed design
trustpilot_css = """
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f8f9fa; /* Light gray */
        color: #4b515d; /* Dark gray */
    }
    .main-title {
        text-align: center;
        color: #00b67a; /* Trustpilot green */
        margin-top: 20px;
    }
    .description {
        text-align: center;
        margin-bottom: 20px;
    }
    .box {
        background-color: #ffffff;
        border: 1px solid #d3d3d3;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .button {
        background-color: #00b67a;
        color: #ffffff;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
        display: inline-block;
    }
    .button:hover {
        background-color: #007f56;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 12px;
        color: #6c757d;
    }
</style>
"""

# Include custom CSS
st.markdown(trustpilot_css, unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-title'>Trustpilot Reviews Scraper</h1>", unsafe_allow_html=True)

# Description
st.markdown("<p class='description'>This is a simple web app to scrape reviews from Trustpilot.</p>", unsafe_allow_html=True)

# User Input Section
st.markdown("<div class='box'>", unsafe_allow_html=True)
urls = st.text_area("Enter Trustpilot URLs (one per line)", height=150)
max_pages = st.number_input("Number of Pages to Scrape (50 Max)", min_value=1, max_value=50, value=10)
st.markdown("</div>", unsafe_allow_html=True)

# Scraping Button
if st.button("Start Scraping"):
    if urls.strip():
        # Convert URLs to a list
        url_list = urls.splitlines()

        # Inform the user scraping is in progress
        st.write("<p class='description'>Scraping reviews... Please wait.</p>", unsafe_allow_html=True)

        try:
            # Run the scraper asynchronously
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            companies_data = loop.run_until_complete(scrape_multiple_urls(url_list, max_pages=max_pages))

            # Save the reviews data to a JSON file
            save_to_json(companies_data, "companies_data.json")
            st.success("Scraping completed! Data Ready!!")

            # Provide JSON download option
            json_data = json.dumps(companies_data, indent=2).encode('utf-8')
            st.download_button(
                label="Download All Data as JSON",
                data=json_data,
                file_name="companies_data.json",
                mime="application/json",
            )

            # Convert reviews to DataFrames
            url_to_df = reviews_to_dataframe(companies_data)

            # Display results for each URL
            for url, df in url_to_df.items():
                st.markdown(f"<h2 class='main-title'>Results for {url}</h2>", unsafe_allow_html=True)
                st.dataframe(df.head())

                # Provide CSV download option
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

# Footer
st.markdown(
    """
    <div class='footer'>
        ---
        <p>**Note:** This app uses Trustpilot's public API and may be subject to rate limits or restrictions.</p>
        <p><b>Disclaimer:</b> Only web scrape publicly available data and website terms of service and use APIs where available.</p>
    </div>
    """,
    unsafe_allow_html=True,
)