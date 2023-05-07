import requests

url = 'https://www.premierleague.com/stats'

response = requests.get(url)

if response.status_code == 200:

    data = response.content

    # process the data

else:

    print('Error: Could not get data from the website')

