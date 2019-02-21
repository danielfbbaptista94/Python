import folium
import pandas


data = pandas.read_csv('Volcanoes.txt')
lat_list = list(data['LAT'])
long_list = list(data['LON'])
elev_list = list(data['ELEV'])


def color_producer(elevetion):
    if elevetion < 1000:
        return 'green'
    elif 1000 <= elevetion < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[-20, -40], zoom_start=3, tiles="Mapbox Bright")

fg_vulcanoes = folium.FeatureGroup(name='Vulcanoes')
for lat, long, elev in zip(lat_list, long_list, elev_list):
    fg_vulcanoes.add_child(folium.CircleMarker(location=[lat, long], radius=6, popup=str(elev)+' m',
                                     fill_color=color_producer(elev), color='grey', fill_opacity=0.7))

fg_population = folium.FeatureGroup(name='Population')
fg_population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                                style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; left: 50px; width: 200px; height: 125px; 
                border:2px solid grey; z-index:9999; font-size:14px;
                ">&nbsp; Population <br>
                  &nbsp; < 10000000 &nbsp; <i class="fa fa-square fa-1x" style="color:green"></i><br>
                  &nbsp; <= 10000000 and &nbsp; <20000000 &nbsp; <i class="fa fa-square fa-1x" style="color:orange"></i><br>
                  &nbsp; > 20000000 &nbsp; <i class="fa fa-square fa-1x" style="color:red"></i>
    </div>
'''

map.add_child(fg_vulcanoes)
map.add_child(fg_population)
map.get_root().html.add_child(folium.Element(legend_html))
map.add_child(folium.LayerControl())
map.save("Map.html")
