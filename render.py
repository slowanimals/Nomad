import osmnx as ox
import read
import folium

def plot(folder, color):

    places = read.get_exif_data(folder) #5087, 5100 are in sitka
    map = folium.Map(location = places[0][1]['location'], zoom_start = 14)

    for i in range(len(places) - 1):
        orig = places[i][1]['location'] #(lat, long)
        dest = places[i+1][1]['location'] #(lat,long)
        img_name = places[i][0]
        date = places[i][1]['time']

        folium.Marker(orig, 
                    tooltip = f'{img_name}\n{date}').add_to(map)
        
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
                            weight = 3).add_to(map)
                
            folium.PolyLine(path_coords, 
                            color = color, 
                            weight = 3).add_to(map)
            
            #if path doesn't go until destination, fill in gap
            if path_coords[-1] != dest:
                folium.PolyLine((path_coords[-1], dest), 
                            color = color, 
                            weight = 3).add_to(map)
           
        except:
            #if unable to generate graph, create standard polylin
            folium.PolyLine(locations = [orig, dest], 
                            color = color, 
                            weight=3).add_to(map)
    
    #last marker
    folium.Marker(
        location = places[-1][1]['location'],
        tooltip= f'{img_name}\n{date}').add_to(map)

    map.save('testmap3.html')
