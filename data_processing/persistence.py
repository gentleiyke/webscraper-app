import json
import pandas as pd
def save_to_json(data: any, file_path: str):
    """Save data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def save_to_csv(df: pd.DataFrame, file_path: str):
    """Save DataFrame to a CSV file."""
    df.to_csv(file_path, index=False)