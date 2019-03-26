import requests
from bs4 import BeautifulSoup
question  = requests.get('https://www.spoj.com/problems/DIRVS/')
soup = BeautifulSoup(question.content, 'html.parser')
tag_area = soup.find(id='problem-tags')
print(tag_area)
tag_data = tag_area.find_all('a')
print(tag_data)