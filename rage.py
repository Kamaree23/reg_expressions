import re

with open('regex_test.txt') as file:
    data = file.readlines()
    for line in data:
        try:
            names = (re.search('[A-Z][a-z]+( [A-Z][a-z]*)? [A-Z][a-z]+', line)).group()
            print(names)
        except:
            print(None)