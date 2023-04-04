import pandas as pd

#df=pd.read_csv(r'pokemon.csv')
#head=["#","Name","Type 1","Type 2","HP","Attack","Defense","Sp. Atk","Sp. Def","Speed","Generation","Legendary"]
#df = pd.read_csv(r"Pokemon.csv",names=head)

df = pd.read_csv('Pokemon.csv', delimiter=',')
a=df.columns
b=df.dtypes
c=df.describe()
d=df.iloc[0:20,1:7] # 0-20 row (Total 20 rows) and column 1 to 7 records will fetch
e=df.iloc[:,0:5] # All rows with 5 columns
f=df.iloc[0:1,:] # Single row with all columns
#print(a)
# Iteration Over Rows Using iterrows() Function :
#for index, row in df.iterrows():
    #print(index, row['Speed'])
#for (colname, colval) in df.iteritems():
    #print(colname)
#Filtering Data in Pandas DataFrame Using loc[] :
filtered_df=df.loc[df['Type 1'] != "Grass"] # where Type 1 Value is Grass
filtered_df1 = df.loc[df['Speed'] > 130] # Where Speed Greater than 130

filtered_df2=df.sort_values(['Type 1']) # soring the values of column by Default ascending order
filtered_df3=df.sort_values(['Type 1'],ascending=False) # ascending=False Means sorting by descending
# Sort Multipal column in Ascending and Descending order(We can also use 1 and 0 instead of True and False.)
filtered_df4=df.sort_values(['Name','Type 1','Type 2','Speed'],ascending=[False,True,True,False])
#print(filtered_df4)

# Method1 create a new Column named total_sum , that is addition of HP,Attack,Defense,Sp.atk,Sp.def,Speed,Generation.
df['total_sum'] = df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
gg=df['total_sum']
d1=df.iloc[0:20,7:14] # display 20 row and last 7 columns
aa=df.columns # Display all columns
# Method2 create a new Column named total_sum2 , that is addition of HP,Attack,Defense,Sp.atk,Sp.def,Speed,Generation.
df['total_sum2'] = df.iloc[:,6:11].sum(axis=1)
#df['total_sum2']
dd1=df.iloc[0:20,7:15] # display 20 row and last 7 columns
aa2=df.columns # Display all columns
print(aa2)

#gb=df.groupby('Generation')
gb=df.groupby(['Type 1','Type 2']).count()['total_sum']
print(gb)
#new_df = df.drop(columns=['Generation']) # Delete column form sheet
#new_df.reset_index(drop=True,inplace=True) # reset Index

#filtered_df = df.loc[((df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')) & (df['HP'] > 70)]


#gb=df.groupby(['Type 1', 'Type 2']).count()['count']
#print(gb)


#col=df[['HP','Name','Type 1']]
#print(col)
#print(df.head(5))
#df=pd.read_csv('pokemon.csv',names=head)
#print(df.head())
#print(df)
