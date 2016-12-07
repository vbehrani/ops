#!/usr/bin/env python3
import requests

print(requests.get('http://localhost:9200/_cat/indices').text)
