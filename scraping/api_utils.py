from httpx import AsyncClient
from parsel import Selector
import json

# Initialise an async HTTPX client
client = AsyncClient(
    http2=True,
    headers={
        "accept-language": "en-US,en;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
    },
)

async def get_reviews_api_url(url: str) -> str:
    """Scrape the API version from the HTML and create the reviews API URL."""
    response = await client.get(url)
    selector = Selector(response.text)
    build_id = json.loads(selector.xpath("//script[@id='__NEXT_DATA__']/text()").get())["buildId"]
    business_unit = url.split("review/")[-1]
    return f"https://www.trustpilot.com/_next/data/{build_id}/review/{business_unit}.json?sort=recency&businessUnit={business_unit}"
