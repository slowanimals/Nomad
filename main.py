import render
import folium
from pathlib import Path
import os
import random
import shutil

def run():
    base_map = folium.Map(location = (34.0556, -117.1825), 
                 zoom_start = 4, 
                 tiles='Esri.WorldTopoMap',
                 no_wrap = True,
                 max_zoom = 16, #inward
                 min_zoom = 2, #outward
                 max_bounds=True
                 )

    if os.path.exists('assets/thumbs'):
        shutil.rmtree('assets/thumbs')
    os.mkdir('assets/thumbs')

    folder_path = Path('assets') / 'Trips'
    folders = [f.name.split('/')[-1] for f in folder_path.iterdir()]
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'black']

    for name in folders:
        print(name)
        try:
            render.plot(base_map, f'assets/Trips/{name}', colors[random.randint(0, len(colors)-1)])
        except UserWarning:
            render.plot(base_map,f'assets/Trips/{name}','purple')
        
    base_map.save('assets/themap.html')



#trips = Path(__file__).parent.resolve() / "Trips"

#run()




