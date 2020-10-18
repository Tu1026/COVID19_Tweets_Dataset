-   [Data Organization](#data-organization)
-   [Data Statistics](#data-statistics)
    -   [General Statistics](#general-statistics)
    -   [Language Statistics](#language-statistics)
    -   [Sentiment Analaysis](#sentiment-analaysis)
    -   [Named Entity Recognition, Mentions, and
        Hashtags](#named-entity-recognition-mentions-and-hashtags)
    -   [Data Collection Process
        Inconsistencies](#data-collection-process-inconsistencies)
-   [Inquiries](#inquiries)
-   [Licensing](#licensing)
-   [References](#references)

The repository contains an ongoing collection of tweets associated with
the novel coronavirus COVID-19 since January 22nd, 2020.

As of 08/31/2020 there were a total of **696,455,472** tweets collected.
The tweets are collected using Twitter’s trending topics and selected
keywords. Moreover, the tweets from [Chen et
al. (2020)](https://github.com/echen102/COVID-19-TweetIDs) was used to
supplement the dataset by hydrating non-duplicated tweets.

**Citation**

Christian Lopez, Malolan Vasu, and Caleb Gallemore (2020) Understanding
the perception of COVID-19 policies by mining a multilanguage Twitter
dataset. arXiv:cs.SI/2003.10359,2020
<a href="https://arxiv.org/abs/2003.10359" class="uri">https://arxiv.org/abs/2003.10359</a>

Data Organization
-----------------

The dataset is organized by hour (UTC) , month, and by tables. The
description of all the features in all five tables is provided below.
For example, the path
“./Summary\_Details/2020\_01/2020\_01\_22\_00\_Summary\_Details.csv”
contains all the summary details of the tweets collection on January
22nd at 00:00 UTC time.

<table class="table table" style="margin-left: auto; margin-right: auto; font-size: 9px; margin-left: auto; margin-right: auto;">
<caption style="font-size: initial !important;">
Features Description
</caption>
<thead>
<tr>
<th style="text-align:left;font-weight: bold;">
Table
</th>
<th style="text-align:left;font-weight: bold;">
Feature.Name
</th>
<th style="text-align:left;font-weight: bold;">
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
Primary key
</td>
<td style="text-align:left;">
Tweet\_ID
</td>
<td style="text-align:left;">
Integer representation of the tweet’s unique identifier
</td>
</tr>
<tr>
<td style="text-align:left;">
2.Summary\_Details
</td>
<td style="text-align:left;">
Language
</td>
<td style="text-align:left;">
When present, indicates a BCP47 language identifier corresponding to the
machine-detected language of the Tweet text
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Geolocation\_cordinate
</td>
<td style="text-align:left;">
Indicates whether or not the geographic location of the tweet was
reported
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
RT
</td>
<td style="text-align:left;">
Indicates if the tweet is a retweet (YES) or original tweet (NO)
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Likes
</td>
<td style="text-align:left;">
Number of likes for the tweet
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Retweets
</td>
<td style="text-align:left;">
Number of times the tweet was retweeted
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Country
</td>
<td style="text-align:left;">
When present, indicates a list of uppercase two-letter country
codes from which the tweet comes
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Date\_Created
</td>
<td style="text-align:left;">
UTC date and time the tweet was created
</td>
</tr>
<tr>
<td style="text-align:left;">
2.Summary\_Hastag
</td>
<td style="text-align:left;">
Hashtag
</td>
<td style="text-align:left;">
Hashtag (\#) present in the tweet
</td>
</tr>
<tr>
<td style="text-align:left;">
3.Summary\_Mentions
</td>
<td style="text-align:left;">
Mention
</td>
<td style="text-align:left;">
Mention (@) present in the tweet
</td>
</tr>
<tr>
<td style="text-align:left;">
4.Summary\_Sentiment
</td>
<td style="text-align:left;">
Sentiment\_Label
</td>
<td style="text-align:left;">
Most probable tweet sentiment (neutral, positive, negative)
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Logits\_Neutral
</td>
<td style="text-align:left;">
Non-normalized prediction for neutral sentiment
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Logits\_Positive
</td>
<td style="text-align:left;">
Non-normalized prediction for positive sentiment
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Logits\_Negative
</td>
<td style="text-align:left;">
Non-normalized prediction for negative sentiment
</td>
</tr>
<tr>
<td style="text-align:left;">
5.Summary\_NER
</td>
<td style="text-align:left;">
NER\_text
</td>
<td style="text-align:left;">
Text stating a named entity recognized by the NER algorithm
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Start\_Pos
</td>
<td style="text-align:left;">
Initial character position within the tweet of the NER\_text
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
End\_Pos
</td>
<td style="text-align:left;">
End character position within the tweet of the NER\_text
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
NER\_Label Prob
</td>
<td style="text-align:left;">
Label and probability of the named entity recognized by the NER
algorithm
</td>
</tr>
</tbody>
</table>

Data Statistics
---------------

### General Statistics

Total Number of tweets: **696,455,472**

Average daily number of tweets: **123,186**

<table class="table table" style="margin-left: auto; margin-right: auto; font-size: 12px; margin-left: auto; margin-right: auto;">
<caption style="font-size: initial !important;">
Summary Statistics per Month
</caption>
<thead>
<tr>
<th style="text-align:left;font-weight: bold;">
Month
</th>
<th style="text-align:left;font-weight: bold;">
Daily Avg. Original
</th>
<th style="text-align:left;font-weight: bold;">
Daily Avg. Retweets
</th>
<th style="text-align:left;font-weight: bold;">
Daily Avg. Tweets
</th>
<th style="text-align:left;font-weight: bold;">
Total of Orignal
</th>
<th style="text-align:left;font-weight: bold;">
Total of Retweets
</th>
<th style="text-align:left;font-weight: bold;">
Total of Tweets
</th>
<th style="text-align:left;font-weight: bold;">
Total with Geolocation
</th>
<th style="text-align:left;font-weight: bold;">
Max No. Retweets
</th>
<th style="text-align:left;font-weight: bold;">
Max No. Likes
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
1
</td>
<td style="text-align:left;">
5,947
</td>
<td style="text-align:left;">
30,576
</td>
<td style="text-align:left;">
35,501
</td>
<td style="text-align:left;">
1,958,346
</td>
<td style="text-align:left;">
7,852,504
</td>
<td style="text-align:left;">
9,810,850
</td>
<td style="text-align:left;">
1,773
</td>
<td style="text-align:left;">
674,151
</td>
<td style="text-align:left;">
334,802
</td>
</tr>
<tr>
<td style="text-align:left;">
2
</td>
<td style="text-align:left;">
10,978
</td>
<td style="text-align:left;">
29,918
</td>
<td style="text-align:left;">
40,604
</td>
<td style="text-align:left;">
7,624,648
</td>
<td style="text-align:left;">
21,944,443
</td>
<td style="text-align:left;">
29,568,948
</td>
<td style="text-align:left;">
8,103
</td>
<td style="text-align:left;">
469,739
</td>
<td style="text-align:left;">
637,589
</td>
</tr>
<tr>
<td style="text-align:left;">
3
</td>
<td style="text-align:left;">
13,095
</td>
<td style="text-align:left;">
44,714
</td>
<td style="text-align:left;">
56,283
</td>
<td style="text-align:left;">
12,610,824
</td>
<td style="text-align:left;">
46,659,589
</td>
<td style="text-align:left;">
59,270,412
</td>
<td style="text-align:left;">
19,952
</td>
<td style="text-align:left;">
1,064,693
</td>
<td style="text-align:left;">
1,255,858
</td>
</tr>
<tr>
<td style="text-align:left;">
4
</td>
<td style="text-align:left;">
30,091
</td>
<td style="text-align:left;">
89,513
</td>
<td style="text-align:left;">
119,859
</td>
<td style="text-align:left;">
20,591,357
</td>
<td style="text-align:left;">
60,301,889
</td>
<td style="text-align:left;">
80,893,244
</td>
<td style="text-align:left;">
38,213
</td>
<td style="text-align:left;">
649,823
</td>
<td style="text-align:left;">
662,005
</td>
</tr>
<tr>
<td style="text-align:left;">
5
</td>
<td style="text-align:left;">
35,163
</td>
<td style="text-align:left;">
99,928
</td>
<td style="text-align:left;">
135,709
</td>
<td style="text-align:left;">
26,258,213
</td>
<td style="text-align:left;">
73,618,083
</td>
<td style="text-align:left;">
99,876,289
</td>
<td style="text-align:left;">
47,684
</td>
<td style="text-align:left;">
1,007,616
</td>
<td style="text-align:left;">
929,811
</td>
</tr>
<tr>
<td style="text-align:left;">
6
</td>
<td style="text-align:left;">
51,033
</td>
<td style="text-align:left;">
142,569
</td>
<td style="text-align:left;">
193,096
</td>
<td style="text-align:left;">
34,786,076
</td>
<td style="text-align:left;">
95,171,388
</td>
<td style="text-align:left;">
129,957,461
</td>
<td style="text-align:left;">
58,138
</td>
<td style="text-align:left;">
790,652
</td>
<td style="text-align:left;">
882,693
</td>
</tr>
<tr>
<td style="text-align:left;">
7
</td>
<td style="text-align:left;">
53,594
</td>
<td style="text-align:left;">
154,921
</td>
<td style="text-align:left;">
209,298
</td>
<td style="text-align:left;">
38,272,412
</td>
<td style="text-align:left;">
108,111,086
</td>
<td style="text-align:left;">
146,383,498
</td>
<td style="text-align:left;">
55,184
</td>
<td style="text-align:left;">
615,768
</td>
<td style="text-align:left;">
1,287,117
</td>
</tr>
<tr>
<td style="text-align:left;">
8
</td>
<td style="text-align:left;">
51,330
</td>
<td style="text-align:left;">
143,551
</td>
<td style="text-align:left;">
195,142
</td>
<td style="text-align:left;">
37,596,182
</td>
<td style="text-align:left;">
103,098,588
</td>
<td style="text-align:left;">
140,694,770
</td>
<td style="text-align:left;">
55,837
</td>
<td style="text-align:left;">
2,183,434
</td>
<td style="text-align:left;">
860,162
</td>
</tr>
</tbody>
</table>

![](https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/master/Summary_Details/Tweets%20per%20Day.png)

There is a total of 284,884 tweets with geolocation information, which
are shown on a map below:

![](https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/master/Summary_Details/GeoTweets.png)

### Language Statistics

<table class="table table" style="margin-left: auto; margin-right: auto; font-size: 12px; margin-left: auto; margin-right: auto;">
<caption style="font-size: initial !important;">
Tweets Language Summary
</caption>
<thead>
<tr>
<th style="text-align:left;font-weight: bold;">
Languages
</th>
<th style="text-align:left;font-weight: bold;">
Total No. Tweets
</th>
<th style="text-align:right;font-weight: bold;">
Percentage of Tweets
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
English
</td>
<td style="text-align:left;">
470,166,516
</td>
<td style="text-align:right;">
67.51
</td>
</tr>
<tr>
<td style="text-align:left;">
Spanish; Castilian
</td>
<td style="text-align:left;">
94,542,748
</td>
<td style="text-align:right;">
13.57
</td>
</tr>
<tr>
<td style="text-align:left;">
Portuguese
</td>
<td style="text-align:left;">
28,976,586
</td>
<td style="text-align:right;">
4.16
</td>
</tr>
<tr>
<td style="text-align:left;">
Bahasa
</td>
<td style="text-align:left;">
19,529,913
</td>
<td style="text-align:right;">
2.80
</td>
</tr>
<tr>
<td style="text-align:left;">
French
</td>
<td style="text-align:left;">
14,988,572
</td>
<td style="text-align:right;">
2.15
</td>
</tr>
<tr>
<td style="text-align:left;">
Other
</td>
<td style="text-align:left;">
13,581,185
</td>
<td style="text-align:right;">
1.95
</td>
</tr>
<tr>
<td style="text-align:left;">
Japanese
</td>
<td style="text-align:left;">
8,523,690
</td>
<td style="text-align:right;">
1.22
</td>
</tr>
<tr>
<td style="text-align:left;">
Italian
</td>
<td style="text-align:left;">
6,615,195
</td>
<td style="text-align:right;">
0.95
</td>
</tr>
<tr>
<td style="text-align:left;">
Hindi
</td>
<td style="text-align:left;">
6,019,481
</td>
<td style="text-align:right;">
0.86
</td>
</tr>
<tr>
<td style="text-align:left;">
Thai
</td>
<td style="text-align:left;">
5,409,177
</td>
<td style="text-align:right;">
0.78
</td>
</tr>
<tr>
<td style="text-align:left;">
NA
</td>
<td style="text-align:left;">
28,102,253
</td>
<td style="text-align:right;">
4.04
</td>
</tr>
</tbody>
</table>

![](https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/master/Summary_Details/Tweets%20by%20Language%20Line%20plot.png)

### Sentiment Analaysis

The sentiment of all the English tweets was estimated using a
state-or-the-art Twitter Sentiment algorithm
[BB\_twtr](https://arxiv.org/abs/1704.06125). [(See code
here)](https://github.com/leelaylay/TweetSemEval) .

![](https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/master/Summary_Sentiment/Tweets%20Sentiment.png)

### Named Entity Recognition, Mentions, and Hashtags

The Named Entity Recognition algorithm of
[flairNLP](https://github.com/flairNLP/flair) was used to extract topics
of conversation about PERSON, LOCATION, ORGANIZATION, and others. Below
are the top 5 NER, Mentions (@) and Hastags (\#)

<table class="table table" style="margin-left: auto; margin-right: auto; font-size: 12px; margin-left: auto; margin-right: auto;">
<caption style="font-size: initial !important;">
Top 5 Mentions, Hashtags, and NER
</caption>
<thead>
<tr>
<th style="text-align:left;font-weight: bold;">
Mentions
</th>
<th style="text-align:left;font-weight: bold;">
Hashtags
</th>
<th style="text-align:left;font-weight: bold;">
NER Person
</th>
<th style="text-align:left;font-weight: bold;">
NER Location
</th>
<th style="text-align:left;font-weight: bold;">
NER Organization
</th>
<th style="text-align:left;font-weight: bold;">
NER Miscellaneous
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
@spectatorindex
</td>
<td style="text-align:left;">
\#covid19
</td>
<td style="text-align:left;">
trump
</td>
<td style="text-align:left;">
china
</td>
<td style="text-align:left;">
cdc
</td>
<td style="text-align:left;">
coronavirus
</td>
</tr>
<tr>
<td style="text-align:left;">
123,397
</td>
<td style="text-align:left;">
46,275,884
</td>
<td style="text-align:left;">
3,407,285
</td>
<td style="text-align:left;">
9,993,850
</td>
<td style="text-align:left;">
1,134,620
</td>
<td style="text-align:left;">
4,808,336
</td>
</tr>
<tr>
<td style="text-align:left;">
@WHO
</td>
<td style="text-align:left;">
\#coronavirus
</td>
<td style="text-align:left;">
god
</td>
<td style="text-align:left;">
us
</td>
<td style="text-align:left;">
trump
</td>
<td style="text-align:left;">
chinese
</td>
</tr>
<tr>
<td style="text-align:left;">
105,117
</td>
<td style="text-align:left;">
30,367,629
</td>
<td style="text-align:left;">
425,488
</td>
<td style="text-align:left;">
3,432,212
</td>
<td style="text-align:left;">
440,331
</td>
<td style="text-align:left;">
2,600,473
</td>
</tr>
<tr>
<td style="text-align:left;">
@siwuol
</td>
<td style="text-align:left;">
\#covid
</td>
<td style="text-align:left;">
donald trump
</td>
<td style="text-align:left;">
wuhan
</td>
<td style="text-align:left;">
nhs
</td>
<td style="text-align:left;">
covid-19
</td>
</tr>
<tr>
<td style="text-align:left;">
67,330
</td>
<td style="text-align:left;">
4,088,915
</td>
<td style="text-align:left;">
212,188
</td>
<td style="text-align:left;">
2,347,592
</td>
<td style="text-align:left;">
203,277
</td>
<td style="text-align:left;">
2,206,367
</td>
</tr>
<tr>
<td style="text-align:left;">
@realDonaldTrump
</td>
<td style="text-align:left;">
\#covid\<u+30fc\>19
</td>
<td style="text-align:left;">
fauci
</td>
<td style="text-align:left;">
italy
</td>
<td style="text-align:left;">
world health organization
</td>
<td style="text-align:left;">
americans
</td>
</tr>
<tr>
<td style="text-align:left;">
66,658
</td>
<td style="text-align:left;">
2,298,542
</td>
<td style="text-align:left;">
162,605
</td>
<td style="text-align:left;">
783,383
</td>
<td style="text-align:left;">
156,534
</td>
<td style="text-align:left;">
1,055,204
</td>
</tr>
<tr>
<td style="text-align:left;">
@eyekon131
</td>
<td style="text-align:left;">
\#stayhome
</td>
<td style="text-align:left;">
mike pence
</td>
<td style="text-align:left;">
india
</td>
<td style="text-align:left;">
congress
</td>
<td style="text-align:left;">
american
</td>
</tr>
<tr>
<td style="text-align:left;">
63,249
</td>
<td style="text-align:left;">
1,355,073
</td>
<td style="text-align:left;">
136,105
</td>
<td style="text-align:left;">
661,124
</td>
<td style="text-align:left;">
129,619
</td>
<td style="text-align:left;">
358,421
</td>
</tr>
</tbody>
</table>

### Data Collection Process Inconsistencies

-   Only tweets in English were collected from 22 January to 31 January
    2020, after this time the algorithm collected tweets in all
    languages.

There are also some known gaps of data shown below:

<table class="table table" style="margin-left: auto; margin-right: auto; font-size: 12px; margin-left: auto; margin-right: auto;">
<caption style="font-size: initial !important;">
Known gaps
</caption>
<thead>
<tr>
<th style="text-align:left;font-weight: bold;">
Date
</th>
<th style="text-align:left;font-weight: bold;">
Hour
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
8/6/2020
</td>
<td style="text-align:left;">
7:00 UTC
</td>
</tr>
<tr>
<td style="text-align:left;">
8/8/2020
</td>
<td style="text-align:left;">
7:00 UTC
</td>
</tr>
<tr>
<td style="text-align:left;">
8/9/2020
</td>
<td style="text-align:left;">
7:00 UTC
</td>
</tr>
<tr>
<td style="text-align:left;">
8/14/2020
</td>
<td style="text-align:left;">
7:00 UTC
</td>
</tr>
</tbody>
</table>

Inquiries
---------

For questions about the dataset, please contact Dr. Christian Lopez at
**<a href="mailto:lopezbec@lafayette.edu" class="email">lopezbec@lafayette.edu</a>**,
Dr. Caleb Gallemore at
**<a href="mailto:gallemoc@lafayette.edu" class="email">gallemoc@lafayette.edu</a>**,
or Malolan Vasu at
**<a href="mailto:vasum@lafayette.edu" class="email">vasum@lafayette.edu</a>**.

Licensing
---------

This dataset is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International Public License
([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)).
By using this dataset, you agree to abide by the stipulations in the
license, remain in compliance with Twitter’s [Terms of
Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy),
and cite the following manuscript:

References
----------

<a name="chen"></a> Emily Chen, Kristina Lerman, and Emilio Ferrara.
2020. \#COVID-19: The First Public Coronavirus Twitter Dataset.
arXiv:cs.SI/2003.07372, 2020

<a href="https://github.com/echen102/COVID-19-TweetIDs" class="uri">https://github.com/echen102/COVID-19-TweetIDs</a>
