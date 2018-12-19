import folium
map=folium.Map(location=[27.7,85.35],zoom_start=7, tiles="Mapbox Bright")
map.add_child(folium.Marker(location=[27.8,85.0], popup="This is new marker",icon=folium.Icon(color="green")))
map.save("Map1.html")
