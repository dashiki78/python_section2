import sys
import io
from selenium import webdriver
import time
# from selenium.webdriver.chrome.options import Options


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# chrome_options.add_argument('--log-level=3')
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:/section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome('C:/section3/webdriver/chrome/chromedriver')

driver.set_window_size(1920, 1280)
driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login')
time.sleep(7)
driver.implicitly_wait(3)
driver.find_element_by_name('id').send_keys('dashiki78')
driver.implicitly_wait(1)
driver.find_element_by_name('pw').send_keys('26495538c200')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.get('https://cafe.naver.com/AttendanceView.nhn?search.clubid=11786850&search.menuid=6')
driver.implicitly_wait(30)
driver.switch_to_frame('cafe_main')
driver.find_element_by_id('cmtinput').send_keys('반갑습니다')
driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/a/img').click()
time.sleep(3)
