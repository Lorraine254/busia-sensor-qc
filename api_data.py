import requests
import csv

# API endpoint
url = "https://weather.api.wirelessplanet.co.ke/api/v2/afrisense/weatherdata/"

# parameters
page = 1
page_size = 100
to_time = "2025-09-03T10:10:15+00:00"


csv_file = "weather_data.csv"
headers = ["id", "station_id", "latitude", "longitude", "altitude", "light_intensity",
           "UV_index", "air_temperature", "air_humidity", "pressure", "wind_speed",
           "peak_wind_gust", "wind_direction", "rain_guage", "rain_accumulation",
           "uplink_time", "raw_payload", "timestamp"]

# writing headers to the CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers) # write dictionary data into a csv
    writer.writeheader()

    while True:
        params = {
            "to": to_time,
            "page": page,
            "page_size": page_size
        }

        response = requests.get(url, params=params)
        data = response.json()

        for entry in data["data"]:
            writer.writerow({h: entry.get(h, "") for h in headers})

        print(f"Page {page} saved. Records: {len(data['data'])}")

        if not data.get("has_next", False):
            break

        page += 1

print(f"All data up to {to_time} saved to {csv_file}")


