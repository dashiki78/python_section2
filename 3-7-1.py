import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeWriteAtt:
    def __init__(self):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome('C:/section3/webdriver/chrome/chromedriver')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:/section3/webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)

    def writeAttendCheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('dashiki78')
        self.driver.find_element_by_name('pw').send_keys('26495538c200')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(30)
        self.driver.get('https://cafe.naver.com/AttendanceView.nhn?search.clubid=11786850&search.menuid=6')
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('cafe_main')
        self.driver.find_element_by_id('cmtinput').send_keys('반갑습니다')
        self.driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/a/img').click()
        time.sleep(3)

    def __del__(self):
        self.driver.quit()
        print("removed driver Object")


if __name__ == '__main__':
    a = NcafeWriteAtt()
    start_time = time.time()
    a.writeAttendCheck()
    print("---Total %s seconds ---" % (time.time()-start_time))
    del a
