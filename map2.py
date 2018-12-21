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
map=folium.Map(location=[28.399751,83.688888],zoom_start=6, tiles="Mapbox Bright")

fgpoon=folium.FeatureGroup(name="Poon Hill trek")
for lt, ln, el, ad in zip(lat, lon, elev,addr):
    fgpoon.add_child(folium.Marker(location=[lt, ln], popup=ad+" ("+str(el)+" meters)",icon=folium.Icon(get_color(el))))
map.add_child(fgpoon)


fgwp=folium.FeatureGroup(name="World Population")
fgwp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] <50000000 else 'red'}))
map.add_child(fgwp)

map.add_child(folium.LayerControl())

map.save("Map2.html")
