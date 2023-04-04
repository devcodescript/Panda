import pandas as pd
pd.options.display.max_columns=None # Display all Columns of df 1: None Means no limit to display column

df=pd.read_csv('heroes.csv')
#df=df.shape # To display number of row and no of columns
#df=df.set_index('Publisher') # Reset Index and set New index of column
df=df.reset_index(drop=True) #Reset Index and drop previous index:

# Making a list of publishers to subset on
publishers=['Marvel Comics','DC Comics'] # will filter only those data that are in list
publishers=['Marvel Comics'] # will filter only those publisher that is 'Marvel Comics'
# Subset heroes using standard square brackets
df=df[df['Publisher'].isin(publishers)]

df_multi = df.set_index(['Alignment','Publisher'])
#df_multi=df.reset_index(drop=True)
#df_multi=df.reset_index('Gender')
df_multi=df_multi.sort_index()
df_multi=df_multi.loc['good':'bad']
df=df_multi.head()
print(df)
#print(aa)