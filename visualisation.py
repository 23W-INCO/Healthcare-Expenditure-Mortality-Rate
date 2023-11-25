import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
df = pd.read_excel('Book1.xlsx')
target_year = 2021
df_year = df[df['year'] == target_year]
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
merged = world.merge(df, left_on='name', right_on='country')
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged.plot(column='gge', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, vmin=0, vmax=6000000)
ax.set_title('The Healthcare Expenditure of Different Countries', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.set_axis_off()
plt.show()