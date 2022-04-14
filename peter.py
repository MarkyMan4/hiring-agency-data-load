import pandas as pd
import requests
import re  #library for regex stuff
df = pd.read_csv('data/hp.csv');  #dataframe

print (df)

for i in range(len(df)):
    body = {
        'first_name' : df.iloc[i]['Firstname'],
        'last_name' : df.iloc[i]['Lastname'] ,
        'address' : df.iloc[i]['Address'],
        'gender' : df.iloc[i]['Gender'],
        'month' : df.iloc[i]['Month'],
        'year' : df.iloc[i]['Year'],
        'years_of_experience' : df.iloc[i]['Years of experience'],
        'email' : 'hutnik.markus@uwlax.edu',
        'password': 'abc123$',
        'phone_number' : re.sub('(|)|\s+|-', '', df.iloc[i]['Phone']) ,  #rexex replace
        'group' : 'healthcare_professional'
    }
    
    requests.post('http://loaclhost:8000/api/auth/easy_reg', data=body)