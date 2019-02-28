import requests
import os
import sys
import pandas as pd
from tabulate import tabulate
from pyfiglet import Figlet
from bs4 import BeautifulSoup

def progbar(curr, total, full_progbar):
    frac = curr/total
    filled_progbar = round(frac*full_progbar)
    print('\r', '#'*filled_progbar + '-'*(full_progbar-filled_progbar), '[{:>7.2%}]'.format(frac), end='')

os.system('clear')

f = Figlet(font='slant')
print(f.renderText('SPOJ SUMMARIZER'))

username = input("What is your spoj handle? ")
print()
page = requests.get("https://www.spoj.com/users/"+username)


soup = BeautifulSoup(page.content, 'html.parser')

profile = soup.find(id='user-profile-left')

profile_stats = profile.find_all('p')
stats=[]
for i in profile_stats:
    stats.append(i.get_text())
print('Welcome ',username)
print(stats[3])
print(stats[2])
print(stats[1])
print(stats[0])
print('Analyzing your performance...')

problem_data = soup.find(class_='table-condensed')
problems = problem_data.find_all('a')
problem_codes = []
for i in problems:
    problem_codes.append(i.get_text())
maxp=len(problem_codes)
cc=1
topics={}
topics['#untagged']=0

problem_codes = [x for x in problem_codes if x!='']

for code in problem_codes:
    question  = requests.get('https://www.spoj.com/problems/'+code)
    soup = BeautifulSoup(question.content, 'html.parser')
    tag_area = soup.find(id='problem-tags')
    tag_data = tag_area.find_all('a')
    tags=[]
    for e in tag_data:
        tags.append(e.get_text())
    for tag in tags:
        if tag in topics:
            topics[tag]+=1
        else:
            topics[tag]=1
    if len(tags)==0:
        topics['#untagged']+=1
    progbar(cc,maxp,70)  
    cc+=1
    sys.stdout.flush()
progbar(maxp,maxp,70)
print()
tag_d = []
count_d = []
for tag,count in topics.items():
    tag_d.append(tag[1:])
    count_d.append(count)

df = pd.DataFrame(
    {
        'Topics':tag_d,
        'No of problems solved':count_d
    }
)

print(tabulate(df, headers='keys', tablefmt='psql'))