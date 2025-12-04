# app.py - Uganda Rainfall Forecast Web Application
from flask import Flask, render_template, request, jsonify
import pandas as pd
#import numpy as np
from datetime import datetime
import os

app = Flask(__name__)

# Load your forecast data
DATA_PATH = "static/data/uganda_rainfall_forecasts_2025_2026.csv"

# District coordinates (approximate - you can get more accurate ones)
DISTRICT_COORDINATES = {
    "Abim": [2.7011, 33.6661],
    "Adjumani": [3.3779, 31.7909],
    "Agago": [2.8338, 33.3333],
    "Alebtong": [2.2447, 33.2547],
    "Amolatar": [1.6376, 32.8447],
    "Amudat": [1.9500, 34.9500],
    "Amuru": [2.8139, 31.9389],
    "Apac": [1.9756, 32.5386],
    "Arua": [3.0201, 30.9118],
    "Budaka": [1.0167, 33.9333],
    "Bugiri": [0.5714, 33.7417],
    "Buhweju": [-0.3500, 30.3000],
    "Buikwe": [0.3500, 33.0333],
    "Bukedea": [1.3167, 34.0500],
    "Bukwo": [1.2592, 34.7531],
    "Bulambuli": [1.1667, 34.3833],
    "Buliisa": [2.1667, 31.4167],
    "Bundibugyo": [0.7083, 30.0639],
    "Bunyangabu": [0.5014, 30.2750],
    "Bushenyi": [-0.5853, 30.2114],
    "Busia": [0.4669, 34.0922],
    "Butambala": [0.1833, 32.1000],
    "Buvuma": [0.3833, 33.2500],
    "Buyende": [1.2000, 33.1500],
    "Dokolo": [1.9167, 33.1667],
    "Gomba": [0.2000, 31.9000],
    "Gulu": [2.7746, 32.2980],
    "Hoima": [1.4319, 31.3525],
    "Ibanda": [-0.1333, 30.5000],
    "Iganga": [0.6092, 33.4686],
    "Isingiro": [-0.8833, 30.8000],
    "Jinja": [0.4244, 33.2041],
    "Kaabong": [3.4833, 34.1500],
    "Kabale": [-1.2486, 29.9897],
    "Kaberamaido": [1.7389, 33.1594],
    "Kagadi": [0.9600, 30.7967],
    "Kakumiro": [0.7833, 31.0667],
    "Kalangala": [-0.3089, 32.2250],
    "Kaliro": [1.0833, 33.5000],
    "Kalungu": [-0.1667, 31.7667],
    "Kamuli": [0.9472, 33.1197],
    "Kamwenge": [0.1861, 30.4539],
    "Kanungu": [-0.6900, 29.7425],
    "Kapchorwa": [1.4006, 34.4508],
    "Kapelebyong": [1.9500, 33.8000],
    "Karenga": [3.5000, 34.5500],
    "Kasese": [0.1833, 30.0833],
    "Kassanda": [0.5333, 32.0667],
    "Katakwi": [1.8911, 33.9661],
    "Kayunga": [0.7025, 32.8886],
    "Kazo": [-0.1000, 30.9500],
    "Kibaale": [0.9667, 31.1667],
    "Kiboga": [0.9161, 31.7742],
    "Kibuku": [1.0500, 33.8000],
    "Kikuube": [1.0167, 31.0167],
    "Kiruhura": [-0.1964, 30.8447],
    "Kiryandongo": [1.8667, 32.0500],
    "Kisoro": [-1.2839, 29.6850],
    "Kitagwenda": [-0.2000, 30.4500],
    "Kitgum": [3.2783, 32.8867],
    "Koboko": [3.4136, 31.0194],
    "Kole": [2.4000, 32.8000],
    "Kotido": [3.0081, 34.1125],
    "Kumi": [1.4878, 33.9361],
    "Kwania": [2.2500, 32.8000],
    "Kween": [1.4167, 34.5333],
    "Kyankwanzi": [1.2000, 31.8000],
    "Kyegegwa": [0.5022, 31.0414],
    "Kyenjojo": [0.6328, 30.6214],
    "Kyotera": [-0.6156, 31.5175],
    "Lamwo": [3.5297, 32.8017],
    "Lira": [2.2489, 32.9000],
    "Luuka": [0.7000, 33.3167],
    "Luwero": [0.8492, 32.4731],
    "Lwengo": [-0.4167, 31.4167],
    "Lyantonde": [-0.4081, 31.1572],
    "Madi Okollo": [2.5333, 31.4000],
    "Maracha": [3.2700, 30.9850],
    "Masaka": [-0.3350, 31.7342],
    "Masindi": [1.6744, 31.7150],
    "Mayuge": [0.4578, 33.4803],
    "Mbale": [1.0822, 34.1753],
    "Mbarara": [-0.6072, 30.6545],
    "Mitooma": [-0.6000, 30.0167],
    "Mityana": [0.4000, 32.0500],
    "Moroto": [2.5333, 34.6667],
    "Moyo": [3.6631, 31.7200],
    "Mpigi": [0.2250, 32.3139],
    "Mubende": [0.5583, 31.3950],
    "Mukono": [0.3533, 32.7553],
    "Nabilatuk": [2.3000, 34.6500],
    "Nakapiripirit": [1.9167, 34.7833],
    "Nakaseke": [1.3500, 32.2333],
    "Nakasongola": [1.3089, 32.4564],
    "Namayingo": [0.2397, 33.8844],
    "Namutumba": [0.8361, 33.6856],
    "Napak": [2.2500, 34.2500],
    "Nebbi": [2.4789, 31.0889],
    "Ngora": [1.4833, 33.7667],
    "Ntoroko": [1.0411, 30.3911],
    "Ntungamo": [-0.8792, 30.2642],
    "Nwoya": [2.6333, 32.0833],
    "Obongi": [3.3761, 31.4108],
    "Omoro": [2.7167, 32.4333],
    "Otuke": [2.5000, 33.5000],
    "Oyam": [2.2356, 32.3850],
    "Pader": [2.9667, 33.2167],
    "Pallisa": [1.1450, 33.7094],
    "Rakai": [-0.7200, 31.4833],
    "Rubirizi": [-0.2986, 30.1081],
    "Rukungiri": [-0.8411, 29.9419],
    "Rwampara": [-0.8500, 30.4500],
    "Serere": [1.5000, 33.4667],
    "Sironko": [1.2333, 34.2500],
    "Soroti": [1.7147, 33.6111],
    "Ssembabule": [-0.0772, 31.4567],
    "Tororo": [0.6928, 34.1808],
    "Wakiso": [0.4044, 32.4594],
    "Yumbe": [3.4651, 31.2469],
    "Zombo": [2.5133, 30.9097],
}

