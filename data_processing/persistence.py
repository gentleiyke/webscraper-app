import json
import pandas as pd
from loguru import logger as log
def save_to_json(data: any, file_path: str):
    """Save data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    log.info(f"Scraped data for {file_path} successfully")

def save_to_csv(df: pd.DataFrame):
    """Save DataFrame to a CSV file."""
    # df.to_csv(file_path, index=False)
    df.to_csv(index=False).encode('utf-8')
    log.info(f"Saved DataFrame to {file_path}")