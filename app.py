import streamlit as st
import asyncio
from scraping.scraper import scrape_multiple_urls
from data_processing.transform import reviews_to_dataframe
from data_processing.persistence import save_to_json, save_to_csv
import pandas as pd
import json

# Initialize session state variables
if "scraping_in_progress" not in st.session_state:
    st.session_state.scraping_in_progress = False
if "scrape_button_text" not in st.session_state:
    st.session_state.scrape_button_text = "Start Scraping"

# Streamlit UI
st.title("Trustpilot Reviews Scraper")
st.markdown("This is a simple web app to scrape reviews from Trustpilot.")
st.markdown("Enter Trustpilot URLs (one per line) and the maximum number of pages to scrape is 50.")

# User Input Section
urls = st.text_area("Enter Trustpilot URLs (one per line)", height=150)
max_pages = st.number_input("Maximum Pages to Scrape", min_value=1, max_value=50, value=10)

# Button callback function
def start_scraping():
    st.session_state.scraping_in_progress = True
    st.session_state.scrape_button_text = "Scrape Another"

def reset_session():
    st.session_state.scraping_in_progress = False
    st.session_state.scrape_button_text = "Start Scraping"

# Scraping button
if st.button(st.session_state.scrape_button_text):
    if st.session_state.scraping_in_progress:
        reset_session()  # Reset session if "Scrape Another" is clicked
        st.experimental_rerun()
    else:
        start_scraping()  # Start scraping process

# Scraping process
if st.session_state.scraping_in_progress:
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
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter at least one URL.")
                
# Footer
st.markdown(
    """
    ---
    **Note:** This app uses Trustpilot's public API and may be subject to rate limits or restrictions. 
    Use responsibly.
    **Disclaimer:** Only web scrape publicly available data and website terms of service and use APIs where available.
    """
)
