import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('nuggets_pps_2324.csv')
df.columns = [col.replace(' PPS', '') for col in df.columns]
heatmap_data = df.set_index('Name')
plt.figure(figsize=(14, 10))
ax = sns.heatmap(
    heatmap_data, 
    cmap='coolwarm', 
    linewidths=.5, 
    linecolor='black',
    vmin=0,  
    vmax=1.8,   
    cbar_kws={'label': 'Points Per Shot (PPS)'}, 
    annot=True, 
    annot_kws={"size": 8},  
)
cbar = ax.collections[0].colorbar
cbar.set_label('Points Per Shot (PPS)', labelpad=20)
plt.title('Points Per Shot (PPS) by Player and Zone for 23-24 Denver Nuggets')
plt.xlabel('Zone', labelpad = -25)
plt.ylabel('Player')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()