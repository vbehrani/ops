import fileinput
import requests


for line in map(str.strip, fileinput.input()):
    r = requests.post('http://localhost:8080/', data=line)
    print(line)
