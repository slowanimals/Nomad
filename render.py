import read
import folium

def plot(path):
    coords = read.get_exif_data(f'{path}/')
    map = folium.Map(location=coords[0], zoom_start=6)

    for i in coords:
        folium.Marker(
        location = i,
        tooltip='Click me!',
        icon = folium.Icon(color='red')
        ).add_to(map)
    map.save('testmap.html')

plot('images')
