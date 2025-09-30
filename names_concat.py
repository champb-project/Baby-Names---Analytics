import pandas as pd
import glob
import re

files = glob.glob("C:/Users/Champion/Desktop/DataProjects/names/yob*.txt")

dfs = []

for file in files:
    curr_df = pd.read_csv(file, header=None, names=['name', 'sex', 'count'])

    year = int(re.search('\d{4}',file).group())
    curr_df['yob'] = year

    dfs.append(curr_df)

names_df = pd.concat(dfs)
names_df.to_csv('C:/Users/Champion/Desktop/DataProjects/names_processed.csv',index=False)