import requests

url = 'https://www.premierleague.com/stats'

response = requests.get(url)

if response.status_code == 200:

    data = response.content

    # process the data

else:

    print('Error: Could not get data from the website')

import pandas as pd

data = pd.read_csv('premier_league_data.csv')

# drop duplicates

data = data.drop_duplicates()

# drop rows with missing values

data = data.dropna()

# drop irrelevant columns

data = data.drop(['column1', 'column2'], axis=1)

