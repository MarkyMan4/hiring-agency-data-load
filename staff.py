import pandas as pd

df = pd.read_csv('data/staff.csv')



for rec in df.iterrows():
    print(rec)
