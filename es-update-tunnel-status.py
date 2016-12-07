#!/usr/bin/env python3
import requests
import json
import beehive
from datetime import datetime
from pprint import pprint

for node in beehive.get_nodes():
    ssh_alive = beehive.get_tunnel_status(node['ssh_port'])

    if ssh_alive:
        data = json.dumps({
            'doc': {
                'ssh_last_alive': datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
            }
        })

        pprint(requests.post('http://localhost:9200/waggle/node/{}/_update'.format(node['id']), data=data).json())
