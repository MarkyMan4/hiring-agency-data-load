import pandas as pd
import requests
import re  #library for regex stuff
from datetime import datetime

df = pd.read_csv('data/hp.csv');  #dataframe

salary_lookup = {
    1: {
        1: {
            'low': 35.00,
            'high': 40.00
        },
        2: {
            'low': 40.00,
            'high': 45.00
        }
    },
    2: {
        1: {
            'low': 40.00,
            'high': 50.00
        },
        2: {
            'low': 50.00,
            'high': 60.00
        }
    },
    3: {
        2: {
            'low': 100.00,
            'high': 125.00
        },
        3: {
            'low': 150.00,
            'high': 200.00
        }
    }
}


for i in range(len(df)):
    yoe = int(df.iloc[i]['Years of experience'])
    service_type = int(df.iloc[i]['Type'])
    education_type = int(df.iloc[i]['Education'])

    salary_range = salary_lookup[service_type][education_type]

    if yoe <= 4:
        hourly_rate = salary_range['low']
    else:
        hourly_rate = salary_range['high']

    body = {
        'first_name' : df.iloc[i]['Firstname'],
        'last_name' : df.iloc[i]['Lastname'] ,
        'address' : df.iloc[i]['Address'],
        'gender' : df.iloc[i]['Gender'],
        'graduation_month' : df.iloc[i]['Month'],
        'graduation_year' : df.iloc[i]['Year'],
        'years_of_experience' : df.iloc[i]['Years of experience'],
        'email' : 'hutnik.markus@uwlax.edu',
        'password': 'abc123$',
        'phone_number' : re.sub('\(|\)|\s+|-', '', df.iloc[i]['Phone']) ,  #rexex replace
        'date_of_birth': datetime.strptime(df.iloc[i]['Date of birth'], '%b %d,%Y').strftime('%Y-%m-%d'),
        'ssn': df.iloc[i]['SSN'],
        'service_type': df.iloc[i]['Type'],
        'education_type': df.iloc[i]['Education'],
        'education_institution': df.iloc[i]['Institution'],
        'hourly_rate': hourly_rate,
        'group' : 'healthcareprofessional'
    }
    
    requests.post('http://localhost:8000/api/auth/easy_reg', data=body)