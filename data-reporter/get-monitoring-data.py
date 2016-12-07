import requests
import subprocess
from datetime import datetime


def sortkey(node):
    if 'coresense:3' in node['plugins']:
        return node['plugins']['coresense:3']['last']
    else:
        return ''


entries = requests.get('http://beehive1.mcs.anl.gov/api/nodes').json()
nodes = {}

for entry in entries:
    nodes[entry['id'][4:].lower()] = entry
    del entry['id']
    entry['plugins'] = {}

output = subprocess.check_output('./get-monitoring-data.sh', shell=True)

for line in output.decode().splitlines():
    node, plugin, epoch_second = line.strip().split('|')
    nodes[node]['plugins'][plugin] = {
        'last': str(datetime.fromtimestamp(float(epoch_second)))
    }

for nodeid, data in nodes.items():
    try:
        print(data['plugins']['coresense:3']['last'], nodeid, data['name'], data['description'], data['port'])
    except:
        pass
