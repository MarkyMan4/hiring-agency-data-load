import pandas as pd
from datetime import datetime

df = pd.read_csv('data/workreported.csv');  #dataframe

for col in df.columns:
    df[col] = df[col].fillna('null')

with open('sql/service_entry_inserts.sql', 'w') as outfile:
    for i in range(len(df)):
        outfile.write('insert into agency_api_serviceentry (start_time, end_time, billing_account_id, healthcare_professional_id, date_of_service) values (')
        rec = df.iloc[i]
        date = datetime.strptime(rec['Date'], '%b %d,%Y').strftime('%Y-%m-%d')

        outfile.write(f'\'{rec["Start"]}\', ')
        outfile.write(f'\'{rec["End"]}\', ')
        outfile.write(f'{rec["billing_acct_id"]}, ')
        outfile.write(f'{rec["hp_id"]}, ')
        outfile.write(f'\'{date}\'')
        outfile.write(');\n')