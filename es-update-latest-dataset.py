#!/usr/bin/env python3
import beehive
import json
import requests
from pprint import pprint


for node in beehive.get_nodes():
    try:
        r = beehive.get_node_data_dates(node['id'])
    except RuntimeError:
        continue

    if len(r['dates']) == 0:
        continue

    data = json.dumps({
        'doc': {
            'dataset_version': r['version'],
            'dataset_latest': max(r['dates']),
        }
    })

    pprint(requests.post('http://localhost:9200/waggle/node/{}/_update'.format(node['id']), data=data).json())
