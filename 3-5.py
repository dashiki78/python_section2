from bs4 import BeautifulSoup
import sys
import io
import requests
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

URL = 'https://www.wishket.com/accounts/login/'
ua = UserAgent()

with requests.Session() as s:
    s.get(URL)
    LOGIN_INFO = {
        'identification' : 'dashiki',
        'password' : 'c20026495538',
        'csrfmiddlewaretoken' : s.cookies['csrftoken'],

    }
    # print (s.cookies['csrftoken'])
    # print (s.headers)
    response = s.post(URL, data=LOGIN_INFO, headers={'User-Agent':str(ua.chrome), 'referer':'https://www.wishket.com/accounts/login/'})
    # print (response.text)
    if response.status_code == 200 and response.ok :
        soup = BeautifulSoup(response.text, 'html.parser')
        projectList = soup.select("table.table-responsive > tbody > tr")
        for i in projectList:
            print (i.text)
            print(i.find('th').text, i.find('td').text)
