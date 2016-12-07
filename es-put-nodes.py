#!/usr/bin/env python3
import requests
import json
from pprint import pprint


r = requests.get('http://beehive1.mcs.anl.gov/api/nodes')
assert r.status_code == 200
nodes = r.json()

# Consider defining index and mapping here too?
# This will help with later datatype conflicts.

for node in nodes:
    data = {
        'id': node['id'][-12:].lower(),
        'name': node['name'],
        'description': node['description'],
        'location': node['location'],
        'ssh_port': node['port'],
    }

    url = 'http://localhost:9200/waggle/node/{}'.format(data['id'])
    pprint(requests.put(url, data=json.dumps(data)).json())
