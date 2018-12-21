import folium
import pandas

data = pandas.read_csv("PakhareBagar_Poonhill_Trek.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
addr = list(data["NAME"]+", "+data["LOCAL"]+", "+data["DIST"])

def get_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 2000:
        return 'orange'
    elif 2000 <= elevation < 3000:
        return "pink"
    else:
        return 'red'

#map=folium.Map(location=[27.7,85.35],zoom_start=7, tiles="Mapbox Bright")
map=folium.Map(location=[28.399751,83.688888],zoom_start=10, tiles="Mapbox Bright")

fg=folium.FeatureGroup(name="My Map")
for lt, ln, el, ad in zip(lat, lon, elev,addr):
    fg.add_child(folium.Marker(location=[lt, ln], popup=ad+" ("+str(el)+" meters)",icon=folium.Icon(get_color(el))))
map.add_child(fg)

map.save("Map2.html")
