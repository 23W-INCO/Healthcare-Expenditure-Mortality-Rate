import pandas as pd
import folium

df = pd.read_excel('./GHED_data (1).xlsx')
df_2021 = df[df['year'] == 2021]

geojson_path = 'countries.geojson'

map_center = [48.4284, 12.9424]

mymap = folium.Map(location=map_center, zoom_start=3)

folium.Choropleth(
    geo_data=geojson_path,
    name='choropleth',
    data=df_2021,
    columns=['country', 'gge'],
    key_on='feature.properties.ADMIN',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Your Legend Name'
).add_to(mymap)

# Display the map
mymap.save('your_choropleth_map.html')
