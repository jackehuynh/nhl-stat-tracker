import requests

path = 'data/teams/'

def get_response():
    response = requests.get("https://statsapi.web.nhl.com/api/v1/teams")
    return response

def get_abbreviations():
    data = get_response().json()
    teams = data.get('teams')
    abbrev_list = []

    for i in range(len(teams)):
        abbrev_list.append(teams[i]['abbreviation'])
    return abbrev_list

def write_abbrev_to_file(fileName):
    file = path + fileName
    abbrev_list = get_abbreviations()

    with open(file, 'w') as f:
        for item in abbrev_list:
            f.write('%s\n' % item)