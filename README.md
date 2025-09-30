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
### Names per Year
When looking at the total number of babies recorded each year, the counts fluctuate but overall show growth.  
- Compared to 50 years ago, total births have increased by about **10%**.  
- Compared to 100 years ago, they’ve risen by about **42%**. 
![Total Names per Year](Plots/Names_per_Year.png)

When we shift focus from total births to the number of **unique names** (the total variety of different names given each year), a trend emerges:  
- Over the past 50 years, the number of unique names has grown by about **89%**.  
- Over the past 100 years, that growth is an impressive **207%**.
There is a small dip in the last 15 years, but the overall long-term trend shows that parents are drawing from a **much wider pool of names** than in the past.
![Unique Names per Year](Plots/Unique_Name_per_Year.png)
While the *total number* of names only grew by 42% in 100 years, the *variety of names* grew by over 200%. This points to a strong cultural shift: parents today are far more likely to choose **unique, less common names** for their children, leading to the larger name pool.

### Popularity of Top 10 and Top 1 Names
Briefly, there's a graph showing the total number of names of the top 10 most popular names each year. Even with the total number of names rising over the last 100 years, as mentioned, the total number of the top 10 names, while having an increase around 1947 and 1982, has trended downward.
![Total of Top10 Names per Year](Plots/Total_of_Top_10_Names_per_Year.png)

Seen more clearly when looking at the percent of the top 10 names compared to the total population. The trend is more consistent, seeing the previous increase most likely due to a rise in population and not to an increase in name popularity. You can also see a similar trend in the number 1 most popular name each year.
![Percentage of Top10 Names per Year](Plots/Percent_of_Top_10_Names_per_Year.png)
With the top 10 names going from 19.3% of the total population in 1925 down to 4.4% in 2024, there isnt just a case of the popluar names being over run by the new names, but the popular names are less popular.

### Usage of Unisex Names

![Percent of Unisex](Plots/Percent_of_Names_that_were_Unisex.png)

### Average Length of Names

![avg-length](Plots/Median_Length_of_Names_by_Year.png)

![avg-length](Plots/Median_Length_of_the_Top_10_Names_by_Year.png)

## Tools Used
- **Python**: data processing and analysis  
- **Pandas**: grouping, aggregations  
- **Seaborn & Matplotlib**: visualizations 
