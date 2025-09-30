import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

names_df = pd.read_csv(r"C:\Users\Champion\Desktop\DataProjects\names_processed.csv")

## Total Names by Year
total_names = names_df.groupby('yob')['count'].sum().reset_index()

plt.figure(figsize=(14,8))
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
sns.lineplot(data=total_names, x='yob', y='count')
plt.title('Names per Year')
plt.xlabel('Year')
plt.ylabel('Total Number of Names')
plt.xticks(range(1925,2024,5),rotation = 90)
plt.ticklabel_format(style='plain', axis='both')
plt.show()
totals = (total_names[total_names['yob'].isin([1925, 1975, 2024])].groupby('yob')['count'].sum())
print('TOTALS --- ',totals)


## Number of Unique Names per Year
uNames_byYear = names_df.groupby('yob')['name'].nunique().reset_index(name='count')

plt.figure(figsize=(14,8))
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
sns.lineplot(uNames_byYear, x='yob',y='count')
plt.title('Unique Names per Year')
plt.xlabel('Year')
plt.ylabel('Number of Unique Names')
plt.xticks(range(1925,2024,5),rotation = 90)
plt.ticklabel_format(style='plain', axis='both')
plt.show()
uTotals = uNames_byYear.loc[uNames_byYear['yob'].isin([1925, 1975, 2024])]
print('uTotals --- ',uTotals)


## Percent of top names each year
total_perYear = names_df.groupby('yob')['count'].sum().reset_index(name='total')
top10_perYear = names_df.groupby('yob').apply(lambda x: x.nlargest(10,'count')).reset_index(drop=True)
top1_perYear = names_df.groupby('yob').apply(lambda x: x.nlargest(1,'count')).reset_index(drop=True)
top1_totals = top1_perYear.groupby('yob')['count'].sum().reset_index(name='top1_total')
top10_totals = top10_perYear.groupby('yob')['count'].sum().reset_index(name='top10_total')
merged_top10 = pd.merge(total_perYear,top10_totals,on='yob')
merged_top = pd.merge(merged_top10,top1_totals,on='yob')
merged_top['top10_percent'] = merged_top['top10_total'] / merged_top['total']*100
merged_top['top1_percent'] = merged_top['top1_total'] / merged_top['total']*100

plt.figure(figsize=(14,8))
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
sns.barplot(data=merged_top,x='yob',y='top10_percent',label="Top 10")
sns.barplot(data=merged_top,x='yob',y='top1_percent',label="Top 1")
plt.title('Percent of Top 10 Names per Year')
plt.xlabel('Year')
plt.ylabel('Percent of Total Names')
plt.xticks(rotation = 90)
plt.ticklabel_format(style='plain', axis='y')
plt.show()
print('TOP 10 %\n',merged_top.loc[merged_top['yob'].isin([1925, 1975, 2024]),'top10_percent'])
print('TOP 1 %\n',merged_top.loc[merged_top['yob'].isin([1925, 1975, 2024]),'top1_percent'])

#- Total of top names each year
plt.figure(figsize=(14,8))
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
sns.barplot(data=merged_top,x='yob',y='top10_total',label="Top 10")
sns.barplot(data=merged_top,x='yob',y='top1_total',label="Top 1")
plt.title('Total of Top 10 Names per Year')
plt.xlabel('Year')
plt.ylabel('Percent of Total Names')
plt.xticks(rotation = 90)
plt.ticklabel_format(style='plain', axis='y')
plt.show()
print('TOP 10 Total\n',merged_top.loc[merged_top['yob'].isin([1925, 1975, 2024]),'top10_total'])
print('TOP 1 Total\n',merged_top.loc[merged_top['yob'].isin([1925, 1975, 2024]),'top1_total'])


## Gendered names and nutrality
F_names = names_df[names_df['sex']=='F']
M_names = names_df[names_df['sex']=='M']

both = pd.merge(F_names, M_names, how='inner', on=['name','yob'],suffixes=('_F','_M'))
both['total_B'] = both['count_F'] + both['count_M']
both = both[((both['count_F'] / both['total_B']) > 0.1) & ((both['count_M'] / both['total_B']) > 0.1)]
print(both.head())
both = both.groupby('yob')['total_B'].sum()


total_perYear = names_df.groupby('yob')['count'].sum().reset_index(name='total')
both = pd.merge(both,total_perYear,on='yob')
print(both.head())
both['both_percent'] = both['total_B'] / both['total']*100

plt.figure(figsize=(14,8))
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
sns.barplot(data=both,x='yob',y='both_percent')
plt.title('Percent of Names that were Unisex')
plt.xlabel('Year')
plt.ylabel('Percent of Unisex Names')
plt.xticks(rotation = 90)
plt.ticklabel_format(style='plain', axis='y')
plt.show()
print('Both Percent ---\n',both.loc[both['yob'].isin([1925, 1975, 2024]),'both_percent'])


## Average Length of Name by Year
names_df['length'] = int(names_df['name'].str.len())
med_len_byYear = names_df.groupby('yob')['length'].median().round().reset_index(name='avg_len')
plt.figure(figsize=(14,8))
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
sns.barplot(data=med_len_byYear,x='yob',y='avg_len')
plt.title('Median Length of Names by Year')
plt.xlabel('Year')
plt.ylabel('Avg. Length of Names')
plt.xticks(rotation = 90)
plt.ticklabel_format(style='plain', axis='y')
plt.show()


#- Average Length of the Top 10 Names
top10_perYear = names_df.groupby('yob').apply(lambda x: x.nlargest(10,'count')).reset_index(drop=True)
top10_perYear['length'] = top10_perYear['name'].str.len()
print(top10_perYear.head())
med_len_byYear = top10_perYear.groupby('yob')['length'].median().round().reset_index(name='avg_len')
plt.figure(figsize=(14,8))
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
sns.barplot(data=med_len_byYear,x='yob',y='avg_len')
plt.title('Median Length of Names by Year')
plt.xlabel('Year')
plt.ylabel('Avg. Length of Names')
plt.xticks(rotation = 90)
plt.ticklabel_format(style='plain', axis='y')
plt.show()

