import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

df = pd.read_csv('Age_winpct.csv')
df.columns = [datetime.strptime(col, '%m/%d/%Y') if '/' in col else col for col in df.columns]
df = df.sort_values(by='Average Age')
heatmap_data = df.set_index('Team').drop(columns=['Average Age'])
plt.figure(figsize=(14, 10))
ax =sns.heatmap(
    heatmap_data, 
    cmap='RdYlBu_r', 
    linewidths=.5, 
    linecolor='black',
    vmin=0,  
    vmax=1,   
    cbar_kws={'label': 'Winning Percentage'} 
)
cbar = ax.collections[0].colorbar
cbar.set_label('Winning Percentage', labelpad=20) 

plt.title('Winning % over 2023-24 Season (ordered in increasing average age of top nine players in MP)')
plt.xlabel('Date')
plt.ylabel('Team')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()