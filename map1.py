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
map=folium.Map(location=[38.58,-99.09],zoom_start=2, tiles="Mapbox Bright")

fgv=folium.FeatureGroup(name="US Voalcanoes")
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el)+" meters",fill_color=(get_color(el)),color='grey',fill_opacity=0.5))
map.add_child(fgv)

fgwp=folium.FeatureGroup(name="World Population")
fgwp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] <50000000 else 'red'}))
map.add_child(fgwp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
