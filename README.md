# Baby Name Trends Analysis

An exploration of U.S. baby naming patterns over time, using historical datasets.  


## Overview
This project analyzes trends in baby names over the last 100 years.  
Key questions:
- Are parents choosing from a larger pool of names today than in the past?
- How is the popularity of the top 10 names changing each year?
- How has the usage of unisex names changed over time?
- Are names getting longer or shorter over the decades?

## Preparing Data
The dataset comes from the U.S. Social Security Administration baby names files (yobYYYY.txt).
Each file contains all registered baby names for a given year, split by gender, along with the number of babies given that name.

Steps taken to prepare the data:
- Load raw files – All yearly text files (yobYYYY.txt) were read in using pandas and glob.
- Add year column – The year was extracted from each filename and stored as 'yob'.
- Combine into one dataset – All yearly data was concatenated into a single DataFrame 'names_df'.
- Quality checks – Verified there were no missing values or duplicate rows.
- Save processed file – Exported the cleaned dataset to names_processed.csv for later analysis.

## Findings
### Unique Names per Year
![Total Names per Year](Plots/"Names per Year.png")

### Percent of Top 10 vs Top 1 Names
![top10-vs-top1](plots/top10_top1.png)

### Percent of Unisex Names
![unisex](plots/unisex.png)

### Average Length of Top 10 Names
![avg-length](plots/avg_length.png)

## Tools Used
- **Python**: data processing and analysis  
- **Pandas**: grouping, aggregations  
- **Seaborn & Matplotlib**: visualizations 
