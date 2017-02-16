#!/opt/deploy/web_weixin/web_weixin_venv/bin/python
# -*- coding: utf-8 -*-
import requests,time,json
from bs4 import BeautifulSoup
from init_mysql import *

MySQL = mysql()

class c_player_map:

    def GetHtmlParser(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        }
        res = requests.get(url,headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        # dict_data = json.loads(soup.text) #json 转换 python dict
        return soup
    
    def main(self):
        MillisTimeStamp = int(round(time.time() * 1000)) # 毫秒时间戳
        PlayerMapInfoList = []
        TotalIP = MySQL.getAllServerIP()
        for i in range(len(TotalIP)):
            PlayerMapUrl = 'http://vs.5eplay.com/?mod=live&ip=' + TotalIP[i][0] + '&_=' + str(MillisTimeStamp)
            PlayerMapInfo = self.GetHtmlParser(PlayerMapUrl)
            print(PlayerMapInfo)
            # if len(PlayerMapInfo) == 3:
                # PlayerMapInfoList.append((PlayerMapInfo['cur'].encode('utf-8'),PlayerMapInfo['max'].encode('utf-8'),PlayerMapInfo['map'].encode('utf-8')))
                # print((PlayerMapInfo['cur'].encode('utf-8'),PlayerMapInfo['max'].encode('utf-8'),PlayerMapInfo['map'].encode('utf-8')))
            # else:
                # DelNum = MySQL.DeleteTimeOutServer(TotalIP[i][0])
                # DelNum0[0] += 1
                # DelNum1[1] += 1
        # InsertNum = MySQL.InsertCollect5EDataToPlayerMapTable(PlayerMapInfoList)
        # logging.info("删除总表{0}行;删除用户表{1}行;".format(DelNum0,DelNum1))
        # logging.info("插入用户表{0}行".format(InsertNum))
        # print(PlayerMapInfoList)
    
if __name__=='__main__':
    a = c_player_map()
    a.main()
    # print(MySQL.getAllServerIP())