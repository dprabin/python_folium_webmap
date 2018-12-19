import folium
map=folium.Map(location=[27.7,85.35],zoom_start=7, tiles="Mapbox Bright")
map.add_child(folium.Marker(location=[27.66,85.33], popup="This is new marker"))
map.save("Map1.html")
