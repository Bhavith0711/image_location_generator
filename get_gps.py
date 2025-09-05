from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import requests

# Function to convert GPS DMS (degrees, minutes, seconds) to decimal
def convert_to_degrees(value):
    d, m, s = value
    d = float(d)
    m = float(m)
    s = float(s)
    return d + (m / 60.0) + (s / 3600.0)

# Extract GPS data from image
def get_gps_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    
    if not exif_data:
        return None
    
    gps_info = {}
    for tag, value in exif_data.items():
        decoded = TAGS.get(tag, tag)
        if decoded == "GPSInfo":
            for t in value:
                sub_decoded = GPSTAGS.get(t, t)
                gps_info[sub_decoded] = value[t]
    
    if not gps_info:
        return None
    
    # ✅ Safe check before accessing GPSLatitude & GPSLongitude
    if "GPSLatitude" in gps_info and "GPSLongitude" in gps_info:
        lat = convert_to_degrees(gps_info["GPSLatitude"])
        if gps_info.get("GPSLatitudeRef") == "S":
            lat = -lat

        lon = convert_to_degrees(gps_info["GPSLongitude"])
        if gps_info.get("GPSLongitudeRef") == "W":
            lon = -lon

        return lat, lon
    
    return None

# Get human-readable address from OpenStreetMap
def get_address(lat, lon):
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    headers = {"User-Agent": "location-script"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("display_name", "Address not found")
    return "Error fetching address"

# Main
if __name__ == "__main__":
    image_file = "D:/photo_location/england-london-bridge.jpg"   # 👈 change to your photo filename
    gps_data = get_gps_data(image_file)
    
    if gps_data:
        lat, lon = gps_data
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")
        print("Fetching address...")
        address = get_address(lat, lon)
        print(f"Location: {address}")
    else:
        print("❌ No GPS data found in this image")
