### IMPORT TO DATAFRAME ###
# SERFF excel file is transposed, so using .T at end
pd.read_csv('kaiser.csv', index_col=0, header=None).T

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

# remove "Exchange" column
del df_on['Exchange']
del df_off['Exchange']

# groupby Plan_Name and sum member months
df_on_grouped = df_on.groupby('Plan_Name', as_index=False)[['Metal', 'AV', 'Category', 'Network', 'Plan_Adjusted_Index_Rate', 'Member_Months']].agg({'Metal':'first', 'AV':'first', 'Category':'first', 'Network':'first', 'Plan_Adjusted_Index_Rate':'first', 'Member_Months':'sum'})
df_off_grouped = df_off.groupby('Plan_Name', as_index=False)[['Metal', 'AV', 'Category', 'Network', 'Plan_Adjusted_Index_Rate', 'Member_Months']].agg({'Metal':'first', 'AV':'first', 'Category':'first', 'Network':'first', 'Plan_Adjusted_Index_Rate':'first', 'Member_Months':'sum'})

### onvert string to category ###
# Convert Metal from string object to category
df.Metal = df.Metal.astype('category')
# Convert "Category" column from string object to category
df.Category = df.Category.astype('category')
# Convert "Network" column from string object to category
df.Network = df.Network.astype('category')
# Convert "Exchange" column from string object to category
df.Exchange = df.Exchange.astype('category')

### SAVE ###
# Save a .csv of this dataframe as backup
df.to_csv('kaiser.csv', index=False, encoding='utf8')