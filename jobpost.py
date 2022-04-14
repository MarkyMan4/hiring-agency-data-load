import pandas as pd
import requests
import re  #library for regex stuff
df = pd.read_csv('data/jobpostings.csv');  #dataframe

print (df)

for i in range(len(df)):
    body = {
        'type' : df.iloc[i]['type'],
        'education' : df.iloc[i]['education'] ,
        'Number of years of exeprience required' : df.iloc[i]['Number of years of exeprience required'],
        'Description' : df.iloc[i]['Description'],
        'group' : 'jobpostings'
    }
    
    requests.post('http://loaclhost:8000/api/auth/easy_reg', data=body)