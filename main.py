import pandas as pd

df = pd.read_csv('staff.csv')

for rec in df.iterrows():
    print(rec)
