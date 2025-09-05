# image_location_generator
this is my basic project
# 📍 image location generator

This project extracts **GPS coordinates** (latitude & longitude) from an image’s EXIF metadata and converts them into a **human-readable address** using the OpenStreetMap Nominatim API.

It’s useful if you want to:

* Find out **where a photo was taken**
* Convert EXIF GPS data into **decimal coordinates**
* Get a real-world **address or place name** from a photo

---

## 🚀 Features

* Reads **EXIF metadata** from JPEG/HEIC photos
* Extracts **GPSLatitude & GPSLongitude** (if available)
* Converts Degrees/Minutes/Seconds (DMS) into **decimal degrees**
* Automatically detects **N/S/E/W hemisphere** and adjusts sign
* Reverse-geocodes coordinates into an **address** using OpenStreetMap
* Prints location info in the terminal

---

## 🛠️ Requirements

* Python 3.8+
* Libraries:

  ```bash
  pip install pillow requests
  ```
* If using **HEIC (iPhone/modern phones)** images:

  ```bash
  pip install pillow-heif
  ```

---

## 📂 Usage

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/photo-location-extractor.git
   cd photo-location-extractor
   ```

2. Place your photo in the project folder (e.g., `your_photo.jpg`).

3. Run the script:

   ```bash
   python get_location.py
   ```

4. Example output:

   ```
   Latitude: 17.412345
   Longitude: 78.503210
   Fetching address...
   Location: Road No. 12, Banjara Hills, Hyderabad, Telangana, India
   ```

---

## 📷 Important Notes

* **Not all images have GPS metadata.**
  Many apps (WhatsApp, Instagram, screenshots) **remove EXIF data**. Use original camera photos.
* Accuracy depends on your device and GPS signal.
* Reverse-geocoding uses **OpenStreetMap Nominatim** (be kind: rate limit ≈1 request/sec).

---

## 📌 Example

Let’s say you have a photo taken on your phone. Running the script:

```
python get_location.py
```

Might print:

```
Latitude: 37.774929
Longitude: -122.419416
Fetching address...
Location: San Francisco, California, United States of America
```

You can also open the coordinates directly in Google Maps:
👉 [https://maps.google.com/?q=37.774929,-122.419416](https://maps.google.com/?q=37.774929,-122.419416)

---

## 🔮 Future Improvements

* Add GUI/web interface for easier photo uploads
* Batch processing for multiple photos
* Display results on an interactive map
* Support for more EXIF tags (altitude, timestamp, camera info)

---

## 📜 License

This project is licensed under the MIT License.

---

👉 Do you also want me to make a **short one-line tagline** (like a GitHub repo description) that appears right under your repo name? Example: *“Extract GPS location and address from your photos using Python.”*