# Region descriptions
REGION_DESCRIPTIONS = {
    "Northern": {
        "name": "Northern Region",
        "description": "Northern Uganda is characterized by savanna grasslands and experiences two rainy seasons. The region has faced challenges but is now experiencing economic growth with agriculture as the main activity.",
        "climate": "Tropical savanna climate with distinct wet and dry seasons",
        "rainfall_pattern": "Bimodal rainfall pattern with peaks in April-May and August-September",
    },
    "Eastern": {
        "name": "Eastern Region",
        "description": "Eastern Uganda is mountainous with fertile volcanic soils, home to Mount Elgon. The region receives significant rainfall and is known for agriculture, especially coffee and fruit production.",
        "climate": "Tropical monsoon climate with high rainfall",
        "rainfall_pattern": "Consistent rainfall throughout the year with peaks in April and October",
    },
    "Western": {
        "name": "Western Region",
        "description": "Western Uganda features highlands, lakes, and national parks including Queen Elizabeth and Bwindi. Known as Uganda's cattle corridor, it has moderate rainfall and rich agricultural lands.",
        "climate": "Tropical savanna and highland climates",
        "rainfall_pattern": "Moderate bimodal rainfall with peaks in March-May and September-November",
    },
    "Central": {
        "name": "Central Region",
        "description": "Central Uganda includes the capital Kampala and Lake Victoria shores. It has tropical rainforest climate with consistent rainfall supporting diverse agriculture and urban development.",
        "climate": "Tropical rainforest climate",
        "rainfall_pattern": "Relatively consistent rainfall throughout the year",
    },
}

# Global variable for forecast data
forecast_data = pd.DataFrame()


@app.before_request
def load_forecast_data():
    """Load forecast data from CSV"""
    global forecast_data
    if forecast_data.empty:
        try:
            forecast_data = pd.read_csv(DATA_PATH)
            # Convert date string to datetime for easier querying
            forecast_data["date_dt"] = pd.to_datetime(forecast_data["date"] + "-01")

            print(f"✅ Loaded {len(forecast_data)} forecast records")
            print(f"📊 Districts: {forecast_data['district'].nunique()}")
            print(
                f"📅 Date range: {forecast_data['date_dt'].min()} to {forecast_data['date_dt'].max()}"
            )

        except Exception as e:
            print(f"❌ Error loading data: {e}")
            forecast_data = pd.DataFrame()


