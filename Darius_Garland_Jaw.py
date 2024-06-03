import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



pre_jaw = { 
    'x': [2.5, 7.5, 12.5, 17.5, 22.5, 27.5],
    'y': [57.6, 51.7, 47.2, 42.3, 50, 35.1]
}

after_jaw = {
    'x': [2.5, 7.5, 12.5, 17.5, 22.5, 27.5],
    'y': [55.3, 32.2, 57.4, 37.5, 39.3, 40.9]      ############ Efficiency
}
df1 = pd.DataFrame(pre_jaw)
df2 = pd.DataFrame(after_jaw)

plt.scatter(df1['x'], df1['y'], color = 'red', label = 'Pre-jaw injury (10/25 - 12/14)')
plt.scatter(df2['x'], df2['y'], color = 'blue', label = 'Post-jaw injury (1/31 - 4/14)')
plt.plot(df1['x'], df1['y'], color = 'red', marker = 'o')
plt.plot(df2['x'], df2['y'], color = 'blue', marker = 'o')
plt.xlabel('Shot Distance (ft.)')
plt.ylabel('Field Goal Percentage (FG%)')
plt.legend()
plt.show()




pre_jaw = { 
    'x': [2.5, 7.5, 12.5, 17.5, 22.5, 27.5],
    'y': [4.6, 2.9, 1.8, 1.3, 1.3, 3.7]
}

after_jaw = {
    'x': [2.5, 7.5, 12.5, 17.5, 22.5, 27.5],
    'y': [3.1, 1.6, 1.3, 1.1, 1.6, 4.9]
}
df1 = pd.DataFrame(pre_jaw)
df2 = pd.DataFrame(after_jaw)                ############### Field Goals Attempted per Game

plt.scatter(df1['x'], df1['y'], color = 'red', label = 'Pre-jaw injury (10/25 - 12/14)')
plt.scatter(df2['x'], df2['y'], color = 'blue', label = 'Post-jaw injury (1/31 - 4/14)')
plt.plot(df1['x'], df1['y'], color = 'red', marker = 'o')
plt.plot(df2['x'], df2['y'], color = 'blue', marker = 'o')
plt.xlabel('Shot Distance (ft.)')
plt.ylabel('Field Goals Attempted per Game (FGA)')
plt.legend()
plt.show()