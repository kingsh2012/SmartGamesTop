#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, time, json, sys

sys.path.append('../')

from DB.configMySQL import ConfigMySQL
from vs_5eplay import vs_5eplay
from Util.HttpHeaders import HttpRequestHeader

class Web5Eplay(object):
    def __init__(self):
        self.head = HttpRequestHeader().getHttpRequestHeader()
        self.vs = vs_5eplay()
        self.db = ConfigMySQL()
    
    def ChecckWxid(self,wxid):
        return True if self.db.QueryWxid(wxid) != None else False
    
    def ReleaseMatch(self, args):
        if self.ChecckWxid(args['wxid']) != True:
            return "您的微信未登录5E帐号,无法使用5E发送"
        
        cookie = self.db.GetCookie(args['wxid'])
        # print(cookie)
        if self.vs.check_connect(args['ip']) == 1:
            url = 'http://vs.5eplay.com/?mod=vs&action=ajax&op=vspost&ip={0}&password=&about={1}&_{2}'.format(args['ip'],str(args['about']),str(int(round(time.time() * 1000))))
            # return url
            req = requests.get(url, headers=self.head, cookies={'sf_auth':cookie[0]})
            req.encoding = 'utf-8'
            jsonData = json.loads(req.text)
            result = jsonData['alert'].encode('utf-8')
            return '5Eplay'+result
        else:
            return '找不到服务器'

# if __name__ == '__main__':
    # a = Web5Eplay()
    # print a.ReleaseMatch({'wxid':'oK5lzwisZKBNF3DLf4hM1b0shXbE'})
    # print(a.ReleaseMatch(wxid='oK5lzwisZKBNF3DLf4hM1b0shXbE',cookie='b345bh%2F%2Bcmws1ws8ZxzrkzgJebUNYcnvLVhsILO4%2Fy3qHC9GyXDYkeachetE9TFzn5C%2BfiqzrhIJ5J7HovFy91ZlCFU',ip='182.92.122.10:9999',about=0))