import requests
import folium

res = requests.get('https://ipinfo.com')
data = res.json()

location = data['loc'].split(',')
lat = float(location[0])
log = float(location[1])

fg = folium.FeatureGroup('My map')
fg.add_child(folium.GeoJson(data=(open('./docs/india_states.json', 'r', encoding='utf-8-sig').read())))
fg.add_child(folium.Marker(location=[lat, log], popup='This is my location'))

map = folium.Map(location=[lat, log], zoom_start=7)
map.save("1.html")