@app.route("/")
def index():
    """Main page"""
    if forecast_data.empty:
        districts = list(DISTRICT_COORDINATES.keys())
    else:
        districts = sorted(forecast_data["district"].unique().tolist())

    return render_template("index.html", districts=districts)


@app.route("/predict", methods=["POST"])
def predict():
    """Get rainfall prediction for a district and date"""
    try:
        data = request.json
        district = data.get("district")
        year = int(data.get("year", 2025))
        month = int(data.get("month", 1))

        # Create date string in format used in CSV
        date_str = f"{year}-{month:02d}"

        # Query the forecast data
        result = forecast_data[
            (forecast_data["district"] == district)
            & (forecast_data["date"] == date_str)
        ]

        if result.empty:
            return jsonify(
                {"error": f"No forecast found for {district} in {date_str}"}
            ), 404

        # Get the forecast value
        forecast = result.iloc[0]

        # Get region information
        region = forecast["region"]
        region_info = REGION_DESCRIPTIONS.get(region, {})

        # Get coordinates
        coordinates = DISTRICT_COORDINATES.get(
            district, [1.3733, 32.2903]
        )  # Uganda center as fallback

        # Prepare response
        response = {
            "district": district,
            "year": year,
            "month": month,
            "rainfall_mm": round(forecast["predicted_rainfall_mm"], 1),
            "region": region,
            "region_name": region_info.get("name", region),
            "region_description": region_info.get("description", ""),
            "region_climate": region_info.get("climate", ""),
            "region_rainfall_pattern": region_info.get("rainfall_pattern", ""),
            "coordinates": coordinates,
            "month_name": datetime(year, month, 1).strftime("%B"),
            "interpretation": interpret_rainfall(forecast["predicted_rainfall_mm"]),
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/districts/<region>")
def get_districts_by_region(region):
    """Get all districts in a region"""
    if forecast_data.empty:
        return jsonify({"error": "Data not loaded"}), 500

    districts = (
        forecast_data[forecast_data["region"] == region]["district"].unique().tolist()
    )
    return jsonify({"region": region, "districts": sorted(districts)})


@app.route("/forecast/<district>")
def get_district_forecast(district):
    """Get all forecasts for a district"""
    if forecast_data.empty:
        return jsonify({"error": "Data not loaded"}), 500

    district_data = forecast_data[forecast_data["district"] == district]

    forecasts = []
    for _, row in district_data.iterrows():
        date_parts = row["date"].split("-")
        forecasts.append(
            {
                "year": int(date_parts[0]),
                "month": int(date_parts[1]),
                "rainfall_mm": round(row["predicted_rainfall_mm"], 1),
                "month_name": datetime(
                    int(date_parts[0]), int(date_parts[1]), 1
                ).strftime("%B"),
            }
        )

    # Sort by year and month
    forecasts.sort(key=lambda x: (x["year"], x["month"]))

    return jsonify(
        {
            "district": district,
            "region": district_data.iloc[0]["region"]
            if not district_data.empty
            else "",
            "forecasts": forecasts,
        }
    )


@app.route("/api/stats")
def get_statistics():
    """Get overall statistics"""
    if forecast_data.empty:
        return jsonify({"error": "Data not loaded"}), 500

    total_districts = forecast_data["district"].nunique()
    avg_rainfall = forecast_data["predicted_rainfall_mm"].mean()
    max_rainfall = forecast_data["predicted_rainfall_mm"].max()
    min_rainfall = forecast_data["predicted_rainfall_mm"].min()

    # Find district with highest rainfall
    max_row = forecast_data.loc[forecast_data["predicted_rainfall_mm"].idxmax()]

    return jsonify(
        {
            "total_districts": total_districts,
            "avg_rainfall": round(avg_rainfall, 1),
            "max_rainfall": round(max_rainfall, 1),
            "min_rainfall": round(min_rainfall, 1),
            "wettest_district": {
                "name": max_row["district"],
                "rainfall": round(max_row["predicted_rainfall_mm"], 1),
                "date": max_row["date"],
            },
        }
    )


def interpret_rainfall(mm):
    """Interpret rainfall amount"""
    if mm < 30:
        return "Very light rainfall - Dry conditions"
    elif mm < 60:
        return "Light rainfall - Suitable for light crops"
    elif mm < 100:
        return "Moderate rainfall - Good for most crops"
    elif mm < 150:
        return "Heavy rainfall - Good for water-intensive crops"
    elif mm < 200:
        return "Very heavy rainfall - Risk of flooding"
    else:
        return "Extreme rainfall - High flood risk"


if __name__ == "__main__":
    # Load data before starting
    load_forecast_data()
    app.run(debug=True, port=5000)
