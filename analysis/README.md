# Tweets Analysis
In this subdirectory, you will find a series of analyses that have been performed on the dataset of tweets from January 22nd, 2020 until the date specified on the subdirectory/folder (e.g., in folder  “until_2020_04_12” the analysis is from all Tweets until 2020_04_12).
*After 2020_04_12, all analyses are performed at a keyword level (i.e., per keyword).
Before 2020_04_12, all the analysis aggregated using all the keywords. Also, no mention, sentiment, nor hashtag analysis are performed.
### Tweets_Number_by_Month.csv 
This file contains a table that shows the mean (M), standard deviation (SD), median, (Mdn) of the average daily tweets per month (Month) and category (Type). 
-	In the Month column, you will find a tag for each of the months contained on the datasets plus a tag “All_M” (i.e., all months), that show the aggregated statistics for all the months. 
-	In the “Type” columns, there are three tags: “All” (for all tweets”, “Org” (for original tweets”, “RT” (for re-tweets).
Lastly, there is a “NoDays” column that show the total number of days of tweets collected.
### SummaryTable.csv 
This file show summary statistics (total number, maximum, median, 25th percentile) for the GeoLocated, Likes and Retweets information.

### TweetLanguages.csv
This file contains information about the languages o the tweets collected organized in descending order. It contain 3 columns: Language (V1), Total number of tweets in that language (Freq), and percentage (Percentage). 

