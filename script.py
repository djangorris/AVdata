import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches
from matplotlib import style
import numpy as np

style.use('fivethirtyeight')
np_members = np.array(df.Member_Months * .01)
col = df.Select.map({'On':'b', 'Off':'r'})
red_patch = mpatches.Patch(color='red', label='Off Exchange')
blue_patch = mpatches.Patch(color='blue', label='On Exchange')
# green_patch = mpatches.Patch(color='green', label='On Exchange (Select Network*)')
# yellow_patch = mpatches.Patch(color='yellow', label='Off Exchange (Select Network*)')
df.plot.scatter('AV', 'Plan_Adjusted_Index_Rate', s=np_members, marker='o', c=col, edgecolor='black')
plt.xlabel('Actuarial Value (AV)')
plt.ylabel('Plan Adjusted Index Rate')
plt.title('Kaiser Permanente\nVisualizing Plan Popularity (Marker Size)\nMeasured in Member Months')
plt.grid(True)
plt.legend(handles=[red_patch, blue_patch, green_patch, yellow_patch])
plt.show()

