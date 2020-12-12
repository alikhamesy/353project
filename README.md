# CMPT 353 FINAL PROJECT

Fall 2020 CMPT353 GROUP PROJECT

## Required libraries
For python 3.6+
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import seaborn
```
## Order of execution

- Get the data (10.25 is the version we are using, it can be anything from 10.1 to 10.25)
- This cleans the data in order to create a Pandas dataframe


``` 
python3 get_data.py 10.25 champions.json
```
You should now have a json file in this format 
```
{
	“name”: {“date:” “yyyy-mm-dd”, “passive”: “champion passive...”},
	“name”: {“date:” “yyyy-mm-dd”, “passive”: “champion passive...”},
	“name”: {“date:” “yyyy-mm-dd”, “passive”: “champion passive...”},
}
```
Along with a file a `released.py` file in the format:
```
{
	“name”: {“date:” “yyyy-mm-dd”, “passive”: “champion passive...”},
	“name”: {“date:” “yyyy-mm-dd”, “passive”: “champion passive...”},
	“name”: {“date:” “yyyy-mm-dd”, “passive”: “champion passive...”},
}
```
- `champions.json` will now contain all the champion data after the fetch (so you don't have to run get_data.py)
- Run: 

 ```
 python3 parse.py champions.json parsed.csv
 ```
- `parsed.csv` will now contain the output of the parse.py file, which is the list of champions and their word count (sorted by total word count)
## Extras

During our investiagtion we made a program file `mataches.py`

This is for users who want to figure out how many games they have played over a period of time.
Which includes different game modes:
  - Ranked 
  - Blind pick 
  - Bots (intro, easy, hard)
  - Aram
  - One for all
  - URF

In order to run this program, users need to create a `secret.py` file that includes an api provided from Riot

You file should look something like this:

```
key = '[THIS IS THE API KEY]'
```
Run:
```
python3 matches.py [USERNAME] ALL [DD-MM-YYYY]
```
This may take a few seconds but, you can now see how many games you have played from the [DD-MM-YYYY] inputted  starting date.
