#!/opt/deploy/web_weixin/web_weixin_venv/bin/python
# -*- coding: utf-8 -*-
import requests,time,json
from bs4 import BeautifulSoup
from init_mysql import *

MySQL = mysql()

class collection:

    def GetHtmlParser(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        }
        res = requests.get(url,headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        dict_data = json.loads(soup.text) #json 转换 python dict
        return dict_data['data']
        

    def PageRawDataList(self):
        RawDataList = []
        MillisTimeStamp = int(round(time.time() * 1000)) # 毫秒时间戳
        for PageNum in range(1,2):  # 1到5页数据
            PageUrl = 'http://vs.5eplay.com/?mod=vs&action=ajax&op=vslist&vsquery=game:1&page=' + str(PageNum) + '&_=' + str(MillisTimeStamp)
            RawData = self.GetHtmlParser(PageUrl)
            for i in range(0,30):
                if isinstance(RawData[i]['hostname'],unicode) == True:
                    RawDataList.append((
                    RawData[i]['game'].encode('utf-8'),
                    RawData[i]['uid'].encode('utf-8'),
                    RawData[i]['username'].encode('utf-8'),
                    RawData[i]['ip'].encode('utf-8'),
                    RawData[i]['password'].encode('utf-8'),
                    RawData[i]['fpassword'].encode('utf-8'),
                    RawData[i]['cur'].encode('utf-8'),
                    RawData[i]['max'].encode('utf-8'),
                    RawData[i]['map'].encode('utf-8'),
                    RawData[i]['hostname'].encode('utf-8'),
                    RawData[i]['prov'].encode('utf-8'),
                    RawData[i]['prov_en'].encode('utf-8'),
                    RawData[i]['prov_id'].encode('utf-8'),
                    RawData[i]['network'].encode('utf-8'),
                    RawData[i]['anti'].encode('utf-8'),
                    RawData[i]['about'].encode('utf-8'),
                    RawData[i]['ftime'].encode('utf-8'),
                    RawData[i]['live']))
                else:
                    RawDataList.append((
                    RawData[i]['game'].encode('utf-8'),
                    RawData[i]['uid'].encode('utf-8'),
                    RawData[i]['username'].encode('utf-8'),
                    RawData[i]['ip'].encode('utf-8'),
                    RawData[i]['password'].encode('utf-8'),
                    RawData[i]['fpassword'].encode('utf-8'),
                    RawData[i]['cur'].encode('utf-8'),
                    RawData[i]['max'].encode('utf-8'),
                    RawData[i]['map'].encode('utf-8'),
                    'UnknownServerName',
                    RawData[i]['prov'].encode('utf-8'),
                    RawData[i]['prov_en'].encode('utf-8'),
                    RawData[i]['prov_id'].encode('utf-8'),
                    RawData[i]['network'].encode('utf-8'),
                    RawData[i]['anti'].encode('utf-8'),
                    RawData[i]['about'].encode('utf-8'),
                    RawData[i]['ftime'].encode('utf-8'),
                    RawData[i]['live']))
        return RawDataList
        
    def main(self):
        LineNum,LineNum1,LineNum2 = 0,0,0
        RawDataList = self.PageRawDataList() #网页采集出的原始数据
        for i in range(len(RawDataList)):
            RawData_uid, RawData_username, RawData_ip, RawData_ftime, RawData_about = RawDataList[i][1], RawDataList[i][2], RawDataList[i][3], RawDataList[i][16], RawDataList[i][15] # 网页数据提取 变量
            # 判断再网页上采集来的IP地址，在总表内是否存在？
            if MySQL.Check5EServerIPExist(RawData_ip) == 0: # 不存在
                LineNum = MySQL.InsertCollect5EDataToTotalTable(RawDataList[i]) # 插入总表
                # print(RawDataList[i])
                LineNum1 = MySQL.InsertCollect5EDataToUsersTable((RawData_ip, RawData_uid, RawData_username, RawData_ftime, RawData_about)) # 部分数据插入用户表
                LineNum = LineNum+1
                LineNum1 = LineNum1+1
                # print(LineNum)
                # print('不存在')
            else:  # 存在
                DB_raw_uid, DB_raw_ftime = MySQL.QueryUserTableIPInfo(RawData_ip)[1], MySQL.QueryUserTableIPInfo(RawData_ip)[3] # 数据库数据提取 变量
                # 判断采集到的UID和fitme是否与用户表内的相等
                if DB_raw_uid != RawData_uid and DB_raw_ftime != RawData_ftime:
                    # print('存在,但用户不一样,网页:{0};DB:{1};IP:{2}'.format(RawData_uid,DB_raw_uid,RawData_ip))
                    LineNum2 = MySQL.InsertCollect5EDataToUsersTable((RawData_ip, RawData_uid, RawData_username, RawData_ftime, RawData_about))# 插入用户表
                    LineNum2 = LineNum2+1
                # else:
                    # print("存在,用户一样")
        logging.info("查找总表内IP不存在;插入总表{0}行;插入用户表{1}行;".format(LineNum,LineNum1))
        logging.info("查找总表内IP存在;发布用户不同;插入用户表{0}行;".format(LineNum2))

if __name__=='__main__':
    collect = collection()
    while 1:
        collect.main()
        time.sleep(300)
