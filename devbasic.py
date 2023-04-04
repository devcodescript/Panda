import pandas as pd
data=pd.read_csv(r'pending_records.csv')
#data=pd.read_csv('pokemon.csv')
#data=pd.read_csv('Gocall.csv');

col=data[['mobile_no','bank_account_no']] # Fetch Multipal column records user list['column1','column2','column3'] inside the  function data
col=data['mobile_no'] # Fetch Single column records

datatype=data.dtypes # dttypes use for display all colums datatype
describe=data.describe() # describe() provide details of data like total, avg, median,Min, Max, Percentage
data.columns # Read all coiumns from data

print(describe)

#head() to find top / last  records ex: head(4) means top 4 , head(-4) from last 4 records
#print(data.head())