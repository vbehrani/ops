import requests


def getdates(nodeid):
    r = requests.get('http://beehive1.mcs.anl.gov/api/1/nodes/{}/dates?version=2'.format(nodeid))

    if r.status_code == 200:
        return 'v2', sorted(r.json()['data'], reverse=True)

    r = requests.get('http://beehive1.mcs.anl.gov/api/1/nodes/{}/dates?version=1'.format(nodeid))

    if r.status_code == 200:
        return 'v1', sorted(r.json()['data'], reverse=True)

    return '', []


r = requests.get('http://beehive1.mcs.anl.gov/api/nodes')
nodes = r.json()

for node in nodes:
    version, dates = getdates(node['id'])

    if len(dates) > 0:
        print(','.join([node['id'], version, dates[0]]))
    else:
        print(','.join([node['id'], version, '']))
