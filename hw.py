import re

with open('names.txt') as file:
    data = file.readlines()
    for line in data:
        try:
            twitter = (re.search(r'\B@[a-zA-Z0-9]+', line)).group()
            first = (re.search('\s(?P[A-Z][a-z]+)', line)).group('first')
            last = (re.search('[A-Z][a-z]+', line)).group()
            f_l_t = f'{first} {last} / {twitter}\n'
            print(f_l_t)
        except:
            continue
