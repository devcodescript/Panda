import pandas as pd
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380, 370, 24, 26],
                   'Max Speed2': [38, 37, 2, 6],
                   'Max Speed3': [1, 2, 2, 4]})

print(df)
heroes_publisher = df.set_index('Max Speed3') # Max Speeed3 all value will appear as Index default index will remove
print(heroes_publisher.head())
defaultindex=df.reset_index() # Rest index  but two index will appear
defaultindex=df.reset_index(drop='true') # Reset index same As Previous default index
print(defaultindex)
#groups=df.groupby(['Animal']).max()
#print(groups)