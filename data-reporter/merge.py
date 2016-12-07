import requests
import re

dates = {}

fs = re.compile(',')

for f in map(fs.split, map(str.strip, open('dates.csv'))):
    dates[f[0]] = f

r = requests.get('http://beehive1.mcs.anl.gov/api/nodes')
nodes = r.json()

for node in nodes:
    f = dates[node['id']]
    last = f[2]
    version = f[1]
    print(','.join([last, version, node['id'], node['name'], node['description'], node['location'], str(node['port'])]))
