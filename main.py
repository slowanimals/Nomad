import render
import folium

def run(base_map, filename, color):
    try:
        render.plot(base_map,filename, color)
    except UserWarning:
        render.plot(base_map,filename,'purple')
    base_map.save('multimap.html')

map = folium.Map(location = (34.0556, -117.1825), zoom_start = 4, tiles='Esri.WorldTopoMap')

run(map,'alaska','purple')
run(map,'yellowstone','blue')
