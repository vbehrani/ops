#!/usr/bin/env python3
import requests
import subprocess
import json
import time
from pprint import pprint


nodes = requests.get('http://beehive1.mcs.anl.gov/api/nodes').json()
results = []

for node in nodes:
    result = {
        'node_id': node['id'][-12:].lower(),
        'ssh_port': node['port'],
        'ssh_time': time.time(),
    }

    try:
        output = subprocess.check_output("ssh node{} 'echo OK; exit'".format(node['port']), shell=True).decode()
        assert 'OK' in output
        result['ssh_alive'] = True
    except:
        result['ssh_alive'] = False

    pprint(result)
    results.append(result)

with open('../ssh.json', 'w') as f:
    json.dump(results, f)
