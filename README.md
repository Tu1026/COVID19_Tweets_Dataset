COVID-19 Multilanguage Tweets Dataset
================

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
dataset. arXiv:cs.SI/2003.10359,2020 <https://arxiv.org/abs/2003.10359>

## Data Organization

The dataset is organized by hour (UTC) , month, and by tables: (1)
“Summary\_Details”, (2) “Summary\_Hastag”, (3) “Summary\_Mentions”,
(4) “Summary\_Sentiment”, and (5) “Summary\_NER”. For example, the path
“./Summary\_Details/2020\_01/2020\_01\_22\_00\_Summary\_Details.csv”
contains all the summary details of the tweets collection on January
22nd at 00:00 UTC time. The description of all the features in all five
tables is provided in Table 1 below:

<table class="table table" style="margin-left: auto; margin-right: auto; font-size: 10px; margin-left: auto; margin-right: auto;">

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

Integer representation of the tweet’s unique identifier\*

</td>

</tr>

<tr>

<td style="text-align:left;">

Summary\_Details

</td>

<td style="text-align:left;">

Language

</td>

<td style="text-align:left;">

When present, indicates a BCP47 language identifier corresponding to the
machine-detected language of the Tweet text \*

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
reported\*

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
codes from which the tweet comes\*

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

Summary\_Hastag

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

Summary\_Mentions

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

Summary\_Sentiment

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

Summary\_NER

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

## Data Statistics

### General Statistics

Total Number of tweets: **696,455,472**

Average daily number of tweets: **123,186**

Table 2 shows the daily average and the total number of original and
retweets collected per month:

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

<!--html_preserve-->

<div id="htmlwidget-8be3c3383acba54da9fb" class="plotly html-widget" style="width:672px;height:480px;">

</div>

