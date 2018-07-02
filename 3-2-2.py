from bs4 import BeautifulSoup
import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session()
# r = s.get("http://httpbin.org/get")
# print(r.status_code)
# print(r.ok)

r = s.get("http://jsonplaceholder.typicode.com/posts/1")
# print(r.text)
print(r.json().values())
print(r.raw)
s.close()
