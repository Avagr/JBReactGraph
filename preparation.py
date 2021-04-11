import requests
import json
from requests.models import HTTPError

url = "https://api.github.com/repos/facebook/react/stats/contributors"


# Function for encoding sets into json as lists
def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


# Prepares data and writes it to the disk
def prepare_data(token=None):
    header = {}
    if token:
        header = {'Authorization': 'token %s' % token}
    contributors = requests.get(url, headers=header)
    if contributors.status_code != 200:
        raise HTTPError(contributors.json())

    authors = {}  # A dictionary for storing all the relevant information
    for cont in sorted(contributors.json(), key=lambda x: -x['total'])[:50]:
        name_req = requests.get(cont['author']['url'], headers=header)
        if name_req.status_code != 200:
            raise HTTPError(name_req.json())
        name = name_req.json()['name']
        if not name:  # If there is no name in github, use their login
            name = name_req.json()['login']
            if name == 'marocchino':  # Cross-referenced this person using commit hashes
                name = 'Shim Won'
        authors[name] = {'total': cont['total'],
                         'files': set(),
                         'maxdate': -1,
                         # this unix time is in the far far future
                         'mindate': 99999999999}

    with open('git_log.txt', 'r') as log:
        for line in log:
            if line.strip() == '':
                continue
            if line[0] == '$':
                _, date, name = line.strip().split(maxsplit=2)
                if name in authors:
                    # Searching for the earliest and the latest commit date
                    authors[name]['mindate'] = min(authors[name]['mindate'], int(date))
                    authors[name]['maxdate'] = max(authors[name]['maxdate'], int(date))
            else:
                if name in authors:
                    authors[name]['files'].add(line.strip())

    with open('authors.json', 'w') as output:
        json.dump(authors, output, default=set_default)