<script type="application/json" data-for="htmlwidget-8be3c3383acba54da9fb">{"x":{"data":[{"x":[18283,18284,18285,18286,18287,18288,18289,18290,18291,18292,18293,18294,18295,18296,18297,18298,18299,18300,18301,18302,18303,18304,18305,18306,18307,18308,18309,18310,18311,18312,18313,18314,18315,18316,18317,18318,18319,18320,18321,18322,18323,18324,18325,18326,18327,18328,18329,18330,18331,18332,18333,18334,18335,18336,18337,18338,18339,18340,18341,18342,18343,18344,18345,18346,18347,18348,18349,18350,18351,18352,18353,18354,18355,18356,18357,18358,18359,18360,18361,18362,18363,18364,18365,18366,18367,18368,18369,18370,18371,18372,18373,18374,18375,18376,18377,18378,18379,18380,18381,18382,18383,18384,18385,18386,18387,18388,18389,18390,18391,18392,18393,18394,18395,18396,18397,18398,18399,18400,18401,18402,18403,18404,18405,18406,18407,18408,18409,18410,18411,18412,18413,18414,18415,18416,18417,18418,18419,18420,18421,18422,18423,18424,18425,18426,18427,18428,18429,18430,18431,18432,18433,18434,18435,18436,18437,18438,18439,18440,18441,18442,18443,18444,18445,18446,18447,18448,18449,18451,18452,18453,18454,18455,18456,18457,18458,18459,18460,18461,18462,18463,18464,18465,18466,18467,18468,18469,18470,18471,18472,18473,18474,18475,18476,18477,18478,18479,18480,18481,18482,18483,18484,18485,18486,18487,18488,18489,18490,18491,18492,18493,18494,18495,18496,18497,18498,18499,18500,18501,18502,18503,18504,18505],"y":[36333,203690,568485,856089,1137733,871085,765992,1647765,1930672,1793006,827939,920137,919892,1007050,930821,921608,865530,858404,855649,936314,978002,884123,978155,905226,800878,816206,866439,941773,856378,897232,998010,899919,158058,898785,970572,1139063,1143009,1927526,3466107,2573941,977484,2879793,3081743,1126188,1173275,1194054,1196941,1191461,1210799,1244151,1184557,1175432,1198572,1187715,1163521,2560356,1618260,2914695,2962629,2866351,3008950,2913754,904867,1197378,3004512,2599647,2949281,2983856,2062352,963896,1913570,2753085,2697387,2885900,2911934,2908969,2970189,2079489,1844015,2898349,2874495,2879760,2898901,2899728,2936409,2914281,2791027,2269435,2886277,2871900,860087,2812206,2817592,2823757,3309484,3296327,3348013,2511718,2075822,2953136,2797636,2915583,2978466,3076312,1746499,3171255,3633711,3401023,3288483,3217612,3700694,3534107,3733185,3646903,3613371,3415582,3424102,3629541,3547301,3520098,3403888,3203318,3096605,3028523,3035953,3053694,2966819,3025092,3114110,3028092,2928724,3111723,2911739,2881214,2915917,2420088,4464440,4541388,4511154,4500095,4664105,4683289,4651985,4491924,4345782,4719121,4602070,4645645,4522965,4579185,4408125,4312872,4626294,4778853,4760720,4927751,4900490,4633288,4611867,4758478,5074891,5066747,4757030,4818268,4653034,4666372,4966247,4966733,4724475,4602458,4367496,4119296,5549327,4998739,5314638,5122505,5137243,4916051,5091562,4895498,5071583,5030064,4861094,4648985,4543164,4493827,4803863,5200574,5153883,5020051,4822691,4508204,4707409,4482064,4858355,4300412,4472590,4655061,4136621,4633092,4935200,4862710,4356173,4617337,4466298,4235274,4200107,4366290,4389130,4393857,4455164,4622409,4487676,4737102,4744988,4808933,4781885,4802854,4763210,4083157,4320991,4510217],"text":["Date: 2020-01-22<br />total:   36333","Date: 2020-01-23<br />total:  203690","Date: 2020-01-24<br />total:  568485","Date: 2020-01-25<br />total:  856089","Date: 2020-01-26<br />total: 1137733","Date: 2020-01-27<br />total:  871085","Date: 2020-01-28<br />total:  765992","Date: 2020-01-29<br />total: 1647765","Date: 2020-01-30<br />total: 1930672","Date: 2020-01-31<br />total: 1793006","Date: 2020-02-01<br />total:  827939","Date: 2020-02-02<br />total:  920137","Date: 2020-02-03<br />total:  919892","Date: 2020-02-04<br />total: 1007050","Date: 2020-02-05<br />total:  930821","Date: 2020-02-06<br />total:  921608","Date: 2020-02-07<br />total:  865530","Date: 2020-02-08<br />total:  858404","Date: 2020-02-09<br />total:  855649","Date: 2020-02-10<br />total:  936314","Date: 2020-02-11<br />total:  978002","Date: 2020-02-12<br />total:  884123","Date: 2020-02-13<br />total:  978155","Date: 2020-02-14<br />total:  905226","Date: 2020-02-15<br />total:  800878","Date: 2020-02-16<br />total:  816206","Date: 2020-02-17<br />total:  866439","Date: 2020-02-18<br />total:  941773","Date: 2020-02-19<br />total:  856378","Date: 2020-02-20<br />total:  897232","Date: 2020-02-21<br />total:  998010","Date: 2020-02-22<br />total:  899919","Date: 2020-02-23<br />total:  158058","Date: 2020-02-24<br />total:  898785","Date: 2020-02-25<br />total:  970572","Date: 2020-02-26<br />total: 1139063","Date: 2020-02-27<br />total: 1143009","Date: 2020-02-28<br />total: 1927526","Date: 2020-02-29<br />total: 3466107","Date: 2020-03-01<br />total: 2573941","Date: 2020-03-02<br />total:  977484","Date: 2020-03-03<br />total: 2879793","Date: 2020-03-04<br />total: 3081743","Date: 2020-03-05<br />total: 1126188","Date: 2020-03-06<br />total: 1173275","Date: 2020-03-07<br />total: 1194054","Date: 2020-03-08<br />total: 1196941","Date: 2020-03-09<br />total: 1191461","Date: 2020-03-10<br />total: 1210799","Date: 2020-03-11<br />total: 1244151","Date: 2020-03-12<br />total: 1184557","Date: 2020-03-13<br />total: 1175432","Date: 2020-03-14<br />total: 1198572","Date: 2020-03-15<br />total: 1187715","Date: 2020-03-16<br />total: 1163521","Date: 2020-03-17<br />total: 2560356","Date: 2020-03-18<br />total: 1618260","Date: 2020-03-19<br />total: 2914695","Date: 2020-03-20<br />total: 2962629","Date: 2020-03-21<br />total: 2866351","Date: 2020-03-22<br />total: 3008950","Date: 2020-03-23<br />total: 2913754","Date: 2020-03-24<br />total:  904867","Date: 2020-03-25<br />total: 1197378","Date: 2020-03-26<br />total: 3004512","Date: 2020-03-27<br />total: 2599647","Date: 2020-03-28<br />total: 2949281","Date: 2020-03-29<br />total: 2983856","Date: 2020-03-30<br />total: 2062352","Date: 2020-03-31<br />total:  963896","Date: 2020-04-01<br />total: 1913570","Date: 2020-04-02<br />total: 2753085","Date: 2020-04-03<br />total: 2697387","Date: 2020-04-04<br />total: 2885900","Date: 2020-04-05<br />total: 2911934","Date: 2020-04-06<br />total: 2908969","Date: 2020-04-07<br />total: 2970189","Date: 2020-04-08<br />total: 2079489","Date: 2020-04-09<br />total: 1844015","Date: 2020-04-10<br />total: 2898349","Date: 2020-04-11<br />total: 2874495","Date: 2020-04-12<br />total: 2879760","Date: 2020-04-13<br />total: 2898901","Date: 2020-04-14<br />total: 2899728","Date: 2020-04-15<br />total: 2936409","Date: 2020-04-16<br />total: 2914281","Date: 2020-04-17<br />total: 2791027","Date: 2020-04-18<br />total: 2269435","Date: 2020-04-19<br />total: 2886277","Date: 2020-04-20<br />total: 2871900","Date: 2020-04-21<br />total:  860087","Date: 2020-04-22<br />total: 2812206","Date: 2020-04-23<br />total: 2817592","Date: 2020-04-24<br />total: 2823757","Date: 2020-04-25<br />total: 3309484","Date: 2020-04-26<br />total: 3296327","Date: 2020-04-27<br />total: 3348013","Date: 2020-04-28<br />total: 2511718","Date: 2020-04-29<br />total: 2075822","Date: 2020-04-30<br />total: 2953136","Date: 2020-05-01<br />total: 2797636","Date: 2020-05-02<br />total: 2915583","Date: 2020-05-03<br />total: 2978466","Date: 2020-05-04<br />total: 3076312","Date: 2020-05-05<br />total: 1746499","Date: 2020-05-06<br />total: 3171255","Date: 2020-05-07<br />total: 3633711","Date: 2020-05-08<br />total: 3401023","Date: 2020-05-09<br />total: 3288483","Date: 2020-05-10<br />total: 3217612","Date: 2020-05-11<br />total: 3700694","Date: 2020-05-12<br />total: 3534107","Date: 2020-05-13<br />total: 3733185","Date: 2020-05-14<br />total: 3646903","Date: 2020-05-15<br />total: 3613371","Date: 2020-05-16<br />total: 3415582","Date: 2020-05-17<br />total: 3424102","Date: 2020-05-18<br />total: 3629541","Date: 2020-05-19<br />total: 3547301","Date: 2020-05-20<br />total: 3520098","Date: 2020-05-21<br />total: 3403888","Date: 2020-05-22<br />total: 3203318","Date: 2020-05-23<br />total: 3096605","Date: 2020-05-24<br />total: 3028523","Date: 2020-05-25<br />total: 3035953","Date: 2020-05-26<br />total: 3053694","Date: 2020-05-27<br />total: 2966819","Date: 2020-05-28<br />total: 3025092","Date: 2020-05-29<br />total: 3114110","Date: 2020-05-30<br />total: 3028092","Date: 2020-05-31<br />total: 2928724","Date: 2020-06-01<br />total: 3111723","Date: 2020-06-02<br />total: 2911739","Date: 2020-06-03<br />total: 2881214","Date: 2020-06-04<br />total: 2915917","Date: 2020-06-05<br />total: 2420088","Date: 2020-06-06<br />total: 4464440","Date: 2020-06-07<br />total: 4541388","Date: 2020-06-08<br />total: 4511154","Date: 2020-06-09<br />total: 4500095","Date: 2020-06-10<br />total: 4664105","Date: 2020-06-11<br />total: 4683289","Date: 2020-06-12<br />total: 4651985","Date: 2020-06-13<br />total: 4491924","Date: 2020-06-14<br />total: 4345782","Date: 2020-06-15<br />total: 4719121","Date: 2020-06-16<br />total: 4602070","Date: 2020-06-17<br />total: 4645645","Date: 2020-06-18<br />total: 4522965","Date: 2020-06-19<br />total: 4579185","Date: 2020-06-20<br />total: 4408125","Date: 2020-06-21<br />total: 4312872","Date: 2020-06-22<br />total: 4626294","Date: 2020-06-23<br />total: 4778853","Date: 2020-06-24<br />total: 4760720","Date: 2020-06-25<br />total: 4927751","Date: 2020-06-26<br />total: 4900490","Date: 2020-06-27<br />total: 4633288","Date: 2020-06-28<br />total: 4611867","Date: 2020-06-29<br />total: 4758478","Date: 2020-06-30<br />total: 5074891","Date: 2020-07-01<br />total: 5066747","Date: 2020-07-02<br />total: 4757030","Date: 2020-07-03<br />total: 4818268","Date: 2020-07-04<br />total: 4653034","Date: 2020-07-05<br />total: 4666372","Date: 2020-07-06<br />total: 4966247","Date: 2020-07-08<br />total: 4966733","Date: 2020-07-09<br />total: 4724475","Date: 2020-07-10<br />total: 4602458","Date: 2020-07-11<br />total: 4367496","Date: 2020-07-12<br />total: 4119296","Date: 2020-07-13<br />total: 5549327","Date: 2020-07-14<br />total: 4998739","Date: 2020-07-15<br />total: 5314638","Date: 2020-07-16<br />total: 5122505","Date: 2020-07-17<br />total: 5137243","Date: 2020-07-18<br />total: 4916051","Date: 2020-07-19<br />total: 5091562","Date: 2020-07-20<br />total: 4895498","Date: 2020-07-21<br />total: 5071583","Date: 2020-07-22<br />total: 5030064","Date: 2020-07-23<br />total: 4861094","Date: 2020-07-24<br />total: 4648985","Date: 2020-07-25<br />total: 4543164","Date: 2020-07-26<br />total: 4493827","Date: 2020-07-27<br />total: 4803863","Date: 2020-07-28<br />total: 5200574","Date: 2020-07-29<br />total: 5153883","Date: 2020-07-30<br />total: 5020051","Date: 2020-07-31<br />total: 4822691","Date: 2020-08-01<br />total: 4508204","Date: 2020-08-02<br />total: 4707409","Date: 2020-08-03<br />total: 4482064","Date: 2020-08-04<br />total: 4858355","Date: 2020-08-05<br />total: 4300412","Date: 2020-08-06<br />total: 4472590","Date: 2020-08-07<br />total: 4655061","Date: 2020-08-08<br />total: 4136621","Date: 2020-08-09<br />total: 4633092","Date: 2020-08-10<br />total: 4935200","Date: 2020-08-11<br />total: 4862710","Date: 2020-08-12<br />total: 4356173","Date: 2020-08-13<br />total: 4617337","Date: 2020-08-14<br />total: 4466298","Date: 2020-08-15<br />total: 4235274","Date: 2020-08-16<br />total: 4200107","Date: 2020-08-17<br />total: 4366290","Date: 2020-08-18<br />total: 4389130","Date: 2020-08-19<br />total: 4393857","Date: 2020-08-20<br />total: 4455164","Date: 2020-08-21<br />total: 4622409","Date: 2020-08-22<br />total: 4487676","Date: 2020-08-23<br />total: 4737102","Date: 2020-08-24<br />total: 4744988","Date: 2020-08-25<br />total: 4808933","Date: 2020-08-26<br />total: 4781885","Date: 2020-08-27<br />total: 4802854","Date: 2020-08-28<br />total: 4763210","Date: 2020-08-29<br />total: 4083157","Date: 2020-08-30<br />total: 4320991","Date: 2020-08-31<br />total: 4510217"],"type":"scatter","mode":"lines","line":{"width":3.77952755905512,"color":"rgba(0,0,255,1)","dash":"solid"},"hoveron":"points","showlegend":false,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null}],"layout":{"margin":{"t":44.8252386882524,"r":7.30593607305936,"b":45.7617268576173,"l":62.7646326276463},"plot_bgcolor":"rgba(255,255,255,1)","paper_bgcolor":"rgba(255,255,255,1)","font":{"color":"rgba(0,0,0,1)","family":"","size":14.6118721461187},"title":{"text":"<b> Number of Tweets per day <\/b>","font":{"color":"rgba(0,0,0,1)","family":"","size":18.5969281859693},"x":0,"xref":"paper"},"xaxis":{"domain":[0,1],"automargin":true,"type":"linear","autorange":false,"range":[18271.9,18516.1],"tickmode":"array","ticktext":["Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"],"tickvals":[18293,18322,18353,18383,18414,18444,18475,18506],"categoryorder":"array","categoryarray":["Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"],"nticks":null,"ticks":"outside","tickcolor":"rgba(51,51,51,1)","ticklen":3.65296803652968,"tickwidth":0.66417600664176,"showticklabels":true,"tickfont":{"color":"rgba(0,0,0,1)","family":"","size":13.2835201328352},"tickangle":-0,"showline":false,"linecolor":null,"linewidth":0,"showgrid":true,"gridcolor":"rgba(235,235,235,1)","gridwidth":0.66417600664176,"zeroline":false,"anchor":"y","title":{"text":"<b> Date <\/b>","font":{"color":"rgba(0,0,0,1)","family":"","size":18.5969281859693}},"hoverformat":".2f"},"yaxis":{"domain":[0,1],"automargin":true,"type":"linear","autorange":false,"range":[-239316.7,5824976.7],"tickmode":"array","ticktext":["0e+00","2e+06","4e+06"],"tickvals":[0,2000000,4000000],"categoryorder":"array","categoryarray":["0e+00","2e+06","4e+06"],"nticks":null,"ticks":"outside","tickcolor":"rgba(51,51,51,1)","ticklen":3.65296803652968,"tickwidth":0.66417600664176,"showticklabels":true,"tickfont":{"color":"rgba(0,0,0,1)","family":"","size":13.2835201328352},"tickangle":-0,"showline":false,"linecolor":null,"linewidth":0,"showgrid":true,"gridcolor":"rgba(235,235,235,1)","gridwidth":0.66417600664176,"zeroline":false,"anchor":"x","title":{"text":"<b> Number of Tweets <\/b>","font":{"color":"rgba(0,0,0,1)","family":"","size":18.5969281859693}},"hoverformat":".2f"},"shapes":[{"type":"rect","fillcolor":"transparent","line":{"color":"rgba(51,51,51,1)","width":0.66417600664176,"linetype":"solid"},"yref":"paper","xref":"paper","x0":0,"x1":1,"y0":0,"y1":1}],"showlegend":false,"legend":{"bgcolor":"rgba(255,255,255,1)","bordercolor":"transparent","borderwidth":1.88976377952756,"font":{"color":"rgba(0,0,0,1)","family":"","size":13.2835201328352}},"hovermode":"closest","barmode":"relative"},"config":{"doubleClick":"reset","showSendToCloud":false},"source":"A","attrs":{"3338ff6509a":{"x":{},"y":{},"type":"scatter"}},"cur_data":"3338ff6509a","visdat":{"3338ff6509a":["function (y) ","x"]},"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.2,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>

<!--/html_preserve-->

There is a total of 284,884 tweets with geolocation information are
present on the dataset, which are shown on a map below:
![](README_RMD_files/figure-gfm/unnamed-chunk-5-1.png)<!-- -->

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

<!--html_preserve-->

<div id="htmlwidget-74ae302355f9fd588250" class="plotly html-widget" style="width:672px;height:480px;">

</div>

<script type="application/json" data-for="htmlwidget-74ae302355f9fd588250">{"x":{"data":[{"x":[18290,18291,18292,18293,18294,18295,18296,18297,18298,18299,18300,18301,18302,18303,18304,18305,18306,18307,18308,18309,18310,18311,18312,18313,18314,18315,18316,18317,18318,18319,18320,18321,18322,18323,18324,18325,18326,18327,18328,18329,18330,18331,18332,18333,18334,18335,18336,18337,18338,18339,18340,18341,18342,18343,18344,18345,18346,18347,18348,18349,18350,18351,18352,18353,18354,18355,18356,18357,18358,18359,18360,18361,18362,18363,18364,18365,18366,18367,18368,18369,18370,18371,18372,18373,18374,18375,18376,18377,18378,18379,18380,18381,18382,18383,18384,18385,18386,18387,18388,18389,18390,18391,18392,18393,18394,18395,18396,18397,18398,18399,18400,18401,18402,18403,18404,18405,18406,18407,18408,18409,18410,18411,18412,18413,18414,18415,18416,18417,18418,18419,18420,18421,18422,18423,18424,18425,18426,18427,18428,18429,18430,18431,18432,18433,18434,18435,18436,18437,18438,18439,18440,18441,18442,18443,18444,18445,18446,18447,18448,18449,18451,18452,18453,18454,18455,18456,18457,18458,18459,18460,18461,18462,18463,18464,18465,18466,18467,18468,18469,18470,18471,18472,18473,18474,18475,18476,18477,18478,18479,18480,18481,18482,18483,18484,18485,18486,18487,18488,18489,18490,18491,18492,18493,18494,18495,18496,18497,18498,18499,18500,18501,18502,18503,18504,18505],"y":[49766,32265,27239,28446,39281,54752,50175,49951,43400,39561,41982,42213,43207,49447,33024,41617,43029,44536,37695,22625,28533,21453,19508,21967,18867,6837,34638,20742,27680,23633,27493,26271,28171,116158,109031,61754,39436,30719,20691,24121,22602,17848,25250,20710,24282,45423,63665,68479,127459,81499,187705,156316,176030,194115,158319,49065,47224,154290,148794,159011,141710,105651,40607,61938,98854,107079,110878,113385,102444,92236,69342,39959,89846,91034,81575,84448,88459,81911,71362,90547,45434,74232,76029,26597,82686,74936,39766,55016,51128,54546,54819,34575,57024,57729,62054,50870,58696,42331,80490,121705,138400,169305,135794,176678,149036,146851,170647,168063,124917,121283,196218,173672,179625,165231,173688,125706,93781,109166,127548,131261,121052,123440,113170,99990,129224,126847,117633,131543,57832,105525,130511,171162,180914,187296,167220,136383,124573,110541,101094,122564,113644,92396,86784,81152,102375,111039,102282,97298,84951,93534,88290,68060,70865,103341,119818,109005,101914,89169,89928,92876,88805,94708,124054,86613,62443,87146,81293,101321,78446,71559,82602,135607,155713,143550,143003,119204,110914,109347,126250,143690,156042,140689,135092,63812,88671,147225,125695,105939,94079,77852,125815,107091,91757,98624,97769,120209,90142,87248,88451,99128,65451,69642,105829,97592,87677,68197,83122,78795,76335,101889,110138,114664,98161,117878,118912],"text":["Date: 2020-01-29<br />total:   49766<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-01-30<br />total:   32265<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-01-31<br />total:   27239<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-01<br />total:   28446<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-02<br />total:   39281<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-03<br />total:   54752<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-04<br />total:   50175<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-05<br />total:   49951<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-06<br />total:   43400<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-07<br />total:   39561<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-08<br />total:   41982<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-09<br />total:   42213<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-10<br />total:   43207<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-11<br />total:   49447<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-12<br />total:   33024<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-13<br />total:   41617<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-14<br />total:   43029<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-15<br />total:   44536<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-16<br />total:   37695<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-17<br />total:   22625<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-18<br />total:   28533<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-19<br />total:   21453<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-20<br />total:   19508<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-21<br />total:   21967<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-22<br />total:   18867<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-23<br />total:    6837<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-24<br />total:   34638<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-25<br />total:   20742<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-26<br />total:   27680<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-27<br />total:   23633<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-28<br />total:   27493<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-02-29<br />total:   26271<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-01<br />total:   28171<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-02<br />total:  116158<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-03<br />total:  109031<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-04<br />total:   61754<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-05<br />total:   39436<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-06<br />total:   30719<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-07<br />total:   20691<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-08<br />total:   24121<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-09<br />total:   22602<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-10<br />total:   17848<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-11<br />total:   25250<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-12<br />total:   20710<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-13<br />total:   24282<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-14<br />total:   45423<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-15<br />total:   63665<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-16<br />total:   68479<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-17<br />total:  127459<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-18<br />total:   81499<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-19<br />total:  187705<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-20<br />total:  156316<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-21<br />total:  176030<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-22<br />total:  194115<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-23<br />total:  158319<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-24<br />total:   49065<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-25<br />total:   47224<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-26<br />total:  154290<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-27<br />total:  148794<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-28<br />total:  159011<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-29<br />total:  141710<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-30<br />total:  105651<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-03-31<br />total:   40607<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-01<br />total:   61938<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-02<br />total:   98854<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-03<br />total:  107079<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-04<br />total:  110878<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-05<br />total:  113385<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-06<br />total:  102444<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-07<br />total:   92236<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-08<br />total:   69342<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-09<br />total:   39959<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-10<br />total:   89846<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-11<br />total:   91034<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-12<br />total:   81575<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-13<br />total:   84448<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-14<br />total:   88459<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-15<br />total:   81911<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-16<br />total:   71362<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-17<br />total:   90547<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-18<br />total:   45434<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-19<br />total:   74232<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-20<br />total:   76029<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-21<br />total:   26597<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-22<br />total:   82686<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-23<br />total:   74936<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-24<br />total:   39766<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-25<br />total:   55016<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-26<br />total:   51128<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-27<br />total:   54546<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-28<br />total:   54819<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-29<br />total:   34575<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-04-30<br />total:   57024<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-01<br />total:   57729<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-02<br />total:   62054<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-03<br />total:   50870<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-04<br />total:   58696<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-05<br />total:   42331<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-06<br />total:   80490<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-07<br />total:  121705<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-08<br />total:  138400<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-09<br />total:  169305<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-10<br />total:  135794<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-11<br />total:  176678<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-12<br />total:  149036<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-13<br />total:  146851<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-14<br />total:  170647<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-15<br />total:  168063<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-16<br />total:  124917<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-17<br />total:  121283<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-18<br />total:  196218<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-19<br />total:  173672<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-20<br />total:  179625<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-21<br />total:  165231<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-22<br />total:  173688<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-23<br />total:  125706<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-24<br />total:   93781<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-25<br />total:  109166<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-26<br />total:  127548<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-27<br />total:  131261<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-28<br />total:  121052<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-29<br />total:  123440<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-30<br />total:  113170<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-05-31<br />total:   99990<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-01<br />total:  129224<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-02<br />total:  126847<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-03<br />total:  117633<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-04<br />total:  131543<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-05<br />total:   57832<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-06<br />total:  105525<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-07<br />total:  130511<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-08<br />total:  171162<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-09<br />total:  180914<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-10<br />total:  187296<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-11<br />total:  167220<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-12<br />total:  136383<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-13<br />total:  124573<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-14<br />total:  110541<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-15<br />total:  101094<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-16<br />total:  122564<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-17<br />total:  113644<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-18<br />total:   92396<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-19<br />total:   86784<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-20<br />total:   81152<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-21<br />total:  102375<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-22<br />total:  111039<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-23<br />total:  102282<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-24<br />total:   97298<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-25<br />total:   84951<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-26<br />total:   93534<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-27<br />total:   88290<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-28<br />total:   68060<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-29<br />total:   70865<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-06-30<br />total:  103341<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-01<br />total:  119818<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-02<br />total:  109005<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-03<br />total:  101914<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-04<br />total:   89169<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-05<br />total:   89928<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-06<br />total:   92876<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-08<br />total:   88805<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-09<br />total:   94708<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-10<br />total:  124054<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-11<br />total:   86613<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-12<br />total:   62443<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-13<br />total:   87146<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-14<br />total:   81293<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-15<br />total:  101321<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-16<br />total:   78446<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-17<br />total:   71559<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-18<br />total:   82602<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-19<br />total:  135607<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-20<br />total:  155713<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-21<br />total:  143550<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-22<br />total:  143003<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-23<br />total:  119204<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-24<br />total:  110914<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-25<br />total:  109347<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-26<br />total:  126250<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-27<br />total:  143690<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-28<br />total:  156042<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-29<br />total:  140689<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-30<br />total:  135092<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-07-31<br />total:   63812<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-01<br />total:   88671<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-02<br />total:  147225<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-03<br />total:  125695<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-04<br />total:  105939<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-05<br />total:   94079<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-06<br />total:   77852<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-07<br />total:  125815<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-08<br />total:  107091<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-09<br />total:   91757<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-10<br />total:   98624<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-11<br />total:   97769<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-12<br />total:  120209<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-13<br />total:   90142<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-14<br />total:   87248<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-15<br />total:   88451<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-16<br />total:   99128<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-17<br />total:   65451<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-18<br />total:   69642<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-19<br />total:  105829<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-20<br />total:   97592<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-21<br />total:   87677<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-22<br />total:   68197<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-23<br />total:   83122<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-24<br />total:   78795<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-25<br />total:   76335<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-26<br />total:  101889<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-27<br />total:  110138<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-28<br />total:  114664<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-29<br />total:   98161<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-30<br />total:  117878<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa","Date: 2020-08-31<br />total:  118912<br />TopLanguages: Bahasa<br />TopLanguages: Bahasa"],"type":"scatter","mode":"lines","line":{"width":3.77952755905512,"color":"rgba(248,118,109,1)","dash":"solid"},"hoveron":"points","name":"(Bahasa,1)","legendgroup":"(Bahasa,1)","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null},{"x":[18283,18284,18285,18286,18287,18288,18289,18290,18291,18292,18293,18294,18295,18296,18297,18298,18299,18300,18301,18302,18303,18304,18305,18306,18307,18308,18309,18310,18311,18312,18313,18314,18315,18316,18317,18318,18319,18320,18321,18322,18323,18324,18325,18326,18327,18328,18329,18330,18331,18332,18333,18334,18335,18336,18337,18338,18339,18340,18341,18342,18343,18344,18345,18346,18347,18348,18349,18350,18351,18352,18353,18354,18355,18356,18357,18358,18359,18360,18361,18362,18363,18364,18365,18366,18367,18368,18369,18370,18371,18372,18373,18374,18375,18376,18377,18378,18379,18380,18381,18382,18383,18384,18385,18386,18387,18388,18389,18390,18391,18392,18393,18394,18395,18396,18397,18398,18399,18400,18401,18402,18403,18404,18405,18406,18407,18408,18409,18410,18411,18412,18413,18414,18415,18416,18417,18418,18419,18420,18421,18422,18423,18424,18425,18426,18427,18428,18429,18430,18431,18432,18433,18434,18435,18436,18437,18438,18439,18440,18441,18442,18443,18444,18445,18446,18447,18448,18449,18451,18452,18453,18454,18455,18456,18457,18458,18459,18460,18461,18462,18463,18464,18465,18466,18467,18468,18469,18470,18471,18472,18473,18474,18475,18476,18477,18478,18479,18480,18481,18482,18483,18484,18485,18486,18487,18488,18489,18490,18491,18492,18493,18494,18495,18496,18497,18498,18499,18500,18501,18502,18503,18504,18505],"y":[36333,203690,568485,856089,1137733,871085,765992,1224525,1561487,1393585,486900,509001,495045,558396,507140,543362,523715,521650,508788,577651,588881,543023,608078,576842,453694,486730,528290,559986,505266,518655,533032,434464,76071,418256,479743,532390,670245,1492092,3041483,2250195,564022,2410598,2604086,726491,767869,772467,745449,753786,726316,727766,734379,715549,681795,644804,626233,1433218,927825,1636423,1662311,1497630,1698929,1748497,551877,726550,1781603,1548016,1732811,1737546,1230535,604063,1169231,1680635,1614136,1722087,1729939,1767999,1826123,1287612,1157234,1788110,1686239,1625395,1692642,1744272,1777949,1776688,1712131,1485001,1797245,1794571,526221,1751670,1860108,2090916,2373564,2354468,2414814,1787207,1376137,1963210,1882969,1900477,1985777,2117569,1172105,2232762,2559002,2318809,2261678,2286728,2648858,2581463,2689604,2584430,2540377,2312083,2328238,2494425,2429493,2400226,2370994,2182634,2119521,2132637,2068703,2043111,1981592,2147959,2211589,2090574,2014775,1987699,1939265,1925941,1908654,1456912,2646011,2601141,2620845,2711372,2924588,3016319,2997384,2889344,2791767,3223194,3133066,3118350,3026566,3089624,2965867,2961048,3090288,3395809,3398807,3563402,3780386,3463096,3401090,3527474,3752314,3752756,3604467,3632628,3457444,3391128,3717419,3623043,3451017,3264217,3115726,2845198,3991115,3720892,3983474,3871505,3836606,3455728,3482981,3239873,3388552,3384282,3255103,3120301,3139699,2970221,3305613,3696199,3577773,3577533,3453650,3037256,3245526,3092428,3356324,2886790,3088009,3097547,2767359,3076335,3432854,3302918,2705417,2970374,2931767,2702714,2601192,2760159,2948121,2862807,2932765,3201233,3016705,3376382,3216140,3294857,3279885,3210708,3308778,2657546,2859399,3040227],"text":["Date: 2020-01-22<br />total:   36333<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-01-23<br />total:  203690<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-01-24<br />total:  568485<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-01-25<br />total:  856089<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-01-26<br />total: 1137733<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-01-27<br />total:  871085<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-01-28<br />total:  765992<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-01-29<br />total: 1224525<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-01-30<br />total: 1561487<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-01-31<br />total: 1393585<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-01<br />total:  486900<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-02<br />total:  509001<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-03<br />total:  495045<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-04<br />total:  558396<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-05<br />total:  507140<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-06<br />total:  543362<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-07<br />total:  523715<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-08<br />total:  521650<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-09<br />total:  508788<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-10<br />total:  577651<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-11<br />total:  588881<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-12<br />total:  543023<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-13<br />total:  608078<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-14<br />total:  576842<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-15<br />total:  453694<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-16<br />total:  486730<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-17<br />total:  528290<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-18<br />total:  559986<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-19<br />total:  505266<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-20<br />total:  518655<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-21<br />total:  533032<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-22<br />total:  434464<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-23<br />total:   76071<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-24<br />total:  418256<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-25<br />total:  479743<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-26<br />total:  532390<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-27<br />total:  670245<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-28<br />total: 1492092<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-02-29<br />total: 3041483<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-01<br />total: 2250195<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-02<br />total:  564022<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-03<br />total: 2410598<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-04<br />total: 2604086<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-05<br />total:  726491<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-06<br />total:  767869<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-07<br />total:  772467<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-08<br />total:  745449<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-09<br />total:  753786<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-10<br />total:  726316<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-11<br />total:  727766<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-12<br />total:  734379<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-13<br />total:  715549<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-14<br />total:  681795<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-15<br />total:  644804<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-16<br />total:  626233<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-17<br />total: 1433218<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-18<br />total:  927825<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-19<br />total: 1636423<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-20<br />total: 1662311<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-21<br />total: 1497630<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-22<br />total: 1698929<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-23<br />total: 1748497<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-24<br />total:  551877<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-25<br />total:  726550<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-26<br />total: 1781603<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-27<br />total: 1548016<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-28<br />total: 1732811<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-29<br />total: 1737546<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-30<br />total: 1230535<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-03-31<br />total:  604063<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-01<br />total: 1169231<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-02<br />total: 1680635<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-03<br />total: 1614136<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-04<br />total: 1722087<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-05<br />total: 1729939<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-06<br />total: 1767999<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-07<br />total: 1826123<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-08<br />total: 1287612<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-09<br />total: 1157234<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-10<br />total: 1788110<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-11<br />total: 1686239<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-12<br />total: 1625395<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-13<br />total: 1692642<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-14<br />total: 1744272<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-15<br />total: 1777949<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-16<br />total: 1776688<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-17<br />total: 1712131<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-18<br />total: 1485001<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-19<br />total: 1797245<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-20<br />total: 1794571<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-21<br />total:  526221<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-22<br />total: 1751670<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-23<br />total: 1860108<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-24<br />total: 2090916<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-25<br />total: 2373564<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-26<br />total: 2354468<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-27<br />total: 2414814<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-28<br />total: 1787207<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-29<br />total: 1376137<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-04-30<br />total: 1963210<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-01<br />total: 1882969<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-02<br />total: 1900477<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-03<br />total: 1985777<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-04<br />total: 2117569<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-05<br />total: 1172105<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-06<br />total: 2232762<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-07<br />total: 2559002<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-08<br />total: 2318809<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-09<br />total: 2261678<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-10<br />total: 2286728<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-11<br />total: 2648858<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-12<br />total: 2581463<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-13<br />total: 2689604<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-14<br />total: 2584430<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-15<br />total: 2540377<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-16<br />total: 2312083<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-17<br />total: 2328238<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-18<br />total: 2494425<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-19<br />total: 2429493<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-20<br />total: 2400226<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-21<br />total: 2370994<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-22<br />total: 2182634<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-23<br />total: 2119521<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-24<br />total: 2132637<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-25<br />total: 2068703<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-26<br />total: 2043111<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-27<br />total: 1981592<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-28<br />total: 2147959<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-29<br />total: 2211589<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-30<br />total: 2090574<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-05-31<br />total: 2014775<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-01<br />total: 1987699<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-02<br />total: 1939265<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-03<br />total: 1925941<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-04<br />total: 1908654<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-05<br />total: 1456912<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-06<br />total: 2646011<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-07<br />total: 2601141<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-08<br />total: 2620845<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-09<br />total: 2711372<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-10<br />total: 2924588<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-11<br />total: 3016319<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-12<br />total: 2997384<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-13<br />total: 2889344<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-14<br />total: 2791767<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-15<br />total: 3223194<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-16<br />total: 3133066<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-17<br />total: 3118350<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-18<br />total: 3026566<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-19<br />total: 3089624<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-20<br />total: 2965867<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-21<br />total: 2961048<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-22<br />total: 3090288<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-23<br />total: 3395809<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-24<br />total: 3398807<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-25<br />total: 3563402<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-26<br />total: 3780386<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-27<br />total: 3463096<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-28<br />total: 3401090<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-29<br />total: 3527474<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-06-30<br />total: 3752314<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-01<br />total: 3752756<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-02<br />total: 3604467<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-03<br />total: 3632628<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-04<br />total: 3457444<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-05<br />total: 3391128<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-06<br />total: 3717419<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-08<br />total: 3623043<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-09<br />total: 3451017<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-10<br />total: 3264217<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-11<br />total: 3115726<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-12<br />total: 2845198<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-13<br />total: 3991115<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-14<br />total: 3720892<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-15<br />total: 3983474<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-16<br />total: 3871505<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-17<br />total: 3836606<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-18<br />total: 3455728<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-19<br />total: 3482981<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-20<br />total: 3239873<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-21<br />total: 3388552<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-22<br />total: 3384282<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-23<br />total: 3255103<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-24<br />total: 3120301<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-25<br />total: 3139699<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-26<br />total: 2970221<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-27<br />total: 3305613<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-28<br />total: 3696199<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-29<br />total: 3577773<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-30<br />total: 3577533<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-07-31<br />total: 3453650<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-01<br />total: 3037256<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-02<br />total: 3245526<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-03<br />total: 3092428<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-04<br />total: 3356324<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-05<br />total: 2886790<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-06<br />total: 3088009<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-07<br />total: 3097547<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-08<br />total: 2767359<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-09<br />total: 3076335<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-10<br />total: 3432854<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-11<br />total: 3302918<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-12<br />total: 2705417<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-13<br />total: 2970374<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-14<br />total: 2931767<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-15<br />total: 2702714<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-16<br />total: 2601192<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-17<br />total: 2760159<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-18<br />total: 2948121<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-19<br />total: 2862807<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-20<br />total: 2932765<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-21<br />total: 3201233<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-22<br />total: 3016705<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-23<br />total: 3376382<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-24<br />total: 3216140<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-25<br />total: 3294857<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-26<br />total: 3279885<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-27<br />total: 3210708<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-28<br />total: 3308778<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-29<br />total: 2657546<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-30<br />total: 2859399<br />TopLanguages: English<br />TopLanguages: English","Date: 2020-08-31<br />total: 3040227<br />TopLanguages: English<br />TopLanguages: English"],"type":"scatter","mode":"lines","line":{"width":3.77952755905512,"color":"rgba(163,165,0,1)","dash":"solid"},"hoveron":"points","name":"(English,1)","legendgroup":"(English,1)","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null},{"x":[18290,18291,18292,18293,18294,18295,18296,18297,18298,18299,18300,18301,18302,18303,18304,18305,18306,18307,18308,18309,18310,18311,18312,18313,18314,18315,18316,18317,18318,18319,18320,18321,18322,18323,18324,18325,18326,18327,18328,18329,18330,18331,18332,18333,18334,18335,18336,18337,18338,18339,18340,18341,18342,18343,18344,18345,18346,18347,18348,18349,18350,18351,18352,18353,18354,18355,18356,18357,18358,18359,18360,18361,18362,18363,18364,18365,18366,18367,18368,18369,18370,18371,18372,18373,18374,18375,18376,18377,18378,18379,18380,18381,18382,18383,18384,18385,18386,18387,18388,18389,18390,18391,18392,18393,18394,18395,18396,18397,18398,18399,18400,18401,18402,18403,18404,18405,18406,18407,18408,18409,18410,18411,18412,18413,18414,18415,18416,18417,18418,18419,18420,18421,18422,18423,18424,18425,18426,18427,18428,18429,18430,18431,18432,18433,18434,18435,18436,18437,18438,18439,18440,18441,18442,18443,18444,18445,18446,18447,18448,18449,18451,18452,18453,18454,18455,18456,18457,18458,18459,18460,18461,18462,18463,18464,18465,18466,18467,18468,18469,18470,18471,18472,18473,18474,18475,18476,18477,18478,18479,18480,18481,18482,18483,18484,18485,18486,18487,18488,18489,18490,18491,18492,18493,18494,18495,18496,18497,18498,18499,18500,18501,18502,18503,18504,18505],"y":[30280,27260,22115,16546,31343,24535,30274,28360,26264,22576,34097,45786,47162,34046,24851,23442,18434,21528,40203,36212,48784,20320,17137,18695,19046,7895,50289,49398,48257,52333,49174,46889,38693,60743,69347,59172,56650,59673,50016,50549,49051,45721,40967,43498,39106,51714,61020,56409,111908,56833,106267,122150,117881,109703,94431,29798,40853,97737,87252,117471,126687,71890,32657,67138,102266,107874,110244,101931,105254,104499,72719,60476,92978,97297,93974,110190,101239,100598,104386,114771,69112,95567,91518,26427,92996,91518,72537,89244,86360,78720,66331,63726,90922,76689,79746,98500,93323,43539,86550,80408,68326,78337,83205,98912,69486,70079,62087,71122,65283,57397,56462,57400,56005,51962,55259,55285,45752,51270,53240,55216,63340,52716,51058,54637,62723,63019,52966,53071,52863,79601,69523,82649,70543,95345,79596,66402,68005,74313,80630,110399,102571,72662,74557,74799,62792,70136,62997,69579,72090,55061,53785,47857,50525,67259,69806,59013,54284,60506,68900,62092,74095,77434,55450,52291,59876,73123,72647,60682,68616,74137,69303,71118,74006,79862,79554,72183,82232,71656,84866,71022,69063,82580,94012,93376,87218,76231,67818,87698,79905,80805,75260,57030,75452,75824,78332,77178,79314,92370,99680,93025,117907,99880,100553,106425,95535,93235,87620,90999,99747,98013,137842,128798,105872,124564,107558],"text":["Date: 2020-01-29<br />total:   30280<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-01-30<br />total:   27260<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-01-31<br />total:   22115<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-01<br />total:   16546<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-02<br />total:   31343<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-03<br />total:   24535<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-04<br />total:   30274<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-05<br />total:   28360<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-06<br />total:   26264<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-07<br />total:   22576<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-08<br />total:   34097<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-09<br />total:   45786<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-10<br />total:   47162<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-11<br />total:   34046<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-12<br />total:   24851<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-13<br />total:   23442<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-14<br />total:   18434<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-15<br />total:   21528<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-16<br />total:   40203<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-17<br />total:   36212<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-18<br />total:   48784<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-19<br />total:   20320<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-20<br />total:   17137<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-21<br />total:   18695<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-22<br />total:   19046<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-23<br />total:    7895<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-24<br />total:   50289<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-25<br />total:   49398<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-26<br />total:   48257<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-27<br />total:   52333<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-28<br />total:   49174<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-02-29<br />total:   46889<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-01<br />total:   38693<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-02<br />total:   60743<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-03<br />total:   69347<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-04<br />total:   59172<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-05<br />total:   56650<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-06<br />total:   59673<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-07<br />total:   50016<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-08<br />total:   50549<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-09<br />total:   49051<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-10<br />total:   45721<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-11<br />total:   40967<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-12<br />total:   43498<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-13<br />total:   39106<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-14<br />total:   51714<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-15<br />total:   61020<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-16<br />total:   56409<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-17<br />total:  111908<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-18<br />total:   56833<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-19<br />total:  106267<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-20<br />total:  122150<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-21<br />total:  117881<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-22<br />total:  109703<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-23<br />total:   94431<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-24<br />total:   29798<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-25<br />total:   40853<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-26<br />total:   97737<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-27<br />total:   87252<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-28<br />total:  117471<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-29<br />total:  126687<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-30<br />total:   71890<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-03-31<br />total:   32657<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-01<br />total:   67138<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-02<br />total:  102266<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-03<br />total:  107874<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-04<br />total:  110244<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-05<br />total:  101931<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-06<br />total:  105254<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-07<br />total:  104499<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-08<br />total:   72719<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-09<br />total:   60476<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-10<br />total:   92978<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-11<br />total:   97297<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-12<br />total:   93974<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-13<br />total:  110190<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-14<br />total:  101239<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-15<br />total:  100598<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-16<br />total:  104386<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-17<br />total:  114771<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-18<br />total:   69112<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-19<br />total:   95567<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-20<br />total:   91518<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-21<br />total:   26427<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-22<br />total:   92996<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-23<br />total:   91518<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-24<br />total:   72537<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-25<br />total:   89244<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-26<br />total:   86360<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-27<br />total:   78720<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-28<br />total:   66331<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-29<br />total:   63726<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-04-30<br />total:   90922<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-01<br />total:   76689<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-02<br />total:   79746<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-03<br />total:   98500<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-04<br />total:   93323<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-05<br />total:   43539<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-06<br />total:   86550<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-07<br />total:   80408<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-08<br />total:   68326<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-09<br />total:   78337<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-10<br />total:   83205<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-11<br />total:   98912<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-12<br />total:   69486<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-13<br />total:   70079<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-14<br />total:   62087<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-15<br />total:   71122<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-16<br />total:   65283<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-17<br />total:   57397<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-18<br />total:   56462<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-19<br />total:   57400<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-20<br />total:   56005<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-21<br />total:   51962<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-22<br />total:   55259<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-23<br />total:   55285<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-24<br />total:   45752<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-25<br />total:   51270<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-26<br />total:   53240<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-27<br />total:   55216<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-28<br />total:   63340<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-29<br />total:   52716<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-30<br />total:   51058<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-05-31<br />total:   54637<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-01<br />total:   62723<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-02<br />total:   63019<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-03<br />total:   52966<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-04<br />total:   53071<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-05<br />total:   52863<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-06<br />total:   79601<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-07<br />total:   69523<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-08<br />total:   82649<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-09<br />total:   70543<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-10<br />total:   95345<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-11<br />total:   79596<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-12<br />total:   66402<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-13<br />total:   68005<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-14<br />total:   74313<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-15<br />total:   80630<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-16<br />total:  110399<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-17<br />total:  102571<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-18<br />total:   72662<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-19<br />total:   74557<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-20<br />total:   74799<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-21<br />total:   62792<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-22<br />total:   70136<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-23<br />total:   62997<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-24<br />total:   69579<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-25<br />total:   72090<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-26<br />total:   55061<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-27<br />total:   53785<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-28<br />total:   47857<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-29<br />total:   50525<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-06-30<br />total:   67259<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-01<br />total:   69806<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-02<br />total:   59013<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-03<br />total:   54284<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-04<br />total:   60506<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-05<br />total:   68900<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-06<br />total:   62092<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-08<br />total:   74095<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-09<br />total:   77434<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-10<br />total:   55450<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-11<br />total:   52291<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-12<br />total:   59876<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-13<br />total:   73123<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-14<br />total:   72647<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-15<br />total:   60682<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-16<br />total:   68616<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-17<br />total:   74137<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-18<br />total:   69303<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-19<br />total:   71118<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-20<br />total:   74006<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-21<br />total:   79862<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-22<br />total:   79554<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-23<br />total:   72183<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-24<br />total:   82232<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-25<br />total:   71656<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-26<br />total:   84866<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-27<br />total:   71022<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-28<br />total:   69063<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-29<br />total:   82580<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-30<br />total:   94012<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-07-31<br />total:   93376<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-01<br />total:   87218<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-02<br />total:   76231<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-03<br />total:   67818<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-04<br />total:   87698<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-05<br />total:   79905<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-06<br />total:   80805<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-07<br />total:   75260<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-08<br />total:   57030<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-09<br />total:   75452<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-10<br />total:   75824<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-11<br />total:   78332<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-12<br />total:   77178<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-13<br />total:   79314<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-14<br />total:   92370<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-15<br />total:   99680<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-16<br />total:   93025<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-17<br />total:  117907<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-18<br />total:   99880<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-19<br />total:  100553<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-20<br />total:  106425<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-21<br />total:   95535<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-22<br />total:   93235<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-23<br />total:   87620<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-24<br />total:   90999<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-25<br />total:   99747<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-26<br />total:   98013<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-27<br />total:  137842<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-28<br />total:  128798<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-29<br />total:  105872<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-30<br />total:  124564<br />TopLanguages: French<br />TopLanguages: French","Date: 2020-08-31<br />total:  107558<br />TopLanguages: French<br />TopLanguages: French"],"type":"scatter","mode":"lines","line":{"width":3.77952755905512,"color":"rgba(0,191,125,1)","dash":"solid"},"hoveron":"points","name":"(French,1)","legendgroup":"(French,1)","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null},{"x":[18290,18291,18292,18293,18294,18295,18296,18297,18298,18299,18300,18301,18302,18303,18304,18305,18306,18307,18308,18309,18310,18311,18312,18313,18314,18315,18316,18317,18318,18319,18320,18321,18322,18323,18324,18325,18326,18327,18328,18329,18330,18331,18332,18333,18334,18335,18336,18337,18338,18339,18340,18341,18342,18343,18344,18345,18346,18347,18348,18349,18350,18351,18352,18353,18354,18355,18356,18357,18358,18359,18360,18361,18362,18363,18364,18365,18366,18367,18368,18369,18370,18371,18372,18373,18374,18375,18376,18377,18378,18379,18380,18381,18382,18383,18384,18385,18386,18387,18388,18389,18390,18391,18392,18393,18394,18395,18396,18397,18398,18399,18400,18401,18402,18403,18404,18405,18406,18407,18408,18409,18410,18411,18412,18413,18414,18415,18416,18417,18418,18419,18420,18421,18422,18423,18424,18425,18426,18427,18428,18429,18430,18431,18432,18433,18434,18435,18436,18437,18438,18439,18440,18441,18442,18443,18444,18445,18446,18447,18448,18449,18451,18452,18453,18454,18455,18456,18457,18458,18459,18460,18461,18462,18463,18464,18465,18466,18467,18468,18469,18470,18471,18472,18473,18474,18475,18476,18477,18478,18479,18480,18481,18482,18483,18484,18485,18486,18487,18488,18489,18490,18491,18492,18493,18494,18495,18496,18497,18498,18499,18500,18501,18502,18503,18504,18505],"y":[53319,33554,27065,28796,30025,29793,35114,36429,33607,23308,24296,35707,23911,23700,13787,13681,14977,11370,14528,13862,13203,11974,14718,12532,9523,3261,11635,11289,83926,76497,55988,57279,31726,31128,28655,22900,24800,21856,16899,18412,19228,23860,29482,49923,69129,53836,50656,59160,141905,115005,219709,203371,202804,169642,180785,26936,54693,167338,147446,168839,155479,98846,25707,74441,125216,120761,146098,151660,167633,155792,89523,93256,138201,175082,166244,179038,168711,194211,167053,140877,79003,146475,138260,24248,152828,134863,66058,87802,94317,107805,77371,121894,158004,141348,162440,147388,137565,54483,141548,212695,188997,154086,123810,146597,159855,192929,171075,184765,193674,196018,186088,225858,256029,170902,172534,129008,125916,166015,146346,115698,109631,122369,109935,154096,178275,136513,145343,143974,173089,454923,435533,352885,345522,248535,213567,244133,214722,248902,189041,166219,164883,192537,199658,160878,218238,221475,185292,207022,159678,120036,148601,188133,188622,180292,153349,132349,148418,134560,145302,150112,256141,142362,129843,134641,123943,149416,151401,184884,158049,153384,193770,250875,332248,289177,230968,222979,191264,164013,172581,141143,173683,220772,187738,181318,137355,140887,139058,148667,122411,134655,148718,208467,332384,193997,226112,267358,207530,143105,127186,138402,123989,115085,136565,156404,159747,135788,113105,162084,169096,113761,115832,136278,124671,146517,168936],"text":["Date: 2020-01-29<br />total:   53319<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-01-30<br />total:   33554<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-01-31<br />total:   27065<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-01<br />total:   28796<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-02<br />total:   30025<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-03<br />total:   29793<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-04<br />total:   35114<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-05<br />total:   36429<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-06<br />total:   33607<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-07<br />total:   23308<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-08<br />total:   24296<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-09<br />total:   35707<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-10<br />total:   23911<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-11<br />total:   23700<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-12<br />total:   13787<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-13<br />total:   13681<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-14<br />total:   14977<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-15<br />total:   11370<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-16<br />total:   14528<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-17<br />total:   13862<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-18<br />total:   13203<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-19<br />total:   11974<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-20<br />total:   14718<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-21<br />total:   12532<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-22<br />total:    9523<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-23<br />total:    3261<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-24<br />total:   11635<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-25<br />total:   11289<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-26<br />total:   83926<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-27<br />total:   76497<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-28<br />total:   55988<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-02-29<br />total:   57279<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-01<br />total:   31726<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-02<br />total:   31128<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-03<br />total:   28655<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-04<br />total:   22900<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-05<br />total:   24800<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-06<br />total:   21856<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-07<br />total:   16899<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-08<br />total:   18412<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-09<br />total:   19228<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-10<br />total:   23860<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-11<br />total:   29482<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-12<br />total:   49923<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-13<br />total:   69129<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-14<br />total:   53836<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-15<br />total:   50656<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-16<br />total:   59160<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-17<br />total:  141905<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-18<br />total:  115005<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-19<br />total:  219709<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-20<br />total:  203371<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-21<br />total:  202804<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-22<br />total:  169642<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-23<br />total:  180785<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-24<br />total:   26936<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-25<br />total:   54693<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-26<br />total:  167338<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-27<br />total:  147446<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-28<br />total:  168839<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-29<br />total:  155479<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-30<br />total:   98846<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-03-31<br />total:   25707<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-01<br />total:   74441<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-02<br />total:  125216<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-03<br />total:  120761<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-04<br />total:  146098<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-05<br />total:  151660<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-06<br />total:  167633<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-07<br />total:  155792<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-08<br />total:   89523<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-09<br />total:   93256<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-10<br />total:  138201<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-11<br />total:  175082<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-12<br />total:  166244<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-13<br />total:  179038<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-14<br />total:  168711<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-15<br />total:  194211<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-16<br />total:  167053<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-17<br />total:  140877<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-18<br />total:   79003<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-19<br />total:  146475<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-20<br />total:  138260<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-21<br />total:   24248<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-22<br />total:  152828<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-23<br />total:  134863<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-24<br />total:   66058<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-25<br />total:   87802<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-26<br />total:   94317<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-27<br />total:  107805<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-28<br />total:   77371<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-29<br />total:  121894<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-04-30<br />total:  158004<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-01<br />total:  141348<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-02<br />total:  162440<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-03<br />total:  147388<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-04<br />total:  137565<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-05<br />total:   54483<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-06<br />total:  141548<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-07<br />total:  212695<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-08<br />total:  188997<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-09<br />total:  154086<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-10<br />total:  123810<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-11<br />total:  146597<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-12<br />total:  159855<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-13<br />total:  192929<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-14<br />total:  171075<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-15<br />total:  184765<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-16<br />total:  193674<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-17<br />total:  196018<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-18<br />total:  186088<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-19<br />total:  225858<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-20<br />total:  256029<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-21<br />total:  170902<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-22<br />total:  172534<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-23<br />total:  129008<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-24<br />total:  125916<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-25<br />total:  166015<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-26<br />total:  146346<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-27<br />total:  115698<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-28<br />total:  109631<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-29<br />total:  122369<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-30<br />total:  109935<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-05-31<br />total:  154096<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-01<br />total:  178275<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-02<br />total:  136513<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-03<br />total:  145343<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-04<br />total:  143974<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-05<br />total:  173089<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-06<br />total:  454923<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-07<br />total:  435533<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-08<br />total:  352885<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-09<br />total:  345522<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-10<br />total:  248535<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-11<br />total:  213567<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-12<br />total:  244133<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-13<br />total:  214722<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-14<br />total:  248902<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-15<br />total:  189041<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-16<br />total:  166219<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-17<br />total:  164883<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-18<br />total:  192537<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-19<br />total:  199658<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-20<br />total:  160878<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-21<br />total:  218238<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-22<br />total:  221475<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-23<br />total:  185292<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-24<br />total:  207022<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-25<br />total:  159678<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-26<br />total:  120036<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-27<br />total:  148601<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-28<br />total:  188133<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-29<br />total:  188622<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-06-30<br />total:  180292<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-01<br />total:  153349<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-02<br />total:  132349<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-03<br />total:  148418<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-04<br />total:  134560<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-05<br />total:  145302<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-06<br />total:  150112<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-08<br />total:  256141<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-09<br />total:  142362<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-10<br />total:  129843<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-11<br />total:  134641<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-12<br />total:  123943<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-13<br />total:  149416<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-14<br />total:  151401<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-15<br />total:  184884<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-16<br />total:  158049<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-17<br />total:  153384<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-18<br />total:  193770<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-19<br />total:  250875<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-20<br />total:  332248<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-21<br />total:  289177<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-22<br />total:  230968<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-23<br />total:  222979<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-24<br />total:  191264<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-25<br />total:  164013<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-26<br />total:  172581<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-27<br />total:  141143<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-28<br />total:  173683<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-29<br />total:  220772<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-30<br />total:  187738<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-07-31<br />total:  181318<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-01<br />total:  137355<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-02<br />total:  140887<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-03<br />total:  139058<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-04<br />total:  148667<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-05<br />total:  122411<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-06<br />total:  134655<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-07<br />total:  148718<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-08<br />total:  208467<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-09<br />total:  332384<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-10<br />total:  193997<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-11<br />total:  226112<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-12<br />total:  267358<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-13<br />total:  207530<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-14<br />total:  143105<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-15<br />total:  127186<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-16<br />total:  138402<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-17<br />total:  123989<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-18<br />total:  115085<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-19<br />total:  136565<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-20<br />total:  156404<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-21<br />total:  159747<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-22<br />total:  135788<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-23<br />total:  113105<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-24<br />total:  162084<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-25<br />total:  169096<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-26<br />total:  113761<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-27<br />total:  115832<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-28<br />total:  136278<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-29<br />total:  124671<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-30<br />total:  146517<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese","Date: 2020-08-31<br />total:  168936<br />TopLanguages: Portuguese<br />TopLanguages: Portuguese"],"type":"scatter","mode":"lines","line":{"width":3.77952755905512,"color":"rgba(0,176,246,1)","dash":"solid"},"hoveron":"points","name":"(Portuguese,1)","legendgroup":"(Portuguese,1)","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null},{"x":[18290,18291,18292,18293,18294,18295,18296,18297,18298,18299,18300,18301,18302,18303,18304,18305,18306,18307,18308,18309,18310,18311,18312,18313,18314,18315,18316,18317,18318,18319,18320,18321,18322,18323,18324,18325,18326,18327,18328,18329,18330,18331,18332,18333,18334,18335,18336,18337,18338,18339,18340,18341,18342,18343,18344,18345,18346,18347,18348,18349,18350,18351,18352,18353,18354,18355,18356,18357,18358,18359,18360,18361,18362,18363,18364,18365,18366,18367,18368,18369,18370,18371,18372,18373,18374,18375,18376,18377,18378,18379,18380,18381,18382,18383,18384,18385,18386,18387,18388,18389,18390,18391,18392,18393,18394,18395,18396,18397,18398,18399,18400,18401,18402,18403,18404,18405,18406,18407,18408,18409,18410,18411,18412,18413,18414,18415,18416,18417,18418,18419,18420,18421,18422,18423,18424,18425,18426,18427,18428,18429,18430,18431,18432,18433,18434,18435,18436,18437,18438,18439,18440,18441,18442,18443,18444,18445,18446,18447,18448,18449,18451,18452,18453,18454,18455,18456,18457,18458,18459,18460,18461,18462,18463,18464,18465,18466,18467,18468,18469,18470,18471,18472,18473,18474,18475,18476,18477,18478,18479,18480,18481,18482,18483,18484,18485,18486,18487,18488,18489,18490,18491,18492,18493,18494,18495,18496,18497,18498,18499,18500,18501,18502,18503,18504,18505],"y":[121070,107224,144889,140901,151468,167267,166134,143725,122645,111632,116478,107666,116926,149647,139155,142347,118363,84837,76304,93382,100329,92545,89270,92002,78962,16449,131517,212285,254760,162745,170447,152271,92560,86597,137591,195338,129779,136398,147000,137243,142043,204620,204619,186048,190495,213318,214312,209154,463943,284040,492497,511333,528821,503812,427202,116110,181885,475007,389065,460794,497302,295522,126148,294580,416681,432655,470242,467118,453441,481016,315446,297004,479054,486058,528598,500535,465492,474471,476794,446421,335054,439194,445138,117279,436919,377639,312218,402575,401775,381673,279575,271844,399911,353171,399777,397542,374604,217771,356347,394469,406436,361595,345272,378873,355839,396543,414631,411380,452549,453141,422179,412794,387370,397555,378979,425905,394690,414029,447067,459237,372751,377987,427675,367187,526381,421133,415684,453573,449468,675002,727642,788048,701765,734103,726067,696153,718650,647571,663631,656415,738677,695814,715433,717814,591128,726606,624461,585828,632708,512294,501769,521033,543363,574644,549762,486689,502457,490872,564420,571964,530868,566955,641475,577300,586158,657198,550745,584127,579239,587678,658700,656639,646904,693597,736942,725631,665904,617055,708533,681565,656259,657576,582231,610983,671887,624536,601668,620960,605944,653231,726432,593684,607111,693138,713214,740597,801758,773524,734261,780404,806295,667848,697341,660071,627694,694257,614329,687652,658434,668655,663643,611374,594552,620219,620768],"text":["Date: 2020-01-29<br />total:  121070<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-01-30<br />total:  107224<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-01-31<br />total:  144889<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-01<br />total:  140901<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-02<br />total:  151468<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-03<br />total:  167267<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-04<br />total:  166134<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-05<br />total:  143725<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-06<br />total:  122645<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-07<br />total:  111632<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-08<br />total:  116478<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-09<br />total:  107666<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-10<br />total:  116926<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-11<br />total:  149647<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-12<br />total:  139155<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-13<br />total:  142347<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-14<br />total:  118363<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-15<br />total:   84837<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-16<br />total:   76304<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-17<br />total:   93382<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-18<br />total:  100329<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-19<br />total:   92545<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-20<br />total:   89270<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-21<br />total:   92002<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-22<br />total:   78962<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-23<br />total:   16449<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-24<br />total:  131517<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-25<br />total:  212285<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-26<br />total:  254760<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-27<br />total:  162745<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-28<br />total:  170447<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-02-29<br />total:  152271<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-01<br />total:   92560<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-02<br />total:   86597<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-03<br />total:  137591<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-04<br />total:  195338<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-05<br />total:  129779<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-06<br />total:  136398<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-07<br />total:  147000<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-08<br />total:  137243<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-09<br />total:  142043<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-10<br />total:  204620<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-11<br />total:  204619<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-12<br />total:  186048<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-13<br />total:  190495<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-14<br />total:  213318<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-15<br />total:  214312<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-16<br />total:  209154<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-17<br />total:  463943<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-18<br />total:  284040<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-19<br />total:  492497<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-20<br />total:  511333<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-21<br />total:  528821<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-22<br />total:  503812<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-23<br />total:  427202<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-24<br />total:  116110<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-25<br />total:  181885<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-26<br />total:  475007<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-27<br />total:  389065<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-28<br />total:  460794<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-29<br />total:  497302<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-30<br />total:  295522<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-03-31<br />total:  126148<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-01<br />total:  294580<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-02<br />total:  416681<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-03<br />total:  432655<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-04<br />total:  470242<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-05<br />total:  467118<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-06<br />total:  453441<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-07<br />total:  481016<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-08<br />total:  315446<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-09<br />total:  297004<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-10<br />total:  479054<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-11<br />total:  486058<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-12<br />total:  528598<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-13<br />total:  500535<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-14<br />total:  465492<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-15<br />total:  474471<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-16<br />total:  476794<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-17<br />total:  446421<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-18<br />total:  335054<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-19<br />total:  439194<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-20<br />total:  445138<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-21<br />total:  117279<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-22<br />total:  436919<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-23<br />total:  377639<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-24<br />total:  312218<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-25<br />total:  402575<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-26<br />total:  401775<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-27<br />total:  381673<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-28<br />total:  279575<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-29<br />total:  271844<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-04-30<br />total:  399911<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-01<br />total:  353171<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-02<br />total:  399777<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-03<br />total:  397542<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-04<br />total:  374604<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-05<br />total:  217771<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-06<br />total:  356347<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-07<br />total:  394469<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-08<br />total:  406436<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-09<br />total:  361595<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-10<br />total:  345272<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-11<br />total:  378873<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-12<br />total:  355839<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-13<br />total:  396543<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-14<br />total:  414631<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-15<br />total:  411380<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-16<br />total:  452549<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-17<br />total:  453141<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-18<br />total:  422179<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-19<br />total:  412794<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-20<br />total:  387370<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-21<br />total:  397555<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-22<br />total:  378979<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-23<br />total:  425905<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-24<br />total:  394690<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-25<br />total:  414029<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-26<br />total:  447067<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-27<br />total:  459237<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-28<br />total:  372751<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-29<br />total:  377987<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-30<br />total:  427675<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-05-31<br />total:  367187<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-01<br />total:  526381<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-02<br />total:  421133<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-03<br />total:  415684<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-04<br />total:  453573<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-05<br />total:  449468<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-06<br />total:  675002<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-07<br />total:  727642<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-08<br />total:  788048<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-09<br />total:  701765<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-10<br />total:  734103<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-11<br />total:  726067<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-12<br />total:  696153<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-13<br />total:  718650<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-14<br />total:  647571<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-15<br />total:  663631<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-16<br />total:  656415<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-17<br />total:  738677<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-18<br />total:  695814<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-19<br />total:  715433<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-20<br />total:  717814<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-21<br />total:  591128<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-22<br />total:  726606<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-23<br />total:  624461<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-24<br />total:  585828<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-25<br />total:  632708<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-26<br />total:  512294<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-27<br />total:  501769<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-28<br />total:  521033<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-29<br />total:  543363<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-06-30<br />total:  574644<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-01<br />total:  549762<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-02<br />total:  486689<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-03<br />total:  502457<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-04<br />total:  490872<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-05<br />total:  564420<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-06<br />total:  571964<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-08<br />total:  530868<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-09<br />total:  566955<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-10<br />total:  641475<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-11<br />total:  577300<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-12<br />total:  586158<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-13<br />total:  657198<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-14<br />total:  550745<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-15<br />total:  584127<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-16<br />total:  579239<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-17<br />total:  587678<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-18<br />total:  658700<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-19<br />total:  656639<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-20<br />total:  646904<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-21<br />total:  693597<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-22<br />total:  736942<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-23<br />total:  725631<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-24<br />total:  665904<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-25<br />total:  617055<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-26<br />total:  708533<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-27<br />total:  681565<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-28<br />total:  656259<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-29<br />total:  657576<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-30<br />total:  582231<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-07-31<br />total:  610983<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-01<br />total:  671887<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-02<br />total:  624536<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-03<br />total:  601668<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-04<br />total:  620960<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-05<br />total:  605944<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-06<br />total:  653231<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-07<br />total:  726432<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-08<br />total:  593684<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-09<br />total:  607111<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-10<br />total:  693138<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-11<br />total:  713214<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-12<br />total:  740597<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-13<br />total:  801758<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-14<br />total:  773524<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-15<br />total:  734261<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-16<br />total:  780404<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-17<br />total:  806295<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-18<br />total:  667848<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-19<br />total:  697341<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-20<br />total:  660071<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-21<br />total:  627694<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-22<br />total:  694257<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-23<br />total:  614329<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-24<br />total:  687652<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-25<br />total:  658434<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-26<br />total:  668655<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-27<br />total:  663643<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-28<br />total:  611374<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-29<br />total:  594552<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-30<br />total:  620219<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian","Date: 2020-08-31<br />total:  620768<br />TopLanguages: Spanish; Castilian<br />TopLanguages: Spanish; Castilian"],"type":"scatter","mode":"lines","line":{"width":3.77952755905512,"color":"rgba(231,107,243,1)","dash":"solid"},"hoveron":"points","name":"(Spanish; Castilian,1)","legendgroup":"(Spanish; Castilian,1)","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null}],"layout":{"margin":{"t":44.8252386882524,"r":7.30593607305936,"b":45.7617268576173,"l":62.7646326276463},"plot_bgcolor":"rgba(255,255,255,1)","paper_bgcolor":"rgba(255,255,255,1)","font":{"color":"rgba(0,0,0,1)","family":"","size":14.6118721461187},"title":{"text":"<b> Top 5 Languages Tweets per day <\/b>","font":{"color":"rgba(0,0,0,1)","family":"","size":18.5969281859693},"x":0,"xref":"paper"},"xaxis":{"domain":[0,1],"automargin":true,"type":"linear","autorange":false,"range":[18271.9,18516.1],"tickmode":"array","ticktext":["Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"],"tickvals":[18293,18322,18353,18383,18414,18444,18475,18506],"categoryorder":"array","categoryarray":["Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"],"nticks":null,"ticks":"outside","tickcolor":"rgba(51,51,51,1)","ticklen":3.65296803652968,"tickwidth":0.66417600664176,"showticklabels":true,"tickfont":{"color":"rgba(0,0,0,1)","family":"","size":13.2835201328352},"tickangle":-0,"showline":false,"linecolor":null,"linewidth":0,"showgrid":true,"gridcolor":"rgba(235,235,235,1)","gridwidth":0.66417600664176,"zeroline":false,"anchor":"y","title":{"text":"<b> Date <\/b>","font":{"color":"rgba(0,0,0,1)","family":"","size":18.5969281859693}},"hoverformat":".2f"},"yaxis":{"domain":[0,1],"automargin":true,"type":"linear","autorange":false,"range":[-196131.7,4190507.7],"tickmode":"array","ticktext":["0e+00","1e+06","2e+06","3e+06","4e+06"],"tickvals":[0,1000000,2000000,3000000,4000000],"categoryorder":"array","categoryarray":["0e+00","1e+06","2e+06","3e+06","4e+06"],"nticks":null,"ticks":"outside","tickcolor":"rgba(51,51,51,1)","ticklen":3.65296803652968,"tickwidth":0.66417600664176,"showticklabels":true,"tickfont":{"color":"rgba(0,0,0,1)","family":"","size":13.2835201328352},"tickangle":-0,"showline":false,"linecolor":null,"linewidth":0,"showgrid":true,"gridcolor":"rgba(235,235,235,1)","gridwidth":0.66417600664176,"zeroline":false,"anchor":"x","title":{"text":"<b> Number of Tweets <\/b>","font":{"color":"rgba(0,0,0,1)","family":"","size":18.5969281859693}},"hoverformat":".2f"},"shapes":[{"type":"rect","fillcolor":"transparent","line":{"color":"rgba(51,51,51,1)","width":0.66417600664176,"linetype":"solid"},"yref":"paper","xref":"paper","x0":0,"x1":1,"y0":0,"y1":1}],"showlegend":false,"legend":{"bgcolor":"rgba(255,255,255,1)","bordercolor":"transparent","borderwidth":1.88976377952756,"font":{"color":"rgba(0,0,0,1)","family":"","size":13.2835201328352},"y":0.917322834645669},"annotations":[],"hovermode":"closest","barmode":"relative"},"config":{"doubleClick":"reset","showSendToCloud":false},"source":"A","attrs":{"3338327239cd":{"x":{},"y":{},"colour":{},"type":"scatter"}},"cur_data":"3338327239cd","visdat":{"3338327239cd":["function (y) ","x"]},".hideLegend":true,"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.2,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>

<!--/html_preserve-->

### Sentiment Analaysis

Similarly, the sentiment of all the English tweets was estimated using a
state-or-the-art Twitter Sentiment algorithm
[BB\_twtr](https://arxiv.org/abs/1704.06125) [Code
here](https://github.com/leelaylay/TweetSemEval) .

<!--html_preserve-->

<div id="htmlwidget-7e18294047af79b1e20a" class="plotly html-widget" style="width:672px;height:480px;">

</div>

<script type="application/json" data-for="htmlwidget-7e18294047af79b1e20a">{"x":{"data":[{"x":[18283,18284,18285,18286,18287,18288,18289,18290,18291,18292,18293,18294,18295,18296,18297,18298,18299,18300,18301,18302,18303,18304,18305,18306,18307,18308,18309,18310,18311,18312,18313,18314,18315,18316,18317,18318,18319,18320,18321,18322,18323,18324,18325,18326,18327,18328,18329,18330,18331,18332,18333,18334,18335,18336,18337,18338,18339,18340,18341,18342,18343,18344,18345,18346,18347,18348,18349,18350,18351,18352,18353,18354,18355,18356,18357,18358,18359,18360,18361,18362,18363,18364,18365,18366,18367,18368,18369,18370,18371,18372,18373,18374,18375,18376,18377,18378,18379,18380,18381,18382,18383,18384,18385,18386,18387,18388,18389,18390,18391,18392,18393,18394,18395,18396,18397,18398,18399,18400,18401,18402,18403,18404,18405,18406,18407,18408,18409,18410,18411,18412,18413,18414,18415,18416,18417,18418,18419,18420,18421,18422,18423,18424,18425,18426,18427,18428,18429,18430,18431,18432,18433,18434,18435,18436,18437,18438,18439,18440,18441,18442,18443,18444,18445,18446,18447,18448,18449,18451,18452,18453,18454,18455,18456,18457,18458,18459,18460,18461,18462,18463,18464,18465,18466,18467,18468,18469,18470,18471,18472,18473,18474,18475,18476,18477,18478,18479,18480,18481,18482,18483,18484,18485,18486,18487,18488,18489,18490,18491,18492,18493,18494,18495,18496,18497,18498,18499,18500,18501,18502,18503,18504,18505],"y":[14493,99275,233430,376001,489539,451737,323282,611369,695855,641326,232297,240679,213258,247566,208970,250610,229263,227907,237402,252091,265597,265132,279354,237906,195450,183989,221875,255794,240426,226431,247143,201977,37344,179492,225189,246548,323744,683442,1552649,1079866,257533,1150953,1170227,321755,357364,394389,364863,357599,341765,327084,322441,309781,310743,280025,254148,576972,420011,754476,735432,657147,761859,792262,230022,288356,770442,636935,729384,770852,552804,255609,533857,773537,705078,789978,784071,792203,771585,567745,503204,810174,815616,793817,766401,777905,840507,790607,766758,599945,843780,824903,217165,788259,800717,843035,1080125,1127152,1075196,808979,618533,834683,762468,843162,895659,978404,518947,1048751,1211408,1066409,961539,994443,1149332,1140513,1230672,1173714,1155303,1069624,1119193,1127237,1112594,1129791,1085796,963732,988809,1078468,986311,943470,984918,1122022,1241142,1264988,1320520,1129221,993241,1052427,1045597,776734,1299103,1387285,1176269,1204569,1336280,1321069,1363457,1402478,1450128,1619914,1437913,1443361,1312861,1220364,1246485,1460745,1444967,1580404,1501190,1716072,1858199,1628246,1628051,1635983,1842600,1799952,1697218,1682233,1636422,1653266,1808494,1641766,1555942,1612422,1470493,1285886,1841312,1742244,1996229,1977195,1923943,1621635,1682374,1530898,1555751,1484759,1490028,1418079,1404785,1417240,1460828,1705072,1536426,1695378,1552115,1366555,1485374,1434976,1614891,1309972,1476609,1425240,1352948,1526275,1605333,1476775,1225377,1333123,1310455,1209551,1247316,1225195,1340607,1278795,1356324,1460191,1423859,1634650,1483546,1497680,1525185,1520186,1599860,1266156,1370695,1501691],"text":["Date: 2020-01-22<br />Count:   14493<br />Sentiment: negative","Date: 2020-01-23<br />Count:   99275<br />Sentiment: negative","Date: 2020-01-24<br />Count:  233430<br />Sentiment: negative","Date: 2020-01-25<br />Count:  376001<br />Sentiment: negative","Date: 2020-01-26<br />Count:  489539<br />Sentiment: negative","Date: 2020-01-27<br />Count:  451737<br />Sentiment: negative","Date: 2020-01-28<br />Count:  323282<br />Sentiment: negative","Date: 2020-01-29<br />Count:  611369<br />Sentiment: negative","Date: 2020-01-30<br />Count:  695855<br />Sentiment: negative","Date: 2020-01-31<br />Count:  641326<br />Sentiment: negative","Date: 2020-02-01<br />Count:  232297<br />Sentiment: negative","Date: 2020-02-02<br />Count:  240679<br />Sentiment: negative","Date: 2020-02-03<br />Count:  213258<br />Sentiment: negative","Date: 2020-02-04<br />Count:  247566<br />Sentiment: negative","Date: 2020-02-05<br />Count:  208970<br />Sentiment: negative","Date: 2020-02-06<br />Count:  250610<br />Sentiment: negative","Date: 2020-02-07<br />Count:  229263<br />Sentiment: negative","Date: 2020-02-08<br />Count:  227907<br />Sentiment: negative","Date: 2020-02-09<br />Count:  237402<br />Sentiment: negative","Date: 2020-02-10<br />Count:  252091<br />Sentiment: negative","Date: 2020-02-11<br />Count:  265597<br />Sentiment: negative","Date: 2020-02-12<br />Count:  265132<br />Sentiment: negative","Date: 2020-02-13<br />Count:  279354<br />Sentiment: negative","Date: 2020-02-14<br />Count:  237906<br />Sentiment: negative","Date: 2020-02-15<br />Count:  195450<br />Sentiment: negative","Date: 2020-02-16<br />Count:  183989<br />Sentiment: negative","Date: 2020-02-17<br />Count:  221875<br />Sentiment: negative","Date: 2020-02-18<br />Count:  255794<br />Sentiment: negative","Date: 2020-02-19<br />Count:  240426<br />Sentiment: negative","Date: 2020-02-20<br />Count:  226431<br />Sentiment: negative","Date: 2020-02-21<br />Count:  247143<br />Sentiment: negative","Date: 2020-02-22<br />Count:  201977<br />Sentiment: negative","Date: 2020-02-23<br />Count:   37344<br />Sentiment: negative","Date: 2020-02-24<br />Count:  179492<br />Sentiment: negative","Date: 2020-02-25<br />Count:  225189<br />Sentiment: negative","Date: 2020-02-26<br />Count:  246548<br />Sentiment: negative","Date: 2020-02-27<br />Count:  323744<br />Sentiment: negative","Date: 2020-02-28<br />Count:  683442<br />Sentiment: negative","Date: 2020-02-29<br />Count: 1552649<br />Sentiment: negative","Date: 2020-03-01<br />Count: 1079866<br />Sentiment: negative","Date: 2020-03-02<br />Count:  257533<br />Sentiment: negative","Date: 2020-03-03<br />Count: 1150953<br />Sentiment: negative","Date: 2020-03-04<br />Count: 1170227<br />Sentiment: negative","Date: 2020-03-05<br />Count:  321755<br />Sentiment: negative","Date: 2020-03-06<br />Count:  357364<br />Sentiment: negative","Date: 2020-03-07<br />Count:  394389<br />Sentiment: negative","Date: 2020-03-08<br />Count:  364863<br />Sentiment: negative","Date: 2020-03-09<br />Count:  357599<br />Sentiment: negative","Date: 2020-03-10<br />Count:  341765<br />Sentiment: negative","Date: 2020-03-11<br />Count:  327084<br />Sentiment: negative","Date: 2020-03-12<br />Count:  322441<br />Sentiment: negative","Date: 2020-03-13<br />Count:  309781<br />Sentiment: negative","Date: 2020-03-14<br />Count:  310743<br />Sentiment: negative","Date: 2020-03-15<br />Count:  280025<br />Sentiment: negative","Date: 2020-03-16<br />Count:  254148<br />Sentiment: negative","Date: 2020-03-17<br />Count:  576972<br />Sentiment: negative","Date: 2020-03-18<br />Count:  420011<br />Sentiment: negative","Date: 2020-03-19<br />Count:  754476<br />Sentiment: negative","Date: 2020-03-20<br />Count:  735432<br />Sentiment: negative","Date: 2020-03-21<br />Count:  657147<br />Sentiment: negative","Date: 2020-03-22<br />Count:  761859<br />Sentiment: negative","Date: 2020-03-23<br />Count:  792262<br />Sentiment: negative","Date: 2020-03-24<br />Count:  230022<br />Sentiment: negative","Date: 2020-03-25<br />Count:  288356<br />Sentiment: negative","Date: 2020-03-26<br />Count:  770442<br />Sentiment: negative","Date: 2020-03-27<br />Count:  636935<br />Sentiment: negative","Date: 2020-03-28<br />Count:  729384<br />Sentiment: negative","Date: 2020-03-29<br />Count:  770852<br />Sentiment: negative","Date: 2020-03-30<br />Count:  552804<br />Sentiment: negative","Date: 2020-03-31<br />Count:  255609<br />Sentiment: negative","Date: 2020-04-01<br />Count:  533857<br />Sentiment: negative","Date: 2020-04-02<br />Count:  773537<br />Sentiment: negative","Date: 2020-04-03<br />Count:  705078<br />Sentiment: negative","Date: 2020-04-04<br />Count:  789978<br />Sentiment: negative","Date: 2020-04-05<br />Count:  784071<br />Sentiment: negative","Date: 2020-04-06<br />Count:  792203<br />Sentiment: negative","Date: 2020-04-07<br />Count:  771585<br />Sentiment: negative","Date: 2020-04-08<br />Count:  567745<br />Sentiment: negative","Date: 2020-04-09<br />Count:  503204<br />Sentiment: negative","Date: 2020-04-10<br />Count:  810174<br />Sentiment: negative","Date: 2020-04-11<br />Count:  815616<br />Sentiment: negative","Date: 2020-04-12<br />Count:  793817<br />Sentiment: negative","Date: 2020-04-13<br />Count:  766401<br />Sentiment: negative","Date: 2020-04-14<br />Count:  777905<br />Sentiment: negative","Date: 2020-04-15<br />Count:  840507<br />Sentiment: negative","Date: 2020-04-16<br />Count:  790607<br />Sentiment: negative","Date: 2020-04-17<br />Count:  766758<br />Sentiment: negative","Date: 2020-04-18<br />Count:  599945<br />Sentiment: negative","Date: 2020-04-19<br />Count:  843780<br />Sentiment: negative","Date: 2020-04-20<br />Count:  824903<br />Sentiment: negative","Date: 2020-04-21<br />Count:  217165<br />Sentiment: negative","Date: 2020-04-22<br />Count:  788259<br />Sentiment: negative","Date: 2020-04-23<br />Count:  800717<br />Sentiment: negative","Date: 2020-04-24<br />Count:  843035<br />Sentiment: negative","Date: 2020-04-25<br />Count: 1080125<br />Sentiment: negative","Date: 2020-04-26<br />Count: 1127152<br />Sentiment: negative","Date: 2020-04-27<br />Count: 1075196<br />Sentiment: negative","Date: 2020-04-28<br />Count:  808979<br />Sentiment: negative","Date: 2020-04-29<br />Count:  618533<br />Sentiment: negative","Date: 2020-04-30<br />Count:  834683<br />Sentiment: negative","Date: 2020-05-01<br />Count:  762468<br />Sentiment: negative","Date: 2020-05-02<br />Count:  843162<br />Sentiment: negative","Date: 2020-05-03<br />Count:  895659<br />Sentiment: negative","Date: 2020-05-04<br />Count:  978404<br />Sentiment: negative","Date: 2020-05-05<br />Count:  518947<br />Sentiment: negative","Date: 2020-05-06<br />Count: 1048751<br />Sentiment: negative","Date: 2020-05-07<br />Count: 1211408<br />Sentiment: negative","Date: 2020-05-08<br />Count: 1066409<br />Sentiment: negative","Date: 2020-05-09<br />Count:  961539<br />Sentiment: negative","Date: 2020-05-10<br />Count:  994443<br />Sentiment: negative","Date: 2020-05-11<br />Count: 1149332<br />Sentiment: negative","Date: 2020-05-12<br />Count: 1140513<br />Sentiment: negative","Date: 2020-05-13<br />Count: 1230672<br />Sentiment: negative","Date: 2020-05-14<br />Count: 1173714<br />Sentiment: negative","Date: 2020-05-15<br />Count: 1155303<br />Sentiment: negative","Date: 2020-05-16<br />Count: 1069624<br />Sentiment: negative","Date: 2020-05-17<br />Count: 1119193<br />Sentiment: negative","Date: 2020-05-18<br />Count: 1127237<br />Sentiment: negative","Date: 2020-05-19<br />Count: 1112594<br />Sentiment: negative","Date: 2020-05-20<br />Count: 1129791<br />Sentiment: negative","Date: 2020-05-21<br />Count: 1085796<br />Sentiment: negative","Date: 2020-05-22<br />Count:  963732<br />Sentiment: negative","Date: 2020-05-23<br />Count:  988809<br />Sentiment: negative","Date: 2020-05-24<br />Count: 1078468<br />Sentiment: negative","Date: 2020-05-25<br />Count:  986311<br />Sentiment: negative","Date: 2020-05-26<br />Count:  943470<br />Sentiment: negative","Date: 2020-05-27<br />Count:  984918<br />Sentiment: negative","Date: 2020-05-28<br />Count: 1122022<br />Sentiment: negative","Date: 2020-05-29<br />Count: 1241142<br />Sentiment: negative","Date: 2020-05-30<br />Count: 1264988<br />Sentiment: negative","Date: 2020-05-31<br />Count: 1320520<br />Sentiment: negative","Date: 2020-06-01<br />Count: 1129221<br />Sentiment: negative","Date: 2020-06-02<br />Count:  993241<br />Sentiment: negative","Date: 2020-06-03<br />Count: 1052427<br />Sentiment: negative","Date: 2020-06-04<br />Count: 1045597<br />Sentiment: negative","Date: 2020-06-05<br />Count:  776734<br />Sentiment: negative","Date: 2020-06-06<br />Count: 1299103<br />Sentiment: negative","Date: 2020-06-07<br />Count: 1387285<br />Sentiment: negative","Date: 2020-06-08<br />Count: 1176269<br />Sentiment: negative","Date: 2020-06-09<br />Count: 1204569<br />Sentiment: negative","Date: 2020-06-10<br />Count: 1336280<br />Sentiment: negative","Date: 2020-06-11<br />Count: 1321069<br />Sentiment: negative","Date: 2020-06-12<br />Count: 1363457<br />Sentiment: negative","Date: 2020-06-13<br />Count: 1402478<br />Sentiment: negative","Date: 2020-06-14<br />Count: 1450128<br />Sentiment: negative","Date: 2020-06-15<br />Count: 1619914<br />Sentiment: negative","Date: 2020-06-16<br />Count: 1437913<br />Sentiment: negative","Date: 2020-06-17<br />Count: 1443361<br />Sentiment: negative","Date: 2020-06-18<br />Count: 1312861<br />Sentiment: negative","Date: 2020-06-19<br />Count: 1220364<br />Sentiment: negative","Date: 2020-06-20<br />Count: 1246485<br />Sentiment: negative","Date: 2020-06-21<br />Count: 1460745<br />Sentiment: negative","Date: 2020-06-22<br />Count: 1444967<br />Sentiment: negative","Date: 2020-06-23<br />Count: 1580404<br />Sentiment: negative","Date: 2020-06-24<br />Count: 1501190<br />Sentiment: negative","Date: 2020-06-25<br />Count: 1716072<br />Sentiment: negative","Date: 2020-06-26<br />Count: 1858199<br />Sentiment: negative","Date: 2020-06-27<br />Count: 1628246<br />Sentiment: negative","Date: 2020-06-28<br />Count: 1628051<br />Sentiment: negative","Date: 2020-06-29<br />Count: 1635983<br />Sentiment: negative","Date: 2020-06-30<br />Count: 1842600<br />Sentiment: negative","Date: 2020-07-01<br />Count: 1799952<br />Sentiment: negative","Date: 2020-07-02<br />Count: 1697218<br />Sentiment: negative","Date: 2020-07-03<br />Count: 1682233<br />Sentiment: negative","Date: 2020-07-04<br />Count: 1636422<br />Sentiment: negative","Date: 2020-07-05<br />Count: 1653266<br />Sentiment: negative","Date: 2020-07-06<br />Count: 1808494<br />Sentiment: negative","Date: 2020-07-08<br />Count: 1641766<br />Sentiment: negative","Date: 2020-07-09<br />Count: 1555942<br />Sentiment: negative","Date: 2020-07-10<br />Count: 1612422<br />Sentiment: negative","Date: 2020-07-11<br />Count: 1470493<br />Sentiment: negative","Date: 2020-07-12<br />Count: 1285886<br />Sentiment: negative","Date: 2020-07-13<br />Count: 1841312<br />Sentiment: negative","Date: 2020-07-14<br />Count: 1742244<br />Sentiment: negative","Date: 2020-07-15<br />Count: 1996229<br />Sentiment: negative","Date: 2020-07-16<br />Count: 1977195<br />Sentiment: negative","Date: 2020-07-17<br />Count: 1923943<br />Sentiment: negative","Date: 2020-07-18<br />Count: 1621635<br />Sentiment: negative","Date: 2020-07-19<br />Count: 1682374<br />Sentiment: negative","Date: 2020-07-20<br />Count: 1530898<br />Sentiment: negative","Date: 2020-07-21<br />Count: 1555751<br />Sentiment: negative","Date: 2020-07-22<br />Count: 1484759<br />Sentiment: negative","Date: 2020-07-23<br />Count: 1490028<br />Sentiment: negative","Date: 2020-07-24<br />Count: 1418079<br />Sentiment: negative","Date: 2020-07-25<br />Count: 1404785<br />Sentiment: negative","Date: 2020-07-26<br />Count: 1417240<br />Sentiment: negative","Date: 2020-07-27<br />Count: 1460828<br />Sentiment: negative","Date: 2020-07-28<br />Count: 1705072<br />Sentiment: negative","Date: 2020-07-29<br />Count: 1536426<br />Sentiment: negative","Date: 2020-07-30<br />Count: 1695378<br />Sentiment: negative","Date: 2020-07-31<br />Count: 1552115<br />Sentiment: negative","Date: 2020-08-01<br />Count: 1366555<br />Sentiment: negative","Date: 2020-08-02<br />Count: 1485374<br />Sentiment: negative","Date: 2020-08-03<br />Count: 1434976<br />Sentiment: negative","Date: 2020-08-04<br />Count: 1614891<br />Sentiment: negative","Date: 2020-08-05<br />Count: 1309972<br />Sentiment: negative","Date: 2020-08-06<br />Count: 1476609<br />Sentiment: negative","Date: 2020-08-07<br />Count: 1425240<br />Sentiment: negative","Date: 2020-08-08<br />Count: 1352948<br />Sentiment: negative","Date: 2020-08-09<br />Count: 1526275<br />Sentiment: negative","Date: 2020-08-10<br />Count: 1605333<br />Sentiment: negative","Date: 2020-08-11<br />Count: 1476775<br />Sentiment: negative","Date: 2020-08-12<br />Count: 1225377<br />Sentiment: negative","Date: 2020-08-13<br />Count: 1333123<br />Sentiment: negative","Date: 2020-08-14<br />Count: 1310455<br />Sentiment: negative","Date: 2020-08-15<br />Count: 1209551<br />Sentiment: negative","Date: 2020-08-16<br />Count: 1247316<br />Sentiment: negative","Date: 2020-08-17<br />Count: 1225195<br />Sentiment: negative","Date: 2020-08-18<br />Count: 1340607<br />Sentiment: negative","Date: 2020-08-19<br />Count: 1278795<br />Sentiment: negative","Date: 2020-08-20<br />Count: 1356324<br />Sentiment: negative","Date: 2020-08-21<br />Count: 1460191<br />Sentiment: negative","Date: 2020-08-22<br />Count: 1423859<br />Sentiment: negative","Date: 2020-08-23<br />Count: 1634650<br />Sentiment: negative","Date: 2020-08-24<br />Count: 1483546<br />Sentiment: negative","Date: 2020-08-25<br />Count: 1497680<br />Sentiment: negative","Date: 2020-08-26<br />Count: 1525185<br />Sentiment: negative","Date: 2020-08-27<br />Count: 1520186<br />Sentiment: negative","Date: 2020-08-28<br />Count: 1599860<br />Sentiment: negative","Date: 2020-08-29<br />Count: 1266156<br />Sentiment: negative","Date: 2020-08-30<br />Count: 1370695<br />Sentiment: negative","Date: 2020-08-31<br />Count: 1501691<br />Sentiment: negative"],"type":"scatter","mode":"lines","line":{"width":3.77952755905512,"color":"rgba(248,118,109,1)","dash":"solid"},"hoveron":"points","name":"(negative,1)","legendgroup":"(negative,1)","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null},{"x":[18283,18284,18285,18286,18287,18288,18289,18290,18291,18292,18293,18294,18295,18296,18297,18298,18299,18300,18301,18302,18303,18304,18305,18306,18307,18308,18309,18310,18311,18312,18313,18314,18315,18316,18317,18318,18319,18320,18321,18322,18323,18324,18325,18326,18327,18328,18329,18330,18331,18332,18333,18334,18335,18336,18337,18338,18339,18340,18341,18342,18343,18344,18345,18346,18347,18348,18349,18350,18351,18352,18353,18354,18355,18356,18357,18358,18359,18360,18361,18362,18363,18364,18365,18366,18367,18368,18369,18370,18371,18372,18373,18374,18375,18376,18377,18378,18379,18380,18381,18382,18383,18384,18385,18386,18387,18388,18389,18390,18391,18392,18393,18394,18395,18396,18397,18398,18399,18400,18401,18402,18403,18404,18405,18406,18407,18408,18409,18410,18411,18412,18413,18414,18415,18416,18417,18418,18419,18420,18421,18422,18423,18424,18425,18426,18427,18428,18429,18430,18431,18432,18433,18434,18435,18436,18437,18438,18439,18440,18441,18442,18443,18444,18445,18446,18447,18448,18449,18451,18452,18453,18454,18455,18456,18457,18458,18459,18460,18461,18462,18463,18464,18465,18466,18467,18468,18469,18470,18471,18472,18473,18474,18475,18476,18477,18478,18479,18480,18481,18482,18483,18484,18485,18486,18487,18488,18489,18490,18491,18492,18493,18494,18495,18496,18497,18498,18499,18500,18501,18502,18503,18504,18505],"y":[20061,97048,305404,445823,616673,394150,404091,557347,777769,672792,222222,237507,241663,271905,240624,255327,257809,265138,236690,288628,287552,247959,293838,296307,224167,274185,270014,266731,228009,246110,253786,207869,35596,208871,229143,249014,308442,723081,1302247,1030951,249753,1093097,1252895,349877,345400,319390,323381,341233,331617,345490,354053,322264,312765,302435,310187,736659,428722,734128,781173,693306,777304,802144,261954,356055,846946,742582,822024,800932,566267,279390,543958,774073,762103,762751,770033,810017,884632,596101,541988,808598,714110,674813,781281,818574,797865,827298,805633,717553,798478,828183,244061,807628,897275,1042233,1111303,1053340,1144061,842917,633801,902590,933330,889655,924878,974167,537830,989347,1136458,1049025,1061652,1101411,1274432,1193348,1254835,1204684,1183881,1042680,1030086,1180272,1127077,1073284,1101681,1031279,957617,878271,900565,898891,848085,862335,825965,694736,718878,738845,825337,735290,733583,565347,1113715,998665,1120393,1244284,1296358,1405301,1336712,1200707,1068296,1328774,1437420,1421201,1395896,1556689,1432476,1160605,1360929,1522507,1630577,1559078,1601400,1499337,1487961,1544968,1618341,1572422,1583988,1569324,1416034,1428911,1624526,1691603,1611279,1362093,1328274,1241469,1764618,1691137,1697182,1650048,1649018,1529013,1475774,1420748,1519707,1572444,1450689,1411837,1475931,1307287,1535958,1713376,1711198,1585219,1590447,1365094,1485085,1385445,1462115,1323542,1368328,1401477,1134827,1298335,1495852,1501225,1217303,1367758,1370960,1171076,1119212,1283598,1295826,1256350,1294276,1460487,1332624,1459908,1440385,1481534,1518376,1443471,1443447,1131199,1206342,1295163],"text":["Date: 2020-01-22<br />Count:   20061<br />Sentiment: neutral","Date: 2020-01-23<br />Count:   97048<br />Sentiment: neutral","Date: 2020-01-24<br />Count:  305404<br />Sentiment: neutral","Date: 2020-01-25<br />Count:  445823<br />Sentiment: neutral","Date: 2020-01-26<br />Count:  616673<br />Sentiment: neutral","Date: 2020-01-27<br />Count:  394150<br />Sentiment: neutral","Date: 2020-01-28<br />Count:  404091<br />Sentiment: neutral","Date: 2020-01-29<br />Count:  557347<br />Sentiment: neutral","Date: 2020-01-30<br />Count:  777769<br />Sentiment: neutral","Date: 2020-01-31<br />Count:  672792<br />Sentiment: neutral","Date: 2020-02-01<br />Count:  222222<br />Sentiment: neutral","Date: 2020-02-02<br />Count:  237507<br />Sentiment: neutral","Date: 2020-02-03<br />Count:  241663<br />Sentiment: neutral","Date: 2020-02-04<br />Count:  271905<br />Sentiment: neutral","Date: 2020-02-05<br />Count:  240624<br />Sentiment: neutral","Date: 2020-02-06<br />Count:  255327<br />Sentiment: neutral","Date: 2020-02-07<br />Count:  257809<br />Sentiment: neutral","Date: 2020-02-08<br />Count:  265138<br />Sentiment: neutral","Date: 2020-02-09<br />Count:  236690<br />Sentiment: neutral","Date: 2020-02-10<br />Count:  288628<br />Sentiment: neutral","Date: 2020-02-11<br />Count:  287552<br />Sentiment: neutral","Date: 2020-02-12<br />Count:  247959<br />Sentiment: neutral","Date: 2020-02-13<br />Count:  293838<br />Sentiment: neutral","Date: 2020-02-14<br />Count:  296307<br />Sentiment: neutral","Date: 2020-02-15<br />Count:  224167<br />Sentiment: neutral","Date: 2020-02-16<br />Count:  274185<br />Sentiment: neutral","Date: 2020-02-17<br />Count:  270014<br />Sentiment: neutral","Date: 2020-02-18<br />Count:  266731<br />Sentiment: neutral","Date: 2020-02-19<br />Count:  228009<br />Sentiment: neutral","Date: 2020-02-20<br />Count:  246110<br />Sentiment: neutral","Date: 2020-02-21<br />Count:  253786<br />Sentiment: neutral","Date: 2020-02-22<br />Count:  207869<br />Sentiment: neutral","Date: 2020-02-23<br />Count:   35596<br />Sentiment: neutral","Date: 2020-02-24<br />Count:  208871<br />Sentiment: neutral","Date: 2020-02-25<br />Count:  229143<br />Sentiment: neutral","Date: 2020-02-26<br />Count:  249014<br />Sentiment: neutral","Date: 2020-02-27<br />Count:  308442<br />Sentiment: neutral","Date: 2020-02-28<br />Count:  723081<br />Sentiment: neutral","Date: 2020-02-29<br />Count: 1302247<br />Sentiment: neutral","Date: 2020-03-01<br />Count: 1030951<br />Sentiment: neutral","Date: 2020-03-02<br />Count:  249753<br />Sentiment: neutral","Date: 2020-03-03<br />Count: 1093097<br />Sentiment: neutral","Date: 2020-03-04<br />Count: 1252895<br />Sentiment: neutral","Date: 2020-03-05<br />Count:  349877<br />Sentiment: neutral","Date: 2020-03-06<br />Count:  345400<br />Sentiment: neutral","Date: 2020-03-07<br />Count:  319390<br />Sentiment: neutral","Date: 2020-03-08<br />Count:  323381<br />Sentiment: neutral","Date: 2020-03-09<br />Count:  341233<br />Sentiment: neutral","Date: 2020-03-10<br />Count:  331617<br />Sentiment: neutral","Date: 2020-03-11<br />Count:  345490<br />Sentiment: neutral","Date: 2020-03-12<br />Count:  354053<br />Sentiment: neutral","Date: 2020-03-13<br />Count:  322264<br />Sentiment: neutral","Date: 2020-03-14<br />Count:  312765<br />Sentiment: neutral","Date: 2020-03-15<br />Count:  302435<br />Sentiment: neutral","Date: 2020-03-16<br />Count:  310187<br />Sentiment: neutral","Date: 2020-03-17<br />Count:  736659<br />Sentiment: neutral","Date: 2020-03-18<br />Count:  428722<br />Sentiment: neutral","Date: 2020-03-19<br />Count:  734128<br />Sentiment: neutral","Date: 2020-03-20<br />Count:  781173<br />Sentiment: neutral","Date: 2020-03-21<br />Count:  693306<br />Sentiment: neutral","Date: 2020-03-22<br />Count:  777304<br />Sentiment: neutral","Date: 2020-03-23<br />Count:  802144<br />Sentiment: neutral","Date: 2020-03-24<br />Count:  261954<br />Sentiment: neutral","Date: 2020-03-25<br />Count:  356055<br />Sentiment: neutral","Date: 2020-03-26<br />Count:  846946<br />Sentiment: neutral","Date: 2020-03-27<br />Count:  742582<br />Sentiment: neutral","Date: 2020-03-28<br />Count:  822024<br />Sentiment: neutral","Date: 2020-03-29<br />Count:  800932<br />Sentiment: neutral","Date: 2020-03-30<br />Count:  566267<br />Sentiment: neutral","Date: 2020-03-31<br />Count:  279390<br />Sentiment: neutral","Date: 2020-04-01<br />Count:  543958<br />Sentiment: neutral","Date: 2020-04-02<br />Count:  774073<br />Sentiment: neutral","Date: 2020-04-03<br />Count:  762103<br />Sentiment: neutral","Date: 2020-04-04<br />Count:  762751<br />Sentiment: neutral","Date: 2020-04-05<br />Count:  770033<br />Sentiment: neutral","Date: 2020-04-06<br />Count:  810017<br />Sentiment: neutral","Date: 2020-04-07<br />Count:  884632<br />Sentiment: neutral","Date: 2020-04-08<br />Count:  596101<br />Sentiment: neutral","Date: 2020-04-09<br />Count:  541988<br />Sentiment: neutral","Date: 2020-04-10<br />Count:  808598<br />Sentiment: neutral","Date: 2020-04-11<br />Count:  714110<br />Sentiment: neutral","Date: 2020-04-12<br />Count:  674813<br />Sentiment: neutral","Date: 2020-04-13<br />Count:  781281<br />Sentiment: neutral","Date: 2020-04-14<br />Count:  818574<br />Sentiment: neutral","Date: 2020-04-15<br />Count:  797865<br />Sentiment: neutral","Date: 2020-04-16<br />Count:  827298<br />Sentiment: neutral","Date: 2020-04-17<br />Count:  805633<br />Sentiment: neutral","Date: 2020-04-18<br />Count:  717553<br />Sentiment: neutral","Date: 2020-04-19<br />Count:  798478<br />Sentiment: neutral","Date: 2020-04-20<br />Count:  828183<br />Sentiment: neutral","Date: 2020-04-21<br />Count:  244061<br />Sentiment: neutral","Date: 2020-04-22<br />Count:  807628<br />Sentiment: neutral","Date: 2020-04-23<br />Count:  897275<br />Sentiment: neutral","Date: 2020-04-24<br />Count: 1042233<br />Sentiment: neutral","Date: 2020-04-25<br />Count: 1111303<br />Sentiment: neutral","Date: 2020-04-26<br />Count: 1053340<br />Sentiment: neutral","Date: 2020-04-27<br />Count: 1144061<br />Sentiment: neutral","Date: 2020-04-28<br />Count:  842917<br />Sentiment: neutral","Date: 2020-04-29<br />Count:  633801<br />Sentiment: neutral","Date: 2020-04-30<br />Count:  902590<br />Sentiment: neutral","Date: 2020-05-01<br />Count:  933330<br />Sentiment: neutral","Date: 2020-05-02<br />Count:  889655<br />Sentiment: neutral","Date: 2020-05-03<br />Count:  924878<br />Sentiment: neutral","Date: 2020-05-04<br />Count:  974167<br />Sentiment: neutral","Date: 2020-05-05<br />Count:  537830<br />Sentiment: neutral","Date: 2020-05-06<br />Count:  989347<br />Sentiment: neutral","Date: 2020-05-07<br />Count: 1136458<br />Sentiment: neutral","Date: 2020-05-08<br />Count: 1049025<br />Sentiment: neutral","Date: 2020-05-09<br />Count: 1061652<br />Sentiment: neutral","Date: 2020-05-10<br />Count: 1101411<br />Sentiment: neutral","Date: 2020-05-11<br />Count: 1274432<br />Sentiment: neutral","Date: 2020-05-12<br />Count: 1193348<br />Sentiment: neutral","Date: 2020-05-13<br />Count: 1254835<br />Sentiment: neutral","Date: 2020-05-14<br />Count: 1204684<br />Sentiment: neutral","Date: 2020-05-15<br />Count: 1183881<br />Sentiment: neutral","Date: 2020-05-16<br />Count: 1042680<br />Sentiment: neutral","Date: 2020-05-17<br />Count: 1030086<br />Sentiment: neutral","Date: 2020-05-18<br />Count: 1180272<br />Sentiment: neutral","Date: 2020-05-19<br />Count: 1127077<br />Sentiment: neutral","Date: 2020-05-20<br />Count: 1073284<br />Sentiment: neutral","Date: 2020-05-21<br />Count: 1101681<br />Sentiment: neutral","Date: 2020-05-22<br />Count: 1031279<br />Sentiment: neutral","Date: 2020-05-23<br />Count:  957617<br />Sentiment: neutral","Date: 2020-05-24<br />Count:  878271<br />Sentiment: neutral","Date: 2020-05-25<br />Count:  900565<br />Sentiment: neutral","Date: 2020-05-26<br />Count:  898891<br />Sentiment: neutral","Date: 2020-05-27<br />Count:  848085<br />Sentiment: neutral","Date: 2020-05-28<br />Count:  862335<br />Sentiment: neutral","Date: 2020-05-29<br />Count:  825965<br />Sentiment: neutral","Date: 2020-05-30<br />Count:  694736<br />Sentiment: neutral","Date: 2020-05-31<br />Count:  718878<br />Sentiment: neutral","Date: 2020-06-01<br />Count:  738845<br />Sentiment: neutral","Date: 2020-06-02<br />Count:  825337<br />Sentiment: neutral","Date: 2020-06-03<br />Count:  735290<br />Sentiment: neutral","Date: 2020-06-04<br />Count:  733583<br />Sentiment: neutral","Date: 2020-06-05<br />Count:  565347<br />Sentiment: neutral","Date: 2020-06-06<br />Count: 1113715<br />Sentiment: neutral","Date: 2020-06-07<br />Count:  998665<br />Sentiment: neutral","Date: 2020-06-08<br />Count: 1120393<br />Sentiment: neutral","Date: 2020-06-09<br />Count: 1244284<br />Sentiment: neutral","Date: 2020-06-10<br />Count: 1296358<br />Sentiment: neutral","Date: 2020-06-11<br />Count: 1405301<br />Sentiment: neutral","Date: 2020-06-12<br />Count: 1336712<br />Sentiment: neutral","Date: 2020-06-13<br />Count: 1200707<br />Sentiment: neutral","Date: 2020-06-14<br />Count: 1068296<br />Sentiment: neutral","Date: 2020-06-15<br />Count: 1328774<br />Sentiment: neutral","Date: 2020-06-16<br />Count: 1437420<br />Sentiment: neutral","Date: 2020-06-17<br />Count: 1421201<br />Sentiment: neutral","Date: 2020-06-18<br />Count: 1395896<br />Sentiment: neutral","Date: 2020-06-19<br />Count: 1556689<br />Sentiment: neutral","Date: 2020-06-20<br />Count: 1432476<br />Sentiment: neutral","Date: 2020-06-21<br />Count: 1160605<br />Sentiment: neutral","Date: 2020-06-22<br />Count: 1360929<br />Sentiment: neutral","Date: 2020-06-23<br />Count: 1522507<br />Sentiment: neutral","Date: 2020-06-24<br />Count: 1630577<br />Sentiment: neutral","Date: 2020-06-25<br />Count: 1559078<br />Sentiment: neutral","Date: 2020-06-26<br />Count: 1601400<br />Sentiment: neutral","Date: 2020-06-27<br />Count: 1499337<br />Sentiment: neutral","Date: 2020-06-28<br />Count: 1487961<br />Sentiment: neutral","Date: 2020-06-29<br />Count: 1544968<br />Sentiment: neutral","Date: 2020-06-30<br />Count: 1618341<br />Sentiment: neutral","Date: 2020-07-01<br />Count: 1572422<br />Sentiment: neutral","Date: 2020-07-02<br />Count: 1583988<br />Sentiment: neutral","Date: 2020-07-03<br />Count: 1569324<br />Sentiment: neutral","Date: 2020-07-04<br />Count: 1416034<br />Sentiment: neutral","Date: 2020-07-05<br />Count: 1428911<br />Sentiment: neutral","Date: 2020-07-06<br />Count: 1624526<br />Sentiment: neutral","Date: 2020-07-08<br />Count: 1691603<br />Sentiment: neutral","Date: 2020-07-09<br />Count: 1611279<br />Sentiment: neutral","Date: 2020-07-10<br />Count: 1362093<br />Sentiment: neutral","Date: 2020-07-11<br />Count: 1328274<br />Sentiment: neutral","Date: 2020-07-12<br />Count: 1241469<br />Sentiment: neutral","Date: 2020-07-13<br />Count: 1764618<br />Sentiment: neutral","Date: 2020-07-14<br />Count: 1691137<br />Sentiment: neutral","Date: 2020-07-15<br />Count: 1697182<br />Sentiment: neutral","Date: 2020-07-16<br />Count: 1650048<br />Sentiment: neutral","Date: 2020-07-17<br />Count: 1649018<br />Sentiment: neutral","Date: 2020-07-18<br />Count: 1529013<br />Sentiment: neutral","Date: 2020-07-19<br />Count: 1475774<br />Sentiment: neutral","Date: 2020-07-20<br />Count: 1420748<br />Sentiment: neutral","Date: 2020-07-21<br />Count: 1519707<br />Sentiment: neutral","Date: 2020-07-22<br />Count: 1572444<br />Sentiment: neutral","Date: 2020-07-23<br />Count: 1450689<br />Sentiment: neutral","Date: 2020-07-24<br />Count: 1411837<br />Sentiment: neutral","Date: 2020-07-25<br />Count: 1475931<br />Sentiment: neutral","Date: 2020-07-26<br />Count: 1307287<br />Sentiment: neutral","Date: 2020-07-27<br />Count: 1535958<br />Sentiment: neutral","Date: 2020-07-28<br />Count: 1713376<br />Sentiment: neutral","Date: 2020-07-29<br />Count: 1711198<br />Sentiment: neutral","Date: 2020-07-30<br />Count: 1585219<br />Sentiment: neutral","Date: 2020-07-31<br />Count: 1590447<br />Sentiment: neutral","Date: 2020-08-01<br />Count: 1365094<br />Sentiment: neutral","Date: 2020-08-02<br />Count: 1485085<br />Sentiment: neutral","Date: 2020-08-03<br />Count: 1385445<br />Sentiment: neutral","Date: 2020-08-04<br />Count: 1462115<br />Sentiment: neutral","Date: 2020-08-05<br />Count: 1323542<br />Sentiment: neutral","Date: 2020-08-06<br />Count: 1368328<br />Sentiment: neutral","Date: 2020-08-07<br />Count: 1401477<br />Sentiment: neutral","Date: 2020-08-08<br />Count: 1134827<br />Sentiment: neutral","Date: 2020-08-09<br />Count: 1298335<br />Sentiment: neutral","Date: 2020-08-10<br />Count: 1495852<br />Sentiment: neutral","Date: 2020-08-11<br />Count: 1501225<br />Sentiment: neutral","Date: 2020-08-12<br />Count: 1217303<br />Sentiment: neutral","Date: 2020-08-13<br />Count: 1367758<br />Sentiment: neutral","Date: 2020-08-14<br />Count: 1370960<br />Sentiment: neutral","Date: 2020-08-15<br />Count: 1171076<br />Sentiment: neutral","Date: 2020-08-16<br />Count: 1119212<br />Sentiment: neutral","Date: 2020-08-17<br />Count: 1283598<br />Sentiment: neutral","Date: 2020-08-18<br />Count: 1295826<br />Sentiment: neutral","Date: 2020-08-19<br />Count: 1256350<br />Sentiment: neutral","Date: 2020-08-20<br />Count: 1294276<br />Sentiment: neutral","Date: 2020-08-21<br />Count: 1460487<br />Sentiment: neutral","Date: 2020-08-22<br />Count: 1332624<br />Sentiment: neutral","Date: 2020-08-23<br />Count: 1459908<br />Sentiment: neutral","Date: 2020-08-24<br />Count: 1440385<br />Sentiment: neutral","Date: 2020-08-25<br />Count: 1481534<br />Sentiment: neutral","Date: 2020-08-26<br />Count: 1518376<br />Sentiment: neutral","Date: 2020-08-27<br />Count: 1443471<br />Sentiment: neutral","Date: 2020-08-28<br />Count: 1443447<br />Sentiment: neutral","Date: 2020-08-29<br />Count: 1131199<br />Sentiment: neutral","Date: 2020-08-30<br />Count: 1206342<br />Sentiment: neutral","Date: 2020-08-31<br />Count: 1295163<br />Sentiment: neutral"],"type":"scatter","mode":"lines","line":{"width":3.77952755905512,"color":"rgba(0,186,56,1)","dash":"solid"},"hoveron":"points","name":"(neutral,1)","legendgroup":"(neutral,1)","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null},{"x":[18283,18284,18285,18286,18287,18288,18289,18290,18291,18292,18293,18294,18295,18296,18297,18298,18299,18300,18301,18302,18303,18304,18305,18306,18307,18308,18309,18310,18311,18312,18313,18314,18315,18316,18317,18318,18319,18320,18321,18322,18323,18324,18325,18326,18327,18328,18329,18330,18331,18332,18333,18334,18335,18336,18337,18338,18339,18340,18341,18342,18343,18344,18345,18346,18347,18348,18349,18350,18351,18352,18353,18354,18355,18356,18357,18358,18359,18360,18361,18362,18363,18364,18365,18366,18367,18368,18369,18370,18371,18372,18373,18374,18375,18376,18377,18378,18379,18380,18381,18382,18383,18384,18385,18386,18387,18388,18389,18390,18391,18392,18393,18394,18395,18396,18397,18398,18399,18400,18401,18402,18403,18404,18405,18406,18407,18408,18409,18410,18411,18412,18413,18414,18415,18416,18417,18418,18419,18420,18421,18422,18423,18424,18425,18426,18427,18428,18429,18430,18431,18432,18433,18434,18435,18436,18437,18438,18439,18440,18441,18442,18443,18444,18445,18446,18447,18448,18449,18451,18452,18453,18454,18455,18456,18457,18458,18459,18460,18461,18462,18463,18464,18465,18466,18467,18468,18469,18470,18471,18472,18473,18474,18475,18476,18477,18478,18479,18480,18481,18482,18483,18484,18485,18486,18487,18488,18489,18490,18491,18492,18493,18494,18495,18496,18497,18498,18499,18500,18501,18502,18503,18504,18505],"y":[1779,7367,29652,34265,31525,25199,38621,55809,87863,79468,32381,30816,40125,38926,57546,37426,36644,28605,34696,36933,35732,29933,34886,42630,34077,28558,36403,37461,36651,46114,32103,24620,3131,29894,25411,36828,38060,85570,186589,139380,56736,166550,180967,54860,65106,58691,57205,54956,52935,55194,57886,50904,58287,62347,61901,119588,79093,147820,145708,147177,159768,154096,59905,82139,164222,168503,181405,165763,111465,69065,99590,133029,146956,169359,175835,165782,169907,123767,112042,169338,156513,156765,144962,147794,139577,158784,139740,147939,154989,141486,64995,155783,162116,205650,182142,173997,195564,135317,123804,184956,174887,167662,165242,164999,115329,194664,211138,203376,196314,190712,225094,196789,204098,206032,201194,199783,178960,186919,189823,197151,183519,187626,173097,175900,181828,200750,148590,163602,144482,130850,124468,119633,120688,138224,129475,114832,233194,215192,248729,262520,291954,289951,297217,286161,273345,274508,257735,253791,317809,312573,286907,260257,284394,292901,267041,288254,320788,309405,285082,278691,291377,380382,323262,381075,404988,308958,284400,289676,283799,289704,316961,317844,385187,287513,290065,244262,263648,305081,324834,288230,313095,327083,314388,290388,258984,245698,308827,277755,330152,296939,311090,305727,275067,272010,279321,253278,243074,270831,279584,251729,331673,324918,262741,269495,250359,322091,234664,251370,311691,327667,282167,280557,260225,281826,292210,315643,236324,247058,265473,260191,282363,243374],"text":["Date: 2020-01-22<br />Count:    1779<br />Sentiment: positive","Date: 2020-01-23<br />Count:    7367<br />Sentiment: positive","Date: 2020-01-24<br />Count:   29652<br />Sentiment: positive","Date: 2020-01-25<br />Count:   34265<br />Sentiment: positive","Date: 2020-01-26<br />Count:   31525<br />Sentiment: positive","Date: 2020-01-27<br />Count:   25199<br />Sentiment: positive","Date: 2020-01-28<br />Count:   38621<br />Sentiment: positive","Date: 2020-01-29<br />Count:   55809<br />Sentiment: positive","Date: 2020-01-30<br />Count:   87863<br />Sentiment: positive","Date: 2020-01-31<br />Count:   79468<br />Sentiment: positive","Date: 2020-02-01<br />Count:   32381<br />Sentiment: positive","Date: 2020-02-02<br />Count:   30816<br />Sentiment: positive","Date: 2020-02-03<br />Count:   40125<br />Sentiment: positive","Date: 2020-02-04<br />Count:   38926<br />Sentiment: positive","Date: 2020-02-05<br />Count:   57546<br />Sentiment: positive","Date: 2020-02-06<br />Count:   37426<br />Sentiment: positive","Date: 2020-02-07<br />Count:   36644<br />Sentiment: positive","Date: 2020-02-08<br />Count:   28605<br />Sentiment: positive","Date: 2020-02-09<br />Count:   34696<br />Sentiment: positive","Date: 2020-02-10<br />Count:   36933<br />Sentiment: positive","Date: 2020-02-11<br />Count:   35732<br />Sentiment: positive","Date: 2020-02-12<br />Count:   29933<br />Sentiment: positive","Date: 2020-02-13<br />Count:   34886<br />Sentiment: positive","Date: 2020-02-14<br />Count:   42630<br />Sentiment: positive","Date: 2020-02-15<br />Count:   34077<br />Sentiment: positive","Date: 2020-02-16<br />Count:   28558<br />Sentiment: positive","Date: 2020-02-17<br />Count:   36403<br />Sentiment: positive","Date: 2020-02-18<br />Count:   37461<br />Sentiment: positive","Date: 2020-02-19<br />Count:   36651<br />Sentiment: positive","Date: 2020-02-20<br />Count:   46114<br />Sentiment: positive","Date: 2020-02-21<br />Count:   32103<br />Sentiment: positive","Date: 2020-02-22<br />Count:   24620<br />Sentiment: positive","Date: 2020-02-23<br />Count:    3131<br />Sentiment: positive","Date: 2020-02-24<br />Count:   29894<br />Sentiment: positive","Date: 2020-02-25<br />Count:   25411<br />Sentiment: positive","Date: 2020-02-26<br />Count:   36828<br />Sentiment: positive","Date: 2020-02-27<br />Count:   38060<br />Sentiment: positive","Date: 2020-02-28<br />Count:   85570<br />Sentiment: positive","Date: 2020-02-29<br />Count:  186589<br />Sentiment: positive","Date: 2020-03-01<br />Count:  139380<br />Sentiment: positive","Date: 2020-03-02<br />Count:   56736<br />Sentiment: positive","Date: 2020-03-03<br />Count:  166550<br />Sentiment: positive","Date: 2020-03-04<br />Count:  180967<br />Sentiment: positive","Date: 2020-03-05<br />Count:   54860<br />Sentiment: positive","Date: 2020-03-06<br />Count:   65106<br />Sentiment: positive","Date: 2020-03-07<br />Count:   58691<br />Sentiment: positive","Date: 2020-03-08<br />Count:   57205<br />Sentiment: positive","Date: 2020-03-09<br />Count:   54956<br />Sentiment: positive","Date: 2020-03-10<br />Count:   52935<br />Sentiment: positive","Date: 2020-03-11<br />Count:   55194<br />Sentiment: positive","Date: 2020-03-12<br />Count:   57886<br />Sentiment: positive","Date: 2020-03-13<br />Count:   50904<br />Sentiment: positive","Date: 2020-03-14<br />Count:   58287<br />Sentiment: positive","Date: 2020-03-15<br />Count:   62347<br />Sentiment: positive","Date: 2020-03-16<br />Count:   61901<br />Sentiment: positive","Date: 2020-03-17<br />Count:  119588<br />Sentiment: positive","Date: 2020-03-18<br />Count:   79093<br />Sentiment: positive","Date: 2020-03-19<br />Count:  147820<br />Sentiment: positive","Date: 2020-03-20<br />Count:  145708<br />Sentiment: positive","Date: 2020-03-21<br />Count:  147177<br />Sentiment: positive","Date: 2020-03-22<br />Count:  159768<br />Sentiment: positive","Date: 2020-03-23<br />Count:  154096<br />Sentiment: positive","Date: 2020-03-24<br />Count:   59905<br />Sentiment: positive","Date: 2020-03-25<br />Count:   82139<br />Sentiment: positive","Date: 2020-03-26<br />Count:  164222<br />Sentiment: positive","Date: 2020-03-27<br />Count:  168503<br />Sentiment: positive","Date: 2020-03-28<br />Count:  181405<br />Sentiment: positive","Date: 2020-03-29<br />Count:  165763<br />Sentiment: positive","Date: 2020-03-30<br />Count:  111465<br />Sentiment: positive","Date: 2020-03-31<br />Count:   69065<br />Sentiment: positive","Date: 2020-04-01<br />Count:   99590<br />Sentiment: positive","Date: 2020-04-02<br />Count:  133029<br />Sentiment: positive","Date: 2020-04-03<br />Count:  146956<br />Sentiment: positive","Date: 2020-04-04<br />Count:  169359<br />Sentiment: positive","Date: 2020-04-05<br />Count:  175835<br />Sentiment: positive","Date: 2020-04-06<br />Count:  165782<br />Sentiment: positive","Date: 2020-04-07<br />Count:  169907<br />Sentiment: positive","Date: 2020-04-08<br />Count:  123767<br />Sentiment: positive","Date: 2020-04-09<br />Count:  112042<br />Sentiment: positive","Date: 2020-04-10<br />Count:  169338<br />Sentiment: positive","Date: 2020-04-11<br />Count:  156513<br />Sentiment: positive","Date: 2020-04-12<br />Count:  156765<br />Sentiment: positive","Date: 2020-04-13<br />Count:  144962<br />Sentiment: positive","Date: 2020-04-14<br />Count:  147794<br />Sentiment: positive","Date: 2020-04-15<br />Count:  139577<br />Sentiment: positive","Date: 2020-04-16<br />Count:  158784<br />Sentiment: positive","Date: 2020-04-17<br />Count:  139740<br />Sentiment: positive","Date: 2020-04-18<br />Count:  147939<br />Sentiment: positive","Date: 2020-04-19<br />Count:  154989<br />Sentiment: positive","Date: 2020-04-20<br />Count:  141486<br />Sentiment: positive","Date: 2020-04-21<br />Count:   64995<br />Sentiment: positive","Date: 2020-04-22<br />Count:  155783<br />Sentiment: positive","Date: 2020-04-23<br />Count:  162116<br />Sentiment: positive","Date: 2020-04-24<br />Count:  205650<br />Sentiment: positive","Date: 2020-04-25<br />Count:  182142<br />Sentiment: positive","Date: 2020-04-26<br />Count:  173997<br />Sentiment: positive","Date: 2020-04-27<br />Count:  195564<br />Sentiment: positive","Date: 2020-04-28<br />Count:  135317<br />Sentiment: positive","Date: 2020-04-29<br />Count:  123804<br />Sentiment: positive","Date: 2020-04-30<br />Count:  184956<br />Sentiment: positive","Date: 2020-05-01<br />Count:  174887<br />Sentiment: positive","Date: 2020-05-02<br />Count:  167662<br />Sentiment: positive","Date: 2020-05-03<br />Count:  165242<br />Sentiment: positive","Date: 2020-05-04<br />Count:  164999<br />Sentiment: positive","Date: 2020-05-05<br />Count:  115329<br />Sentiment: positive","Date: 2020-05-06<br />Count:  194664<br />Sentiment: positive","Date: 2020-05-07<br />Count:  211138<br />Sentiment: positive","Date: 2020-05-08<br />Count:  203376<br />Sentiment: positive","Date: 2020-05-09<br />Count:  196314<br />Sentiment: positive","Date: 2020-05-10<br />Count:  190712<br />Sentiment: positive","Date: 2020-05-11<br />Count:  225094<br />Sentiment: positive","Date: 2020-05-12<br />Count:  196789<br />Sentiment: positive","Date: 2020-05-13<br />Count:  204098<br />Sentiment: positive","Date: 2020-05-14<br />Count:  206032<br />Sentiment: positive","Date: 2020-05-15<br />Count:  201194<br />Sentiment: positive","Date: 2020-05-16<br />Count:  199783<br />Sentiment: positive","Date: 2020-05-17<br />Count:  178960<br />Sentiment: positive","Date: 2020-05-18<br />Count:  186919<br />Sentiment: positive","Date: 2020-05-19<br />Count:  189823<br />Sentiment: positive","Date: 2020-05-20<br />Count:  197151<br />Sentiment: positive","Date: 2020-05-21<br />Count:  183519<br />Sentiment: positive","Date: 2020-05-22<br />Count:  187626<br />Sentiment: positive","Date: 2020-05-23<br />Count:  173097<br />Sentiment: positive","Date: 2020-05-24<br />Count:  175900<br />Sentiment: positive","Date: 2020-05-25<br />Count:  181828<br />Sentiment: positive","Date: 2020-05-26<br />Count:  200750<br />Sentiment: positive","Date: 2020-05-27<br />Count:  148590<br />Sentiment: positive","Date: 2020-05-28<br />Count:  163602<br />Sentiment: positive","Date: 2020-05-29<br />Count:  144482<br />Sentiment: positive","Date: 2020-05-30<br />Count:  130850<br />Sentiment: positive","Date: 2020-05-31<br />Count:  124468<br />Sentiment: positive","Date: 2020-06-01<br />Count:  119633<br />Sentiment: positive","Date: 2020-06-02<br />Count:  120688<br />Sentiment: positive","Date: 2020-06-03<br />Count:  138224<br />Sentiment: positive","Date: 2020-06-04<br />Count:  129475<br />Sentiment: positive","Date: 2020-06-05<br />Count:  114832<br />Sentiment: positive","Date: 2020-06-06<br />Count:  233194<br />Sentiment: positive","Date: 2020-06-07<br />Count:  215192<br />Sentiment: positive","Date: 2020-06-08<br />Count:  248729<br />Sentiment: positive","Date: 2020-06-09<br />Count:  262520<br />Sentiment: positive","Date: 2020-06-10<br />Count:  291954<br />Sentiment: positive","Date: 2020-06-11<br />Count:  289951<br />Sentiment: positive","Date: 2020-06-12<br />Count:  297217<br />Sentiment: positive","Date: 2020-06-13<br />Count:  286161<br />Sentiment: positive","Date: 2020-06-14<br />Count:  273345<br />Sentiment: positive","Date: 2020-06-15<br />Count:  274508<br />Sentiment: positive","Date: 2020-06-16<br />Count:  257735<br />Sentiment: positive","Date: 2020-06-17<br />Count:  253791<br />Sentiment: positive","Date: 2020-06-18<br />Count:  317809<br />Sentiment: positive","Date: 2020-06-19<br />Count:  312573<br />Sentiment: positive","Date: 2020-06-20<br />Count:  286907<br />Sentiment: positive","Date: 2020-06-21<br />Count:  260257<br />Sentiment: positive","Date: 2020-06-22<br />Count:  284394<br />Sentiment: positive","Date: 2020-06-23<br />Count:  292901<br />Sentiment: positive","Date: 2020-06-24<br />Count:  267041<br />Sentiment: positive","Date: 2020-06-25<br />Count:  288254<br />Sentiment: positive","Date: 2020-06-26<br />Count:  320788<br />Sentiment: positive","Date: 2020-06-27<br />Count:  309405<br />Sentiment: positive","Date: 2020-06-28<br />Count:  285082<br />Sentiment: positive","Date: 2020-06-29<br />Count:  278691<br />Sentiment: positive","Date: 2020-06-30<br />Count:  291377<br />Sentiment: positive","Date: 2020-07-01<br />Count:  380382<br />Sentiment: positive","Date: 2020-07-02<br />Count:  323262<br />Sentiment: positive","Date: 2020-07-03<br />Count:  381075<br />Sentiment: positive","Date: 2020-07-04<br />Count:  404988<br />Sentiment: positive","Date: 2020-07-05<br />Count:  308958<br />Sentiment: positive","Date: 2020-07-06<br />Count:  284400<br />Sentiment: positive","Date: 2020-07-08<br />Count:  289676<br />Sentiment: positive","Date: 2020-07-09<br />Count:  283799<br />Sentiment: positive","Date: 2020-07-10<br />Count:  289704<br />Sentiment: positive","Date: 2020-07-11<br />Count:  316961<br />Sentiment: positive","Date: 2020-07-12<br />Count:  317844<br />Sentiment: positive","Date: 2020-07-13<br />Count:  385187<br />Sentiment: positive","Date: 2020-07-14<br />Count:  287513<br />Sentiment: positive","Date: 2020-07-15<br />Count:  290065<br />Sentiment: positive","Date: 2020-07-16<br />Count:  244262<br />Sentiment: positive","Date: 2020-07-17<br />Count:  263648<br />Sentiment: positive","Date: 2020-07-18<br />Count:  305081<br />Sentiment: positive","Date: 2020-07-19<br />Count:  324834<br />Sentiment: positive","Date: 2020-07-20<br />Count:  288230<br />Sentiment: positive","Date: 2020-07-21<br />Count:  313095<br />Sentiment: positive","Date: 2020-07-22<br />Count:  327083<br />Sentiment: positive","Date: 2020-07-23<br />Count:  314388<br />Sentiment: positive","Date: 2020-07-24<br />Count:  290388<br />Sentiment: positive","Date: 2020-07-25<br />Count:  258984<br />Sentiment: positive","Date: 2020-07-26<br />Count:  245698<br />Sentiment: positive","Date: 2020-07-27<br />Count:  308827<br />Sentiment: positive","Date: 2020-07-28<br />Count:  277755<br />Sentiment: positive","Date: 2020-07-29<br />Count:  330152<br />Sentiment: positive","Date: 2020-07-30<br />Count:  296939<br />Sentiment: positive","Date: 2020-07-31<br />Count:  311090<br />Sentiment: positive","Date: 2020-08-01<br />Count:  305727<br />Sentiment: positive","Date: 2020-08-02<br />Count:  275067<br />Sentiment: positive","Date: 2020-08-03<br />Count:  272010<br />Sentiment: positive","Date: 2020-08-04<br />Count:  279321<br />Sentiment: positive","Date: 2020-08-05<br />Count:  253278<br />Sentiment: positive","Date: 2020-08-06<br />Count:  243074<br />Sentiment: positive","Date: 2020-08-07<br />Count:  270831<br />Sentiment: positive","Date: 2020-08-08<br />Count:  279584<br />Sentiment: positive","Date: 2020-08-09<br />Count:  251729<br />Sentiment: positive","Date: 2020-08-10<br />Count:  331673<br />Sentiment: positive","Date: 2020-08-11<br />Count:  324918<br />Sentiment: positive","Date: 2020-08-12<br />Count:  262741<br />Sentiment: positive","Date: 2020-08-13<br />Count:  269495<br />Sentiment: positive","Date: 2020-08-14<br />Count:  250359<br />Sentiment: positive","Date: 2020-08-15<br />Count:  322091<br />Sentiment: positive","Date: 2020-08-16<br />Count:  234664<br />Sentiment: positive","Date: 2020-08-17<br />Count:  251370<br />Sentiment: positive","Date: 2020-08-18<br />Count:  311691<br />Sentiment: positive","Date: 2020-08-19<br />Count:  327667<br />Sentiment: positive","Date: 2020-08-20<br />Count:  282167<br />Sentiment: positive","Date: 2020-08-21<br />Count:  280557<br />Sentiment: positive","Date: 2020-08-22<br />Count:  260225<br />Sentiment: positive","Date: 2020-08-23<br />Count:  281826<br />Sentiment: positive","Date: 2020-08-24<br />Count:  292210<br />Sentiment: positive","Date: 2020-08-25<br />Count:  315643<br />Sentiment: positive","Date: 2020-08-26<br />Count:  236324<br />Sentiment: positive","Date: 2020-08-27<br />Count:  247058<br />Sentiment: positive","Date: 2020-08-28<br />Count:  265473<br />Sentiment: positive","Date: 2020-08-29<br />Count:  260191<br />Sentiment: positive","Date: 2020-08-30<br />Count:  282363<br />Sentiment: positive","Date: 2020-08-31<br />Count:  243374<br />Sentiment: positive"],"type":"scatter","mode":"lines","line":{"width":3.77952755905512,"color":"rgba(97,156,255,1)","dash":"solid"},"hoveron":"points","name":"(positive,1)","legendgroup":"(positive,1)","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null}],"layout":{"margin":{"t":44.8252386882524,"r":7.30593607305936,"b":45.7617268576173,"l":76.0481527604815},"plot_bgcolor":"rgba(255,255,255,1)","paper_bgcolor":"rgba(255,255,255,1)","font":{"color":"rgba(0,0,0,1)","family":"","size":14.6118721461187},"title":{"text":"<b> Sentiment of English Tweets <\/b>","font":{"color":"rgba(0,0,0,1)","family":"","size":18.5969281859693},"x":0,"xref":"paper"},"xaxis":{"domain":[0,1],"automargin":true,"type":"linear","autorange":false,"range":[18271.9,18516.1],"tickmode":"array","ticktext":["Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"],"tickvals":[18293,18322,18353,18383,18414,18444,18475,18506],"categoryorder":"array","categoryarray":["Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"],"nticks":null,"ticks":"outside","tickcolor":"rgba(51,51,51,1)","ticklen":3.65296803652968,"tickwidth":0.66417600664176,"showticklabels":true,"tickfont":{"color":"rgba(0,0,0,1)","family":"","size":13.2835201328352},"tickangle":-0,"showline":false,"linecolor":null,"linewidth":0,"showgrid":true,"gridcolor":"rgba(235,235,235,1)","gridwidth":0.66417600664176,"zeroline":false,"anchor":"y","title":{"text":"<b> Date <\/b>","font":{"color":"rgba(0,0,0,1)","family":"","size":18.5969281859693}},"hoverformat":".2f"},"yaxis":{"domain":[0,1],"automargin":true,"type":"linear","autorange":false,"range":[-97943.5,2095951.5],"tickmode":"array","ticktext":["0","500000","1000000","1500000","2000000"],"tickvals":[0,500000,1000000,1500000,2000000],"categoryorder":"array","categoryarray":["0","500000","1000000","1500000","2000000"],"nticks":null,"ticks":"outside","tickcolor":"rgba(51,51,51,1)","ticklen":3.65296803652968,"tickwidth":0.66417600664176,"showticklabels":true,"tickfont":{"color":"rgba(0,0,0,1)","family":"","size":13.2835201328352},"tickangle":-0,"showline":false,"linecolor":null,"linewidth":0,"showgrid":true,"gridcolor":"rgba(235,235,235,1)","gridwidth":0.66417600664176,"zeroline":false,"anchor":"x","title":{"text":"<b> Number of Tweets <\/b>","font":{"color":"rgba(0,0,0,1)","family":"","size":18.5969281859693}},"hoverformat":".2f"},"shapes":[{"type":"rect","fillcolor":"transparent","line":{"color":"rgba(51,51,51,1)","width":0.66417600664176,"linetype":"solid"},"yref":"paper","xref":"paper","x0":0,"x1":1,"y0":0,"y1":1}],"showlegend":false,"legend":{"bgcolor":"rgba(255,255,255,1)","bordercolor":"transparent","borderwidth":1.88976377952756,"font":{"color":"rgba(0,0,0,1)","family":"","size":13.2835201328352},"y":0.917322834645669},"annotations":[],"hovermode":"closest","barmode":"relative"},"config":{"doubleClick":"reset","showSendToCloud":false},"source":"A","attrs":{"33382b5a4458":{"x":{},"y":{},"colour":{},"type":"scatter"}},"cur_data":"33382b5a4458","visdat":{"33382b5a4458":["function (y) ","x"]},".hideLegend":true,"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.2,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>

<!--/html_preserve-->

### Named Entity Recognition, Mentions, and Hashtags

The Named Entity Recognition algorithm of [Python
flairNLP](https://github.com/flairNLP/flair) was used to extract topics
of conversation about person, locations, organization, and others. Below
are the top 5 NER, mentions and Hastags

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

  - Only tweets in English were collected from 22 January to 31 January
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

<https://github.com/echen102/COVID-19-TweetIDs>
