# CMPT 353 FINAL PROJECT

Fall 2020 CMPT353 GROUP PROJECT

## Required libraries
For python 3.6+
1. pandas
2. numpy
3. scipy
4. matplotlib
5. seaborn
## Order of execution

- Get the data (10.25 is the patch we are using, it can be anything from 10.1 to 10.25)
- This cleans the data in order to create a Pandas dataframe

## Gathering

```
python3 get_data.py 10.25 champions.json
```
You should now have a json file with the champion data. 

To augment that, we have releases.py, which is manually entered data as explained in the report and has this shape:
```
{
	“name”: {“date:” “yyyy-mm-dd”, “passive”: “champion passive...”},
	“name”: {“date:” “yyyy-mm-dd”, “passive”: “champion passive...”},
	“name”: {“date:” “yyyy-mm-dd”, “passive”: “champion passive...”},
}
```
- `champions.json` (provied) contains all the champion data after the fetch (so you don't have to run get_data.py since it takes 3 minutes to run due to api throttling)

## Analysis
 ```
 python3 parse.py champions.json parsed.csv
 ```
- `champions.json` is the name of the file get_data released.
- `parsed.csv` will now contain the output of the parse.py file, which is the list of champions and their word count (sorted by total word count)

The program will print the lingress' slope, intercept and pvalue to stdout.
The program will save champions.png which is the plot of word count and regerssion.

## Extras

During our investiagtion we made a program file `mataches.py`
This is for users who want to figure out how many games they have played over a period of time.

Usage:
```
python3 matches.py [USERNAME] [MODE] [DATE]
```

Username is the players string username
Mode is one of the following game modes:
  - Ranked 
  - Blind pick 
  - Bots (intro, easy, hard)
  - Aram
  - One for all
  - URF
  - ALL

Date is either dd-mm-yyyy formated date or a patch (from 10.01 to 10.25) and indicates the start date (ie. how many games have been played since 10.01 or 01-01-2020, etc).

In order to run this program, users need to create a `secret.py` file that includes an api provided from [Riot's Developer Portal](https://developer.riotgames.com/)

You file should look like this:

```
key = '[THIS IS THE API KEY]'
```

This may take a few seconds but, you can now see how many games you have played.
