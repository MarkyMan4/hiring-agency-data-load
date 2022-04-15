import pandas as pd

df = pd.read_csv('data/jobpostings.csv');  #dataframe

for col in df.columns:
    df[col] = df[col].fillna('null')

with open('sql/job_posting_inserts.sql', 'w') as outfile:
    for i in range(len(df)):
        outfile.write('insert into agency_api_jobposting (years_experience_required, education_type_id, service_type_id, description) values (')
        rec = df.iloc[i]
        desc = rec["Description"].replace("'", "''")

        outfile.write(f'{rec["years_experience"]}, ')
        outfile.write(f'{rec["Education"]}, ')
        outfile.write(f'{rec["Type"]}, ')
        outfile.write(f'\'{desc}\'')
        outfile.write(');\n')