import render
import folium
from pathlib import Path
import os
import random

def run(base_map, filename, color):
    try:
        render.plot(base_map,filename, color)
    except UserWarning:
        render.plot(base_map,filename,'purple')
        
    base_map.save('assets/multimap2.html')

map = folium.Map(location = (34.0556, -117.1825), 
                 zoom_start = 4, 
                 tiles='Esri.WorldTopoMap',
                 no_wrap = True,
                 max_zoom = 16, #inward
                 min_zoom = 2, #outward
                 max_bounds=True
                 )

trips = Path(__file__).parent.resolve() / "Trips"

colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'black']

folders = [f.name.split('/')[-1] for f in Path('Trips').iterdir()]

for fname in folders:
    run(map, fname, colors[random.randint(0, len(colors)-1)])
    