import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches
from matplotlib import style
import numpy as np
###
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches
from matplotlib import style
import numpy as np

### FIRST, REMOVE EXTRA ROWS AND COLUMNS IN NUMBERS AND EXPORT TO CSV ###
### Should have rows in order ['Plan Name', Metal', 'AV Metal Value', 'Category', 'Plan Type', 'Exchange Plan?', Plan_Adjusted_Index_Rate', 'Member_Months']]
### IMPORT TO DATAFRAME ###
# SERFF excel file is transposed, so using .T at end

#Change Carrier
carrier = 'cigna'
df = pd.read_csv(carrier + '.csv', index_col=0, header=None).T
# REMOVE THE .T IF IT'S ALREADY TRANSPOSED
# df = pd.read_csv(carrier + '.csv')
### CLEAN ###
# change column names
df.columns = ['Plan_Name', 'Metal', 'AV', 'Category', 'Network', 'Exchange', 'Plan_Adjusted_Index_Rate', 'Member_Months']
# Convert AV from string object to float
df.AV = df.AV.astype(float).fillna(0.0)
# Convert "Plan_Adjusted_Index_Rate" column from string object to float
df.Plan_Adjusted_Index_Rate = df.Plan_Adjusted_Index_Rate.replace('[\$,]', '', regex=True).astype(float)
# Convert Member_Months from string object to int
df.Member_Months = df.Member_Months.str.replace(',', '').astype(int).fillna(0)
# separate ON and OFF exchange
df_on = df[df.Exchange == 'Yes']
df_off = df[df.Exchange == 'No']
# round AV column to 3 decimal places
df_on.AV = df.AV.round(3)
df_off.AV = df.AV.round(3)
# groupby Plan_Name and sum member months
df_on_grouped = df_on.groupby('Plan_Name', as_index=False)[['Metal', 'AV', 'Category', 'Network', 'Exchange', 'Plan_Adjusted_Index_Rate', 'Member_Months']].agg({'Metal':'first', 'AV':'first', 'Category':'first', 'Network':'first', 'Exchange':'first', 'Plan_Adjusted_Index_Rate':'first', 'Member_Months':'sum'})
df_off_grouped = df_off.groupby('Plan_Name', as_index=False)[['Metal', 'AV', 'Category', 'Network', 'Exchange', 'Plan_Adjusted_Index_Rate', 'Member_Months']].agg({'Metal':'first', 'AV':'first', 'Category':'first', 'Network':'first', 'Exchange':'first', 'Plan_Adjusted_Index_Rate':'first', 'Member_Months':'sum'})
# Convert "Exchange" column from string object to category
df_on_grouped.Exchange = df_on_grouped.Exchange.astype('category')
df_off_grouped.Exchange = df_off_grouped.Exchange.astype('category')
### SAVE ###
# Save a .csv of this dataframe as backup
df_on_grouped.to_csv(carrier + '_on.csv', index=False, encoding='utf8')
df_off_grouped.to_csv(carrier + '_off.csv', index=False, encoding='utf8')
# Combine into single dataframe for plotting
df = df_on_grouped.append(df_off_grouped, ignore_index=True)
df.to_csv(carrier + '_cleaned.csv', index=False, encoding='utf8')
############
### PLOT ###
############
style.use('fivethirtyeight')
np_members = np.array(df.Member_Months * .05)
col = df.Exchange.map({'Yes':'b', 'No':'r'})
red_patch = mpatches.Patch(color='red', label='Off Exchange')
blue_patch = mpatches.Patch(color='blue', label='On Exchange')
# green_patch = mpatches.Patch(color='green', label='On Exchange (Select Network*)')
# yellow_patch = mpatches.Patch(color='yellow', label='Off Exchange (Select Network*)')
df.plot.scatter('AV', 'Plan_Adjusted_Index_Rate', s=np_members, marker='o', c=col, edgecolor='black')
plt.xlabel('Actuarial Value (AV)')
plt.ylabel('Plan Adjusted Index Rate')
plt.title(carrier.title() + '\nVisualizing Plan Popularity (Marker Size)\nMeasured in Member Months')
plt.grid(True)
plt.legend(handles=[red_patch, blue_patch])
plt.show()