import pandas as pd
from typing import List, Dict

def reviews_to_dataframe(reviews_data: List[Dict]) -> Dict[str, pd.DataFrame]:
    """ Normalise reviews JSON data and convert it into DataFrames"""
    url_to_df = {}
    for entry in reviews_data:
        url = entry["url"]
        reviews = entry["reviews"]
        # Normalise nested reviews
        df = pd.json_normalize(reviews)
        url_to_df[url] = df
    return url_to_df
