import read
import folium

def plot(path, linecolr):
    meta = read.get_exif_data(f'{path}/')
    map = folium.Map(
        location=meta[0][1]['location'], 
        zoom_start=6,
        tiles='Esri.WorldStreetMap'
        )


    coords = []
    for filename, data in meta:
        coords.append(data['location'])

    for filename, data in meta:

        folium.Marker(
        location = data['location'],
        tooltip= filename,
        icon = folium.Icon(color=linecolr),

        popup = folium.Popup(
            f"<b>{filename}</b><br>{data['time']}<br>"
            f"<img src = 'images/{data['path']}' width ='200'>",
            max_width = 250
        ),
        ).add_to(map)

    folium.PolyLine(
            locations = coords,
            color = linecolr,
            weight = 2
        ).add_to(map)
    

    map.save('testmap.html')




#plot('alaska','blue')
