import streamlit as st
import asyncio
from scraping.scraper import scrape_multiple_urls
from data_processing.transform import reviews_to_dataframe
from data_processing.persistence import save_to_json
import pandas as pd
import json

# Streamlit UI
st.title("Trustpilot Reviews Scraper")
st.markdown("This is a simple web app to scrape reviews from Trustpilot.")
st.markdown("Enter Trustpilot URLs (one per line) and the maximum number of pages to scrape is 50.")

# Initialize session state
if "scraped_data" not in st.session_state:
    st.session_state.scraped_data = None

# User Input Section
urls = st.text_area("Enter Trustpilot URLs (one per line)", height=150)
max_pages = st.number_input("Maximum Pages to Scrape", min_value=1, max_value=50, value=10)

if st.button("Start Scraping"):
    if urls.strip():
        # Convert URLs to a list
        url_list = urls.splitlines()

        # Inform the user scraping is in progress
        st.write("Scraping reviews... Please wait.")

        try:
            # Run the scraper asynchronously
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            companies_data = loop.run_until_complete(scrape_multiple_urls(url_list, max_pages=max_pages))

            # Save the data in session state
            st.session_state.scraped_data = companies_data

            # Save the reviews data to a JSON file
            save_to_json(companies_data, "companies_data.json")
            st.success("Scraping completed! Data Ready!!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter at least one URL.")

# Display and download data if available
if st.session_state.scraped_data:
    companies_data = st.session_state.scraped_data

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
        st.subheader(f"Results for {url}")
        st.dataframe(df.head())

        # Provide CSV download option
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label=f"Download CSV for {url.split('/')[-1]}",
            data=csv,
            file_name=f"{url.split('/')[-1]}_reviews.csv",
            mime="text/csv",
        )

# Footer
st.markdown(
    """
    ---
    **Note:** This app uses Trustpilot's public API and may be subject to rate limits or restrictions. 
    Use responsibly.
    **Disclaimer:** Only web scrape publicly available data and website terms of service and use APIs where available.
    """
)
