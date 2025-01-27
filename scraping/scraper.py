from typing import List, Dict
import asyncio
import json
from scraping.api_utils import get_reviews_api_url
from httpx import AsyncClient

client = AsyncClient()

async def scrape_reviews(url: str, max_pages: int = 5) -> List[Dict]:
    """Parse review data from the Trustpilot API."""
    api_url = await get_reviews_api_url(url)

    first_page = await client.post(api_url)
    data = json.loads(first_page.text)["pageProps"]
    reviews_data = data["reviews"]
    
    total_pages = data["filters"]["pagination"]["totalPages"]
    if max_pages and max_pages < total_pages:
        total_pages = max_pages

    other_pages = [client.post(api_url + f"&page={page_number}") for page_number in range(2, total_pages + 1)]
    
    for response in asyncio.as_completed(other_pages):
        response = await response
        assert response.status_code == 200, "Request was blocked"
        page_data = json.loads(response.text)["pageProps"]["reviews"]
        reviews_data.extend(page_data)

    return reviews_data

async def scrape_multiple_urls(urls: List[str], max_pages: int = 5) -> List[Dict]:
    """Scrape reviews for multiple URLs."""
    # converts single url to list
    if isinstance(urls, str):
        urls = [urls]

    all_reviews_data = []

    for url in urls:
        try:
            reviews_data = await scrape_reviews(url, max_pages)
            all_reviews_data.append({
                "url": url,
                "reviews": reviews_data
            })
        except Exception as e:
            log.error(f"Error scraping {url}: {e}")
    
    return all_reviews_data