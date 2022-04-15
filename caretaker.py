import pandas as pd
import requests
import re

df = pd.read_csv('data/caretakers.csv')


for i in range(len(df)):
    body = {
        'first_name': df.iloc[i]['Firstname'],
        'last_name': df.iloc[i]['Lastname'],
        'address': df.iloc[i]['Address'],
        'email': 'hutnik.markus@uwlax.edu',
        'password': 'abc123$',
        'phone_number': re.sub('\(|\)|\s+|-', '', df.iloc[i]['Phone']),
        'group': 'caretaker'
    }

    requests.post('http://localhost:8000/api/auth/easy_reg', data=body)
