import requests

from pprint import pprint
from team_abbreviation import get_response

prefix = 'https://statsapi.web.nhl.com'
file = 'data/teams/team_names.txt'

def get_teams():
    data = get_response().json()
    return data.get('teams')

def get_team_info(abbreviation):
    teams = get_teams()

    for i in range(len(teams)):
        if teams[i]['abbreviation'] == abbreviation.upper():
            return teams[i]

def write_info_to_file(team, file):
    path = 'data/tests/' + file
    with open(path, 'w') as f:
        f.write(get_team_info(team))

def get_team_link(team):
    data = get_team_info(team)
    return data.get('link')

def get_team_roster(team):
    team_link = get_team_link(team)
    response = requests.get(prefix+team_link+'?expand=team.roster')
    pprint(response.json())