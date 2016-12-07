#!/usr/bin/env python3
import requests
import json

data = json.dumps({
    'mappings': {
        'node': {
            '_all': {'enabled': False},
            'properties': {
                'node_id': {'type': 'keyword'},
                'name': {'type': 'text'},
                'description': {'type': 'text'},
                'location': {'type': 'text'},
                'ssh_port': {'type': 'integer'},
                'ssh_last_alive': {'type': 'date'}
            }
        }
    }
})

print(requests.put('http://localhost:9200/test?pretty', data=data).json())
