import random
import requests
import time
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}

url = 'https://search.jd.com/Search?keyword=python'


f = open('jdpython.txt',mode='w')

# 请求访问
time.sleep(random.randint(0, 3))  # 控制访问速度
response = requests.get(url, headers=headers)
#print(response.text)
html = response.text

soup = BeautifulSoup(html, 'lxml')

for i in soup.find_all(attrs={'class': 'p-name'}):
    f.write(i.find(name='em').text + '\n')
    f.write("-----------------------\n\n")
exit(1)
