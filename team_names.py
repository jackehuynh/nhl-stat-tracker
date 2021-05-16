import requests

response = requests.get("https://statsapi.web.nhl.com/api/v1/teams")

data = response.json()
teams = data.get('teams')

teams_list = []

for i in range(len(teams)):
    teams_list.append(teams[i]['name'])

file = 'data/teams/team_names.txt'

with open(file, 'w') as f:
    f.writelines("%s\n" % team for team in teams_list)