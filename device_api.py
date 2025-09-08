import requests
import pandas as pd

# API endpoint
url = "https://weather.api.wirelessplanet.co.ke/api/v2/afrisense/devices/?page=1&page_size=50"

# Station IDs to check
station_ids = [
    "101990961244800001", "101990961244800005", "101990961244800061",
    "101990961244800083", "101990961244800101", "101990961244800102",
    "101990961244800113", "101990961244800131", "101990961244800184",
    "101990961244800201", "101990961244800207", "101990961244800222",
    "101990961244800246", "101990961244800270", "101990961244800281",
    "101990961244800296", "101990961244800302", "101990961244800306",
    "101990961244800317", "101990961244800336", "101990961244800342",
    "101990961244800348", "101990961244800361", "101990961244800375",
    "101990961244800389", "101990961244800393", "101990961244800395",
    "202003536241300473"
]

def fetch_station_data():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        station_data = data.get("data", {})
        records = []

        for station_id in station_ids:
            if station_id in station_data:
                s = station_data[station_id]
                records.append({
                    "Station_ID": station_id,
                    "Location": s.get("Location", "N/A"),
                    "Latitude": s.get("Latitude", "N/A"),
                    "Longitude": s.get("Longitude", "N/A"),
                    "Last_Update": s.get("Last_Update", "N/A")
                })
            else:
                records.append({
                    "Station_ID": station_id,
                    "Location": "Not Found",
                    "Latitude": "N/A",
                    "Longitude": "N/A",
                    "Last_Update": "N/A"
                })

        # Convert to DataFrame
        df = pd.DataFrame(records)
        # Save to CSV
        df.to_csv("stations_report.csv", index=False)
        print("Data saved to stations_report.csv")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    fetch_station_data()
