# COVID-19 Multilanguage Tweets Dataset

The repository contains an ongoing collection of twee's IDs associated with the novel coronavirus (COVID-19) .
The dataset contains tweet's IDs dating from 22 January tp 13 March 2020 (total of 6,468,526 tweet's IDs). Twitte's Standard search API was used to gather historical tweets from 
multiple continents in multiple languages that containied a given keyword (virus and coronavirus since 22 January, 
ncov19 and ncov2019 since 26 February, and covid since 7 March 2020).
In order to comply with Twitter's [Terms of Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy), 
 only the tweet's IDs of the Tweets gathered are released for non-commercial research use only.

The paper associated with this dataset can be found here: **(Pending)**

## Data Organization
The tweet-IDs are organized by keywords as follows:
* TweetsID files are stored in folders that indicate the keyword used (i.e., coronavirus, virus, covid, ncov19, ncov2019). 
* The Tweet-ID file is a `.txt` containing individual Tweet-IDs stored as a comma-separated-list. The file names follow the naming convention of : `[Keyword]_yyyy_mm_dd.txt` (e.g., `coronavirus_2020_01_22.txt` contains the ids of tweets mentioning the keyword 'coronavirus' tweeted on January 22th, 2020).
* Since the Twitter API returns tweets in UTC, all tweet-ID folder and file names are all in UTC as well.


## Notes About the Data
* Not all keywords were tracked from the very beginning. As news about the novel coronavirus spread, 
additional keywords were added to the search list (virus and coronavirus since 22 January, 
ncov19 and ncov2019 since 26 February, and covid since 7 March 2020).
* Our dataset **does not** capture every single tweet on Twitter relating to the keywords as our data retrieval is restricted at 45,000 every 15 minutes by the Twitter API.
* We notice that there are fewer tweets relating to the novel coronavirus present in our dataset in the first few weeks than in the following weeks. This can explained by the fact that our data collection involved tracking other keywords unrelated to the coronavirus during the first few weeks. This meant that the number of coronavirus-related tweets were limited at a fraction of the total API limit. Once unrelated keywords were removed from our search options, the limit of coronavirus-related tweets became the total API limit, hence resulting in more tweets in our dataset.
* Our dataset is currently missing entries for Feb 06, 2020 and Feb 07, 2020. This data was lost due to technical errors. We currently are
working on retrieving the lost data.
* We currently have some descriptive statistics about our dataset displayed in the paper associated with it. We are working on 
automatically updating these statistics with every update of the dataset.
* Consider using tools such as the [Hydrator](https://github.com/DocNow/hydrator) and [Twarc](https://github.com/DocNow/twarc) to 
rehydrate the tweet-IDs i.e. to fetch tweet data associated with the tweet-IDs using Twitter's API. 

## Hydrating Tweets

The Twitter API's rate limits pose an issue to fetch data from tweed-IDs. So, we recommended using Hydrator to convert the list of tweed-IDs, into a CSV file containing all data and meta-data relating to the tweets. Hydrator also manages Twitter API Rate Limits for you. 

For those who prefer a command line interface over a GUI, we recommend using Twarc.

### Using [Hydrator](https://github.com/DocNow/hydrator)
Follow the instructions on the [Hydrator github repository](https://github.com/DocNow/hydrator).

### Using [Twarc](https://github.com/DocNow/twarc) (CLI)
Follow the instructions on the [Twarc github repository](https://github.com/DocNow/twarc). 
1. First follow instructions for [installation](https://github.com/DocNow/twarc#Install). 
2. Then, obtain your Twitter API token ([apply](https://developer.twitter.com/en/apply-for-access) for a Twitter developer account).
3. Configure twarc with your API token by following the instructions for [configuration](https://github.com/DocNow/twarc#Quickstart).
4. Follow instructions in the [Hydrate section](https://github.com/DocNow/twarc#hydrate). Hydrated tweets are stored in [jsonl](http://jsonlines.org/) files. 


## Current Statistics (Pending)

The following are as of **(Date)**.

Number of Tweets: **(Pending)**.

Language Breakdown **(Pending)**.

## Inquiries

For questions about the dataset, please contact Dr. Christian Lopez at **lopezbec@lafayette.edu** 

## Licensing
This dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)). By using this dataset, you agree to abide by the stipulations in the license, remain in compliance with Twitterâs [Terms of Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy), and cite the following manuscript: 

