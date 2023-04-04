import pandas as pd
import mysql.connector as mc
myco = mc.connect(host="database-1.c5vd49th5mxz.us-east-1.rds.amazonaws.com",user="consoleflare",passwd="Console123",database="infobase")
q = 'select * from infotable'
df = pd.read_sql(q,myco)
print(df)