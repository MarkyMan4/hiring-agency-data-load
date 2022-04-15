import pandas as pd

df = pd.read_csv('data/partialassignments.csv');  #dataframe

for col in df.columns:
    df[col] = df[col].fillna('null')

with open('sql/assignment_inserts.sql', 'w') as outfile:
    for i in range(len(df)):
        outfile.write('insert into agency_api_serviceassignment (healthcare_professional_id, service_request_id) values (')
        rec = df.iloc[i]

        outfile.write(f'{rec["hp_id"]}, ')
        outfile.write(f'{rec["serv_req_id"]}')
        outfile.write(');\n')