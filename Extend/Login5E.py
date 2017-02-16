#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys

sys.path.append('../')

from DB.configMySQL import ConfigMySQL
from Util.HttpHeaders import HttpRequestHeader

class Login5E(object):
    def __init__(self):
        self.db = ConfigMySQL()
        self.head = HttpRequestHeader().getHttpRequestHeader()
    
    def login(self, args):
        if self.db.Query5EplayUser(args['username']) != None:
            return "帐号已经登录" # 后期可以做一个 解除帐号 更新帐号 查看帐号
                   
        req = requests.post(url='http://vs.5eplay.com/login',data={'username':args['username'],'password':args['password']},headers=self.head)
        if req.text.encode('utf-8') == '1':
            user_cookie = req.cookies
            cookie = {c.name: c.value for c in user_cookie}
            if len(cookie) == 1:
                insertUser = self.db.Insert5EplayCookie(wxid=args['wxid'],username=args['username'],password=args['password'],cname1='sf_auth',cvalue1=cookie['sf_auth'])
                if insertUser == 1:
                    return "登录成功"
            else:
                return '登录出错cookie出现改变，联系微信公众号作者。'
        else:
            return '帐号或密码错误'