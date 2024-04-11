import happybase as hb
import pandas as pd

con = hb.Connection('hbase-docker', 9090)
table = con.table('Users')
table.delete('666')
table.put('666', 
        {'Perso:name':'Renata','Perso:age':'40','Info:mail':'rdollerer@gmail.com'})


data = list(table.scan())
for key, info in data:
    print(key, info)



data = pd.read_csv("adult.csv")


con.create_table("adult",{"data":dict(in_memory=True)})
table = con.table(b'adult')

for ind,row in data.iterrows():
    n_row={("data:"+col):str(row[col]) for col in data.columns.values}
    table.put(str(ind),n_row)    
con.close()