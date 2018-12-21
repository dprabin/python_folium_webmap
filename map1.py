import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def get_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

#map=folium.Map(location=[27.7,85.35],zoom_start=7, tiles="Mapbox Bright")
map=folium.Map(location=[38.58,-99.09],zoom_start=5, tiles="Mapbox Bright")

fg=folium.FeatureGroup(name="My Map")
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el)+" meters",fill_color=(get_color(el)),color='grey',fill_opacity=0.5))
map.add_child(fg)

map.save("Map1.html")
