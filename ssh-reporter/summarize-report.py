import os
import os.path
import re


for filename in os.listdir('reports'):
    report = open(os.path.join('reports', filename)).read()

    print(filename)

    # match = re.search('^Description: (.*)$', report)
    # print('system', match)

    print('wagman', 'yes' if re.search('2341:8037', report) else 'no')
    print('coresense', 'yes' if re.search('2341:003e', report) else 'no')
    print('modem', 'yes' if re.search('1bc7:0021', report) else 'no')
    print('alphasense', 'yes' if re.search('04d8:ffee', report) else 'no')
    print()
