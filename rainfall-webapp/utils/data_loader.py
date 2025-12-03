# rainfall-webapp/utils/data_loader.py
import pandas as pd
import numpy as np


def load_rainfall_data(csv_path):
    """Load and preprocess rainfall forecast data"""
    try:
        df = pd.read_csv(csv_path)
        print(f"✅ Loaded {len(df)} forecast records")
        print(f"📊 Districts: {df['district'].nunique()}")
        print(f"📅 Date range: {df['date'].min()} to {df['date'].max()}")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return pd.DataFrame()


def get_district_forecast(df, district, year, month):
    """Get specific forecast for a district"""
    date_str = f"{year}-{month:02d}"
    result = df[(df["district"] == district) & (df["date"] == date_str)]
    return result.iloc[0] if not result.empty else None


def get_region_districts(df, region):
    """Get all districts in a region"""
    return df[df["region"] == region]["district"].unique().tolist()
