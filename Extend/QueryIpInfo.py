#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import sys

sys.path.append('../')

from Util.HttpHeaders import HttpRequestHeader

class QueryIpinfo(object):

    def __init__(self):
        self.head = HttpRequestHeader().getHttpRequestHeader()

    def get_Ip_Info(self, userip):
        # return userip
        req = requests.get(url ='http://ip.taobao.com/service/getIpInfo.php',params = userip,headers=self.head)
        rawData = req.text.encode('utf-8')
        jsonData = json.loads(rawData)
        result = "IP:{0}\n来自:{1} {2} {3}\n地区:{4}\n运营商:{5}".format(jsonData['data']['ip'].encode('utf-8'), \
        jsonData['data']['country'].encode('utf-8'), \
        jsonData['data']['region'].encode('utf-8'), \
        jsonData['data']['city'].encode('utf-8'), \
        jsonData['data']['area'].encode('utf-8'), \
        jsonData['data']['isp'].encode('utf-8') \
        )
        return result
    
# QueryIpinfo()
# if __name__ == '__main__':
    # print(QueryIpinfo().get_Ip_Info({'ip':'60.1.13.238'}))