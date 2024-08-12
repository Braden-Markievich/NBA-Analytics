### COde used for constructing the spider chart


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

df = pd.read_csv('mobley_spider.csv')
selected_seasons = ['2023-24', 'Career', 'League']
filtered_df = df[df['SEASON'].isin(selected_seasons)]
categories = filtered_df.columns[1:].tolist()
data = filtered_df.iloc[:, 1:].values.tolist()
data_names = ['2023-24 Season', 'Career Averages (including 23-24 Season)', 'League Averages for 23-24 Season']
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]
categories += categories[:1]
colors = ['b', 'g', 'r']

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
for i, dataset in enumerate(data):
    dataset += dataset[:1] 
    ax.plot(angles, dataset, color=colors[i], linewidth=2, linestyle='solid', label=data_names[i])
    ax.fill(angles, dataset, color=colors[i], alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories[:-1])

ax.legend(loc='upper right', bbox_to_anchor=(-0.1, 0.8))
fig.text(0.5, 0.965, 'Evan Mobley 2023-2024 Season Offensive Efficiency Breakdown (stats via Basketball-Reference)',
             horizontalalignment='center', color='black', weight='bold',
             size='large')

img = Image.open('mobley_photo.png')
newax = fig.add_axes([0.75, 0.75, 0.2, 0.2], anchor='NE', zorder=1)
newax.imshow(img)
newax.axis('off')

table_data = filtered_df.set_index('SEASON').T  
table = ax.table(cellText=table_data.values, colLabels=data_names, rowLabels=categories[:-1],
                 loc='bottom', cellLoc='center', bbox=[-0.45, -0.5, 2.0, 0.3])

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)
plt.subplots_adjust(bottom=0.3)
plt.show()
