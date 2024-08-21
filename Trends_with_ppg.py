import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('trends_with_ppg.csv')
x_axis = df['SEASON']
left_y_axis = df['PPG']
right_y_axis_3PAr = df['3PAr']
right_y_axis_Pace = df['Pace']
right_y_axis_FTr = df['FTr']
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(16, 18), dpi=80, sharex=True)

ax1.plot(x_axis, left_y_axis, color='tab:red', linewidth=2, label='PPG')
ax1.set_ylabel('PPG', color='tab:red', fontsize=15)
ax1.tick_params(axis='y', labelcolor='tab:red')
ax1.grid(alpha=.4)
ax1_2 = ax1.twinx() 
ax1_2.plot(x_axis, right_y_axis_3PAr, color='tab:blue', label='3PAr')
ax1_2.set_ylabel('3PAr', color='tab:blue', fontsize=15)
ax1_2.tick_params(axis='y', labelcolor='tab:blue')

ax2.plot(x_axis, left_y_axis, color='tab:red', linewidth=2, label='PPG')
ax2.set_ylabel('PPG', color='tab:red', fontsize=15)
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.grid(alpha=.4)
ax2_2 = ax2.twinx()
ax2_2.plot(x_axis, right_y_axis_Pace, color='tab:green', label='Pace')
ax2_2.set_ylabel('Pace', color='tab:green', fontsize=15)
ax2_2.tick_params(axis='y', labelcolor='tab:green')

ax3.plot(x_axis, left_y_axis, color='tab:red', linewidth=2, label='PPG')
ax3.set_ylabel('PPG', color='tab:red', fontsize=15)
ax3.tick_params(axis='y', labelcolor='tab:red')
ax3.grid(alpha=.4)
ax3_2 = ax3.twinx() 
ax3_2.plot(x_axis, right_y_axis_FTr, color='tab:purple', label='FTr')
ax3_2.set_ylabel('FTr', color='tab:purple', fontsize=15)
ax3_2.tick_params(axis='y', labelcolor='tab:purple')

ax3.set_xlabel('Season', fontsize=20)
fig.suptitle('How 3PAr, Pace, and FTr measured with average team PPG over time (stats via Basketball-Reference)', fontsize=15)
fig.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.show()