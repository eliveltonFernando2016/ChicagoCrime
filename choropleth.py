import os
import folium
import json
import pandas as pd

ward = pd.read_csv('quantidadeWard2.csv')
geo_json_data = json.load(open('chicagoCity.json'))

teste = geo_json_data['features']

m = folium.Map([41.679280604, -87.610128133], zoom_start=8)
folium.GeoJson(geo_json_data).add_to(m)

percent = []
total = 0
for i in ward['quantidade']:
    total = total+i

for i in ward['quantidade']:
    percent.append(i/total)

ward['percent'] = percent

bins = list(ward['percent'].quantile([0, 0.10, 0.25, 0.5, 0.75, 1]))
m.choropleth(
    geo_data=geo_json_data,
    name='choropleth',
    data=ward,
    columns=['ward', 'percent'],
    key_on='feature.id',
    fill_color='BuGn',
    fill_opacity=0.8,
    line_opacity=0.5,
    legend_name='Crimes por àrea(%)',
    threshold_scale=bins,
    highlight = True
)
folium.LayerControl().add_to(m)

# Save to html
m.save('choropleth.html')
