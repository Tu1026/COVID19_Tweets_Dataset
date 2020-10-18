# COVID-19 Multilanguage Tweets Dataset

The repository contains an ongoing collection of tweets IDs associated
with the novel coronavirus COVID-19. The dataset contains Tweets’ ids
dating back to January 22th, 2020. The Twitter’s search API was used to
gather historical Tweets from multiple continents in multiple languages
that contained a given keyword (i.e., coronavirus, virus, covid, ncov19,
ncov2019). In order to comply with Twitter’s [Terms of
Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy),
only the Tweet IDs of the Tweets gathered are released for
non-commercial research use only.

The dataset is also on
Kaggle:[Covid19-tweets-dataset](https://www.kaggle.com/lopezbec/covid19-tweets-dataset)

**Citation**

Christian Lopez, Malolan Vasu, and Caleb Gallemore (2020) Understanding
the perception of COVID-19 policies by mining a multilanguage Twitter
dataset. arXiv:cs.SI/2003.10359,2020 <https://arxiv.org/abs/2003.10359>

## Data Organization

The tweet-IDs are organized by keywords as follows:

  - Tweet-ID files are stored in folders that indicate the keyword used
    (i.e., coronavirus, virus, covid, ncov19, ncov2019).

  - The Tweet-ID file is a `.txt` containing individual Tweet-IDs stored
    as a comma-separated-list. The file names follow the naming
    convention of : `[Keyword]_yyyy_mm_dd.txt` (e.g.,
    `coronavirus_2020_01_22.txt` contains the ids of tweets mentioning
    the keyword ‘coronavirus’ tweeted on January 22th, 2020).
    
  - The Tweets_ID_by_language folder contains a series of `.txt` files with the tweets ID and their language organized by keyword (see [Twitter language codes)](https://developer.twitter.com/en/docs/twitter-for-websites/twitter-for-websites-supported-languages/overview).  The file names follow the naming convention of : `[mm_dd_yyyy]_[Keyword].txt` (e.g., `coronavirus`>`Apr_03_2020_coronavirus`, contains tweets id and their language from all the tweets collected on April 3rd, 2020 using the keyword coronavirus).
  
  - Since the Twitter API returns tweets in UTC, all tweet-ID folder and
    file names are all in UTC as well.
    
    

## Data Collection Process

  - Not all keywords were tracked from the very beginning. As news about
    the novel coronavirus spread, additional keywords were added to the
    search list. The keywords used for search tweets are: virus and
    coronavirus since 22 January, ncov19 and ncov2019 since 26 February,
    and covid since 7 March 2020.
  - Since the Twitter API can provide tweets up to 7-days in the pass,
    there is a lag of 7-days in the dataset to ensure as much tweets as
    possible are sampled.
  - Our dataset **does not** capture every single tweet on Twitter
    relating to the keywords as our data retrieval is restricted by the
    Twitter API at 45,000 tweets every 15 minutes.
  - We currently have some descriptive statistics about our dataset
    displayed in the paper associated with it. We are working on
    automatically updating these statistics with every update of the
    dataset.
  - Consider using tools such as the
    [Hydrator](https://github.com/DocNow/hydrator) and
    [Twarc](https://github.com/DocNow/twarc) to rehydrate the tweet-IDs
    i.e. to fetch tweet data associated with the tweet-IDs using
    Twitter’s API.
  - Tweets deleted after our initial collection may still be present in
    our dataset, but their details can no longer be retrieved by using
    Twitter’s API.
  - [Chen et al., 2020](#chen) has published a dataset, similar to ours,
    containing tweet-IDs relating to the novel coronavirus. For those
    looking for an even larger dataset than ours, merging the two
    datasets is a valid option.

### Data Collection Process Inconsistencies

  - Only tweets in English were collected from 22 January to 31 January
    2020, after this time the algorithm collected tweets in all
    languages.
  - You can notice that there are fewer tweets relating to the novel
    coronavirus present in our dataset in the first few weeks than in
    the following weeks. This can explained by the fact that our data
    collection involved tracking other keywords unrelated to the
    coronavirus during the first few weeks (other projects). This meant
    that the number of coronavirus-related tweets were limited at a
    fraction of the total API limit. Once unrelated keywords were
    removed from our search options, the limit of coronavirus-related
    tweets became the total API limit, hence resulting in more tweets in
    our dataset.
  - Our dataset is currently missing tweed-ID entries for Feb 06 and 07,
    2020. This data was lost due to technical errors. However, tweet
    data was retained and hence our statistics were not affected by this
    loss of tweet-IDs. We currently are working on retrieving the lost
    tweet-ID data.
  - Our dataset is currently missing tweed-ID entries for March 24th
    keywords: virus, coronavirus, covid, nvoc2019 (i.e., only ncov19 are
    present in the data set). This data was lost due to technical
    errors.

## Hydrating Tweets

### Using our TWARC Notebook

The notebook
[Automatically\_Hydrate\_TweetsIDs\_COVID190.ipynb](https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/master/Automatically_Hydrate_TweetsIDs_COVID190.ipynb)
will allow you to automatically hydrate the tweets-ID from our
[COVID19\_Tweets\_dataset GitHub
repository](https://github.com/lopezbec/COVID19_Tweets_Dataset).

You can run this notebook directly on the cloud using Google Colab [(see
how to
tutorials)](https://colab.research.google.com/notebooks/welcome.ipynb#scrollTo=xitplqMNk_Hc)
and Google Drive.

In order to hydrate the tweet-IDs using
[TWARC](https://github.com/DocNow/twarc) you need to create a [Twitter
Developer Account](https://developer.twitter.com/en/apply-for-access).

The Twitter API’s rate limits pose an issue to fetch data from
tweed-IDs. So, we recommended using Hydrator to convert the list of
tweed-IDs, into a CSV file containing all data and meta-data relating to
the tweets. Hydrator also manages Twitter API Rate Limits for you.

For those who prefer a command-line interface over a GUI, we recommend
using Twarc.

### Using [Hydrator](https://github.com/DocNow/hydrator)

Follow the instructions on the [Hydrator github
repository](https://github.com/DocNow/hydrator).

### Using [Twarc](https://github.com/DocNow/twarc) (CLI)

Follow the instructions on the [Twarc github
repository](https://github.com/DocNow/twarc).

1.  First follow instructions for
    [installation](https://github.com/DocNow/twarc#Install).

2.  Then, obtain your Twitter API token
    ([apply](https://developer.twitter.com/en/apply-for-access) for a
    Twitter developer account).

3.  Configure twarc with your API token by following the instructions
    for [configuration](https://github.com/DocNow/twarc#Quickstart).

4.  Follow instructions in the [Hydrate
    section](https://github.com/DocNow/twarc#hydrate). Hydrated tweets
    are stored in [jsonl](http://jsonlines.org/) files.

## Data Statistics

The following data is from Tweets colectled until **August  14th, 2020**.
(v1.5)

Number of Tweets: **508,032,902**

Tweets Breakdown by Month:

| Month | Number.of.Tweets |
| :---- | ---------------: |
| Jan   |          724,877 |
| Feb   |        2,994,768 |
| Mar   |       27,414,279 |
| Apr   |       61,080,885 |
| May   |      100,100,066 |
| Jun   |      133,949,338 |
| Jul   |      148,798,867 |
| Aug   |       32,969,822 |

*The increase of the number of tweet per month is not only related to the fact that as the pandemic evolved  more people were tweeting about it, but also our ability to collect more tweets and to augment our dataset with other available datasets, like Chen et al (2020).*



<div class="figure">

<img src="https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/master/analysis/until_2020__05_04/coronavirus/Tweets%20by%20Language.png" alt="Number of tweets a day by language for the keyword 'coronavirus'." width="100%" />

<p class="caption">

Number of tweets a day by language for the keyword
‘coronavirus’.

</p>

</div>

<div class="figure">

<img src="https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/master/analysis/until_2020__05_04/coronavirus/GeoTweets.png" alt="Geolocated tweets for the keyword 'coronavirus'" width="100%" />

<p class="caption">

Geolocated tweets for the keyword
‘coronavirus’

</p>

</div>

<div class="figure">

<img src="https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/master/analysis/until_2020__05_04/coronavirus/Sentiment.png" alt="Average sentiment of tweets for the observation period grouped by keyword." width="100%" />

<p class="caption">

Sentiment of tweets.

</p>

</div>

## Inquiries

For questions about the dataset, please contact Dr. Christian Lopez at
**<lopezbec@lafayette.edu>**, Dr. Caleb Gallemore at
**<gallemoc@lafayette.edu>**, or Malolan Vasu at
**<vasum@lafayette.edu>**.

## Licensing

This dataset is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International Public License
([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)).
By using this dataset, you agree to abide by the stipulations in the
license, remain in compliance with Twitter’s [Terms of
Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy),
and cite the following manuscript:

## References

<a name="chen"></a> Emily Chen, Kristina Lerman, and Emilio Ferrara.
2020. \#COVID-19: The First Public Coronavirus Twitter Dataset.
arXiv:cs.SI/2003.07372, 2020

https://github.com/echen102/COVID-19-TweetIDs
