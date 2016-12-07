import requests
import json
from pprint import pprint


def getdates(nodeid):
    r = requests.get('http://beehive1.mcs.anl.gov/api/1/nodes/{}/dates?version=2'.format(nodeid.rjust(16, '0')))

    if r.status_code == 200:
        return '2', sorted(r.json()['data'], reverse=True)

    r = requests.get('http://beehive1.mcs.anl.gov/api/1/nodes/{}/dates?version=1'.format(nodeid.rjust(16, '0')))

    if r.status_code == 200:
        return '1', sorted(r.json()['data'], reverse=True)

    return '', []


nodes = requests.get('http://beehive1.mcs.anl.gov/api/nodes').json()
results = []

for node in nodes:
    result = {
        'node_id': node['id'][-12:].lower(),
    }

    version, dates = getdates(node['id'])

    if len(dates) > 0:
        result['data_version'] = version
        result['data_latest'] = dates[0]
    else:
        result['data_version'] = ''
        result['data_latest'] = ''

    pprint(result)
    results.append(result)

with open('../data.json', 'w') as f:
    json.dump(results, f)
