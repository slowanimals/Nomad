import exifread
from pathlib import Path

#convert gps coords to decimal
def convert_to_degrees(value):
    deg = float(value.values[0])
    min = float(value.values[1])
    sec = float(value.values[2])

    result = deg + (min/60.0) + (sec/3600.0)
    return result

#extract exif matadata
def get_exif_data(path):
    coords = []
    folder = Path(path)

    for img in folder.iterdir():
        if img.suffix.lower() in ['.png','.jpg','.jpeg','.webp']:
            with open(img, 'rb') as file:
                tags = exifread.process_file(file)
            
            gps_lat = tags.get('GPS GPSLatitude')
            gps_lat_ref = tags.get('GPS GPSLatitudeRef')
            gps_long = tags.get("GPS GPSLongitude")
            gps_long_ref = tags.get("GPS GPSLongitudeRef")

            if gps_lat and gps_lat_ref and gps_long and gps_long_ref:
                lat = convert_to_degrees(gps_lat)
                long = convert_to_degrees(gps_long)

                if gps_lat_ref.values[0] != 'N':
                    lat = -lat
                if gps_long_ref.values[0] != 'E':
                    long = -long
            
            coords.append([lat,long])
    return coords
    
    

#print(get_exif_data('images/'))