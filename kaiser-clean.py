### CURRENTLY WORKS ON EXISTIG 'kaiser.csv' 9/6/17
import pandas as pd

### FIRST, REMOVE EXTRA ROWS AND COLUMNS IN NUMBERS AND EXPORT TO CSV ###
### IMPORT TO DATAFRAME ###
# SERFF excel file is transposed, so using .T at end
# df = pd.read_csv('kaiser.csv', index_col=0, header=None).T
# REMOVE THE .T IF IT'S ALREADY TRANSPOSED
df = pd.read_csv('kaiser.csv')

### CLEAN ###
# change column names
# df.columns = ['Plan_Name', 'Metal', 'AV', 'Category', 'Network', 'Exchange', 'Plan_Adjusted_Index_Rate', 'Member_Months']

# Convert AV from string object to float
# df.AV = df.AV.astype(float).fillna(0.0)

# Convert "Plan_Adjusted_Index_Rate" column from string object to float
# df.Plan_Adjusted_Index_Rate = df.Plan_Adjusted_Index_Rate.replace('[\$,]', '', regex=True).astype(float)

# Convert Member_Months from string object to int
# df.Member_Months = df.Member_Months.str.replace(',', '').astype(int).fillna(0)

# separate ON and OFF exchange
df_on = df[df.Exchange == 'Yes']
df_off = df[df.Exchange == 'No']

# round AV column to 3 decimal places
df_on['AV'] = df_on.loc[:,'AV'].round(3)
df_off['AV'] = df_off.loc[:,'AV'].round(3)

# remove "Exchange" column
del df_on['Exchange']
del df_off['Exchange']

# round AV column to 3 decimal places
df_on.AV = df.AV.round(3)
df_off.AV = df.AV.round(3)

# groupby Plan_Name and sum member months
df_on_grouped = df_on.groupby('Plan_Name', as_index=False)[['Metal', 'AV', 'Category', 'Network', 'Plan_Adjusted_Index_Rate', 'Member_Months']].agg({'Metal':'first', 'AV':'first', 'Category':'first', 'Network':'first', 'Plan_Adjusted_Index_Rate':'first', 'Member_Months':'sum'})
df_off_grouped = df_off.groupby('Plan_Name', as_index=False)[['Metal', 'AV', 'Category', 'Network', 'Plan_Adjusted_Index_Rate', 'Member_Months']].agg({'Metal':'first', 'AV':'first', 'Category':'first', 'Network':'first', 'Plan_Adjusted_Index_Rate':'first', 'Member_Months':'sum'})

### onvert string to category ###
# Convert Metal from string object to category
df_on_grouped.Metal = df_on_grouped.Metal.astype('category')
df_off_grouped.Metal = df_off_grouped.Metal.astype('category')
# Convert "Category" column from string object to category
df_on_grouped.Category = df_on_grouped.Category.astype('category')
df_off_grouped.Category = df_off_grouped.Category.astype('category')
# Convert "Network" column from string object to category
df_on_grouped.Network = df_on_grouped.Network.astype('category')
df_off_grouped.Network = df_off_grouped.Network.astype('category')

### SAVE ###
# Save a .csv of this dataframe as backup
df_on_grouped.to_csv('kaiser_on.csv', index=False, encoding='utf8')
df_off_grouped.to_csv('kaiser_off.csv', index=False, encoding='utf8')

# Combine into single dataframe for plotting
df = kp_on_grouped.append(kp_off_grouped)