import pandas as pd
import re
from datetime import datetime

df = pd.read_csv('data/patients.csv')

for col in df.columns:
    df[col] = df[col].fillna('null')

with open('sql/serv_req_inserts.sql', 'w') as outfile:
    for i in range(len(df)):
        outfile.write('insert into agency_api_servicerequest (patient_first_name, patient_last_name, patient_gender, patient_date_of_birth, patient_phone_number, patient_email, service_location, service_start_time, service_end_time, service_needed_sunday, service_needed_monday, service_needed_tuesday, service_needed_wednesday, service_needed_thursday, service_needed_friday, service_needed_saturday, days_of_service, care_taker_id, service_type_id, flexible_hours, hours_of_service_daily, hp_gender_required, hp_max_age, hp_min_age, is_assigned, is_completed, start_date) values (')
        rec = df.iloc[i]
        phone = re.sub("\(|\)|\s+|-", "", rec["Phone"])
        addr = rec["Location/address"].replace("'", "''")
        dob = datetime.strptime(rec["Date of birth"], '%b %d,%Y').strftime('%Y-%m-%d')
        date_requested = datetime.strptime(rec["Date requested"], '%B %d,%Y').strftime('%Y-%m-%d')

        outfile.write(f'\'{rec["Firstname"]}\', ')
        outfile.write(f'\'{rec["Lastname"]}\', ')
        outfile.write(f'\'{rec["Gender"]}\', ')
        outfile.write(f'\'{dob}\', ')
        outfile.write(f'{phone}, ')
        outfile.write('\'hutnik.markus@uwlax.edu\', ')
        outfile.write(f'\'{addr}\', ')
        outfile.write(f'\'{rec["Start time"]}\', ')
        outfile.write(f'\'{rec["End time"]}\', ')
        outfile.write(f'{rec["service_needed_sunday"]}, ')
        outfile.write(f'{rec["service_needed_monday"]}, ')
        outfile.write(f'{rec["service_needed_tuesday"]}, ')
        outfile.write(f'{rec["service_needed_wednesday"]}, ')
        outfile.write(f'{rec["service_needed_thursday"]}, ')
        outfile.write(f'{rec["service_needed_friday"]}, ')
        outfile.write(f'{rec["service_needed_saturday"]}, ')
        outfile.write(f'{rec["Number of days"]}, ')
        outfile.write(f'{rec["caretaker_id"]}, ')
        outfile.write(f'{rec["Type of service"]}, ')
        outfile.write(f'{rec["flex_hours"]}, ')
        outfile.write(f'{rec["hours_of_service_daily"]}, ')
        outfile.write(f'{rec["hp_gender_required"]}, ')
        outfile.write(f'{rec["hp_max_age"]}, ')
        outfile.write(f'{rec["hp_min_age"]}, ')
        outfile.write(f'FALSE, ')
        outfile.write(f'FALSE, ')
        outfile.write(f'\'{date_requested}\'')
        outfile.write(');\n')
        