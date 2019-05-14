from bs4 import BeautifulSoup
import urllib.request
import numpy as np
import pickle



print('Extracting from https://www.worldfootball.net/schedule/ita-serie-a-1991-1992-spieltag/')
home_goals = []
away_goals = []
home_team = []
away_team = []

for round in np.arange(1,35):

    url = "https://www.worldfootball.net/schedule/ita-serie-a-1991-1992-spieltag/{}/".format(round)
    print('Connecting to {}'.format(url))
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    name_box = list(soup.find_all('td', attrs={'class': 'hell', 'nowrap': 'nowrap'}))
    name_box1 = list(soup.find_all('td', attrs={'class': 'dunkel', 'nowrap': 'nowrap'}))
    table = name_box + name_box1

    slc = slice(2,29,3) #found by printing line numbers
    table = table[slc]

    for line in table:
        a = str(line).split()
        print(a)
        separator = a.index('-')
        if '>' in a[separator+2]:
            home_goals.append(int(a[separator+2][-3]))
            away_goals.append(int(a[separator+2][-1]))
            away_team.append(a[separator+1]+a[separator+2].split('"')[0])
            if a[separator-2] == 'details':
                home_team.append(a[separator-1])
            else:
                home_team.append(a[separator-2]+a[separator-1])
        else:
            home_goals.append(int(a[separator+1][-3]))
            away_goals.append(int(a[separator+1][-1]))
            away_team.append(a[separator+1].split('"')[0])
            if a[separator-2] == 'details':
                home_team.append(a[separator-1])
            else:
                home_team.append(a[separator-2]+ a[separator-1])

        

data = {}
data['home_goals'] = home_goals
data['away_goals'] = away_goals
data['home_team'] = home_team
data['away_team'] = away_team


with open('data.pickle', 'wb') as f:
    pickle.dump(data,f)
