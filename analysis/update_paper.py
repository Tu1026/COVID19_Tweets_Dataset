import os
from shutil import copyfile
import pandas as pd
import datetime
import csv
# Currently the root of the git: COVID19_Tweets_Dataset. If not, make it the root of the git.
print(os.getcwd())
data_directory = "analysis/until_2020_04_01/"
# Folder name is used to find date of analysis.
# NOTE: IMPORANT: CODE ASSUMES THE STRUCTURE OF THE CSV FILES IS ALWAYS THE SAME
# paper_directory is the location for the .tex files are, and the folders data/ and images/
paper_directory = "analysis/paper/"
number_of_languages = 14
version = "v1.2"


def setUpTexVariables():
    """
    Creates a dictionary of variables that will be stored in variables.txt. paper.tex loads all these variables so that they can be accessed just like any regular latex command.

    Returns:
        dict -- variables for LaTeX
    """
    tex_variables = {}
    tex_variables["version"] = version
    # Gets latest date from folder name.
    date_object = datetime.datetime.strptime(
        data_directory[data_directory.index("_")+1:-1],
        "%Y_%m_%d")
    tex_variables["date"] = date_object.strftime("%b %d, %Y")
    tex_variables["latestDay"] = date_object.strftime("%d")
    tex_variables["latestMonth"] = date_object.strftime("%B")
    return tex_variables


def cleanTable1(tex_variables):
    """
    Cleans Table 1 of paper.tex that displays the mean
     number of tweets, SD, and median on one day, for each month.

    Reads the file analysis/until_2020_04_01/Tweets_Number_by_Month.csv
    Writes to file analysis/paper/data/table1.csv

    Arguments:
        tex_variables {string: string} -- Stored in variables.txt. paper.tex loads all these variables so that they can be accessed just like any regular latex command.
    """
    table1 = pd.read_csv(
        data_directory + "Tweets_Number_by_Month.csv", engine='python')
    table1.drop(table1.columns[0], axis=1, inplace=True)
    table1 = table1.rename(columns={"M": "Mean",  "Mdn": "Median"})
    table1 = table1.round(2)
    tex_variables["tweetsNumber"] = table1["Total"][0]

    # Now alter df to store as table1.csv
    # Uses only all tweets: not original or retweets
    table1 = table1[table1["Type"] == "All"]
    # Does it for every month from Jan through December
    for i in range(1, 13):
        if (i < len(table1)):
            tex_variables["tweetsNumber" +
                          table1["Month"][i]] = table1["Total"][i]
    tex_variables["dailyNumAvg"] = table1["Mean"][0]
    tex_variables["dailyNumSD"] = table1["SD"][0]
    tex_variables["dailyNumMedian"] = table1["Median"][0]
    table1 = table1.drop([0])
    table1 = table1.drop(["Total", "Type", "NoDays"], axis=1)
    table1.to_csv(paper_directory + "data/table1.csv", index=False, na_rep="0")


def cleanTable2(tex_variables):
    """
    Cleans Table 2 of paper.tex that displays languages upto number_of_languages, the number of tweets in that language, and its percent share.

    Reads the file analysis/until_2020_04_01/TweetLanguages.csv
    Writes to file analysis/paper/data/table2.csv

    Arguments:
        tex_variables {string: string} -- Stored in variables.txt. paper.tex loads all these variables so that they can be accessed just like any regular latex command.
    """
    table2 = pd.read_csv(
        data_directory + "TweetLanguages.csv", engine="python")
    table2 = table2.rename(
        columns={"Var1": "Language", "Freq": "Number of Tweets"})
    table2["Percentage"] = table2["Percentage"]*100

    tex_variables["languagesNumber"] = len(table2)
    tex_variables["englishPercent"] = table2["Percentage"].loc[0].round(2)
    finalTable2 = table2[:number_of_languages+1]
    # Stores number_of_languages. The rest are summed up into Other.
    finalTable2.loc[number_of_languages] = ["Other", table2["Number of Tweets"][number_of_languages:].sum(),
                                            table2["Percentage"][number_of_languages:].sum()]

    finalTable2 = finalTable2.round(2)
    finalTable2.to_csv(paper_directory + "data/table2.csv",
                       index=False, na_rep="0")


def cleanTable3(tex_variables):
    """
    Cleans Table 3 of paper.tex that displays summary statistics on number geolocated tweets, retweets, likes.

    Reads the file analysis/until_2020_04_01/SummaryTable.csv
    Writes to file analysis/paper/data/table3.csv

    Arguments:
        tex_variables {string: string} -- Stored in variables.txt. paper.tex loads all these variables so that they can be accessed just like any regular latex command.
    """
    table3 = pd.read_csv(data_directory + "SummaryTable.csv")
    table3["V1"] = table3["V1"].str.replace(":", "")
    # Change the row range to select other stats to display
    table3 = table3.loc[2:len(table3) - 4]
    table3.to_csv(paper_directory
                  + "data/table3.csv", header=False, index=False, na_rep="0")
    print(table3)


def writeTexVariables(tex_variables):
    """Writes tex_variables to a file where each variable is separated from its value by a space

    Arguments:
        tex_variables {string: string} -- Stored in variables.txt. paper.tex loads all these variables so that they can be accessed just like any regular latex command.
    """
    with open(paper_directory + "data/variables.txt", "w+") as f:
        for key in tex_variables:
            f.write(key + " " + str(tex_variables[key]) + "\n")


def copyFigures():
    """
    Copies figures from the data_directory to paper_directory/images/
    Figures copied from:
        analysis/until_2020_04_01/Tweets by Language.png
        analysis/until_2020_04_01/Retweets.png
        analysis/until_2020_04_01/GeoTweets.png
    Figures pasted in:
        analysis/paper/images/language.png
        analysis/paper/images/retweets.png
        analysis/paper/images/geotweets.png
    """
    copyfile(data_directory + "Tweets by Language.png",
             paper_directory + "images/language.png")
    copyfile(data_directory + "Retweets.png",
             paper_directory + "images/retweets.png")
    copyfile(data_directory + "Geotweets.png",
             paper_directory + "images/geotweets.png")


def main():
    """
    Sets up tex_variables. Cleans each table, writes the files, copies the figures, and compiles the paper pdf file.
    NOTE: IMPORANT: CODE ASSUMES THE STRUCTURE OF THE CSV FILES IS ALWAYS THE SAME
    NOTE: IMPORTANT: INSTALL ALL TEX PACKAGES FOR THIS CODE TO WORK. Ensure you have pdflatex. Install with MiKTeX or TeX Live.
    NOTE: Paper will be stored in analysis/paper/paper.pdf
    """
    tex_variables = setUpTexVariables()
    cleanTable1(tex_variables)
    cleanTable2(tex_variables)
    cleanTable3(tex_variables)
    writeTexVariables(tex_variables)
    copyFigures()

    # pdflatex paper.tex may produce many errors. These are due to missing LaTeX packages. Install each package used using tlmgr.
    # Installing required packages will resolve errors.
    os.chdir(os.path.dirname(paper_directory))
    os.system("pdflatex paper.tex")


if __name__ == "__main__":
    main()
