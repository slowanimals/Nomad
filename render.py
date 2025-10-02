import osmnx as ox
import read
import folium
from PIL import Image
from pathlib import Path



def plot(base, folder, color):

    group = folium.FeatureGroup(name=folder)

    places = read.get_exif_data(folder) #5087, 5100 are in sitka
    #map = folium.Map(location = places[0][1]['location'], zoom_start = 14)

    for i in range(len(places) - 1):
        orig = places[i][1]['location'] #(lat, long)
        dest = places[i+1][1]['location'] #(lat,long)
        img_name = places[i][0]
        date = places[i][1]['time']
        path = places[i][1]['path']
        thumb = places[i][1]['thumb']

        popup = f"""
                <b> {img_name}</b><br>
                <img src = "{path}" width = "200">
                """ 
        
        icon = folium.CustomIcon(
            thumb,
            icon_size = (40,40),
            shadow_size = (40,40),
            shadow_anchor=(10,40)
        )

        folium.Marker(
                    orig, 
                    icon = icon,
                    tooltip = img_name,
                    popup = popup,
                    #opacity = 0.5
                    ).add_to(group)
        
        lat_mid = (orig[0] + dest[0]) / 2
        lon_mid = (orig[1] + dest[1]) / 2
        try:
            G = ox.graph_from_point((lat_mid, lon_mid), dist=10000, network_type='all')
            
            #find nearest node, switch lat & long
            orig_node = ox.nearest_nodes(G, orig[1], orig[0])
            dest_node = ox.nearest_nodes(G, dest[1], dest[0])

            sp = ox.shortest_path(G, orig_node, dest_node, weight = 'length')
            path_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in sp]
            
            #if path doesn't begin at origin, fill in gap
            if path_coords[0] != orig:
                folium.PolyLine((orig, path_coords[0]), 
                            color = color,
                            tooltip = f'{folder}',
                            weight = 4).add_to(group)
                
            folium.PolyLine(path_coords, 
                            color = color,
                            tooltip = f'{folder}',
                            weight = 4).add_to(group)
            
            #if path doesn't go until destination, fill in gap
            if path_coords[-1] != dest:
                folium.PolyLine((path_coords[-1], dest), 
                            color = color,
                            tooltip = f'{folder}',
                            weight = 4).add_to(group)
           
        except:
            #if unable to generate graph, create standard polylin
            folium.PolyLine(locations = [orig, dest], 
                            color = color,
                            tooltip = f'{folder}',
                            weight=4).add_to(group)
    

    last_meta = places[-1][1]
    last_name = places[-1][0]

    last_popup = f"""
                <b> {last_name}</b><br>
                <img src = "{last_meta['path']}" width = "200">
                """ 
        
    last_icon = folium.CustomIcon(
        last_meta['thumb'],
        icon_size = (40,40),
        shadow_size = (40,40),
        shadow_anchor=(20,30)
    )
    
    #last marker
    folium.Marker(
        location = places[-1][1]['location'],
        tooltip= f'{last_name}',
        popup = last_popup,
        icon = last_icon,
        #opacity = 0.5
        ).add_to(group)
    
    group.add_to(base)

    #map.save('testmap3.html')
