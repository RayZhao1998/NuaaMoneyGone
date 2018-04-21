# -*- coding: utf-8 -*-

__author__ = 'arcosx'
__author2__ = 'rayzhao98'

import requests
import threading


class client(object):
    username = ""
    password = ""
    isLogin = 0
    login_url = "https://ucapp.nuaa.edu.cn/wap/login/invalid"
    search_url = "https://app.nuaa.edu.cn/cardhis/wap/default/index"
    cookie = ""
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://app.nuaa.edu.cn/cardhis/wap/default/index',
    }

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login()

    def login(self):
        post_data = {'username': self.username, 'password': self.password}
        login_res = requests.post(self.login_url, data=post_data, headers=self.headers)
        cookies = login_res.cookies
        UUkey = 'UUkey=' + cookies['UUkey'] + '; '
        vjuid = 'vjuid=' + cookies['vjuid'] + '; '
        vjvd = 'vjvd=' + cookies['vjvd'] + '; '
        vt = 'vt=' + cookies['vt']
        header_cookie = UUkey + vjuid + vjvd + vt
        self.headers['Cookie'] = header_cookie
        self.isLogin = 1
        return 1

    def search(self, begin_date, end_date):
        if self.isLogin == 0:
            return
        payload = "sdate=" + begin_date + "&edate=" + end_date
        res = requests.post(self.search_url, headers=self.headers, data=payload)
        return res.json()

def getChargeMonthly(data):
    charge = 0
    for date in data:
        for item in data[date]:
            if item['type'] == "充值":
                charge += float(item["xfje"])
    return charge
    
def getSpendMonthly(data):
    spend = 0
    for date in data:
        for item in data[date]:
            if item['type'] == "消费":
                spend += float(item["xfje"])
    return spend    

def getIn(data):
        for date in data:
            print(date)
            for item in data[date]:
                print("在" + item['toname'] + item['type'] + "了" + item['xfje'] + '元')

def getDaysInMonth(month):
    return {
        '1':  '31',
        '2':  '28',
        '3':  '31',
        '4':  '30',
        '5':  '31',
        '6':  '30',
        '7':  '31',
        '8':  '31',
        '9':  '30',
        '10': '31',
        '11': '30',
        '12': '31',
    }.get(month, 'error')

def getData(begin_date, end_date):
    data = test.search(begin_date=begin_date, end_date=end_date)['d']
    print(begin_date[5:7])
    print(round(getChargeMonthly(data), 2))
    print(round(getSpendMonthly(data), 2))

if __name__ == '__main__':
    
    test = client(username='161610336', password='133555')
    date = "2017-"
    for month in range(1, 13):
        if month < 10:
            monthString = '0' + str(month)
        else:
            monthString = str(month)
        begin_date = date + monthString + '-01' 
        end_date = date + monthString + '-' + getDaysInMonth(str(month))
        t = threading.Thread(target=getData(begin_date, end_date), name="getDataThread")
        t.start()
        t.join()
        
    # print(test.search(begin_date='2018-04-01', end_date='2018-04-03')['d'].count)
    # getIn(test.search(begin_date='2018-04-01', end_date='2018-04-03')['d'])
    
    
