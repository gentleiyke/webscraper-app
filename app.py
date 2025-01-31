import streamlit as st
import asyncio
import json
from scraping.scraper import scrape_multiple_urls
from data_processing.transform import reviews_to_dataframe
from data_processing.persistence import save_to_json

# Custom CSS
custom_css = """
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #00b67a;
        color: #191919;
    }
    .stApp {
        max-width: 1000px;
        margin: 0 auto;
    }
    .description {
        text-align: justify;
        font-size: 16px;
        margin-bottom: 20px;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #191919;
        border: 1px solid #e5e5e5;
    }
    .stButton > button {
        background-color: #00b67a;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 4px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #00a86b;
    }
    .footer {
        text-align: justify;
        margin-top: 40px;
        font-size: 14px;
        color: #6c757d;
    }
</style>
"""

# Add custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Initialize session state variables
if "scraped_data" not in st.session_state:
    st.session_state.scraped_data = None
if "dataframes" not in st.session_state:
    st.session_state.dataframes = {}

# Streamlit UI
st.title("Company Reviews Scraper")
st.markdown("<p class='description'>This is a simple web app to scrape customer's reviews from Trustpilot. Enter company's Trustpilot URLs (one per line) and the maximum number of pages to scrape is 50.</p>", unsafe_allow_html=True)

# User Input Section
urls = st.text_area("Enter Trustpilot URLs (one per line)", placeholder="https://www.trustpilot.com/review/company-name", height=150)
max_pages = st.number_input("Number of Pages to Scrape (50 Max)", min_value=1, max_value=50, value=10)

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

            # Save data to session state
            st.session_state.scraped_data = companies_data

            # Process the data into DataFrames
            url_to_df = reviews_to_dataframe(companies_data)
            st.session_state.dataframes = url_to_df

            st.success("Scraping completed! Data Ready!!")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter at least one URL.")

# Display and download data if it exists in session state
if st.session_state.scraped_data:
    # Provide JSON download option
    json_data = json.dumps(st.session_state.scraped_data, indent=2).encode('utf-8')
    st.download_button(
        label="Download All Data as JSON",
        data=json_data,
        file_name="companies_data.json",
        mime="application/json",
    )

    # Display results for each URL
    for url, df in st.session_state.dataframes.items():
        st.subheader(f"Scraped URL: {url}")
        st.dataframe(df.head())

        # CSV download option
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
    <div class='footer' style="margin-top: 50px; padding: 20px; background-color: #f1f1f1; border-radius: 4px;">
        <p><strong>Note:</strong> This app uses Trustpilot's public API and may be subject to rate limits or restrictions. Use responsibly.</p>
        <p><strong>Disclaimer:</strong> Only web scrape publicly available data and website terms of service and use APIs where available.</p>
    </div>
    """,
    unsafe_allow_html=True,
)