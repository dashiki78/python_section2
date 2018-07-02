from bs4 import BeautifulSoup
import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


payload1 = {'key1':'value1', 'key2':'value2'}
payload2 = (('key1','value1'),('key2','value2'))
payload3 = {'some':'nice'}
