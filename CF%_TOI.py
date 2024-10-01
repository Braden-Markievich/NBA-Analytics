import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('CF%_TOI.csv')
players = df['Player']
cf_rel = df['CF% Rel']
toi = df['Weighted EV TOI'] * 500  
plt.figure(figsize=(10, 6))
scatter = plt.scatter(players, cf_rel, s=toi, c=cf_rel, cmap='coolwarm', alpha=0.6)
cbar = plt.colorbar(scatter)
cbar.set_label('Even Strength CF% Rel', rotation = 90, fontsize=12)
plt.title('Measuring Even Strength CF% Rel and Weighted Even Strength TOI of the 2023-24 Washington Capitals', fontsize=16) 
plt.xlabel('Players', fontsize=12)
plt.ylabel('Even Strength CF% Rel', fontsize=12)
plt.xticks(rotation=85)

plt.tight_layout()
plt.show()
