# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web

class Handle(object):
    def GET(self):
        try:
            data = web.input()  # 接收微信传来的验证
            if len(data) == 0:  # 判断data里面是否有内容
                return "hello, this is hadle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "kingsh2012" #请按照公众平台官网\基本配置中信息填写
            list = [token, timestamp, nonce] #列表
            list.sort() #排序
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest() # 转为16进制
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:  # 判断是否相等，如果相等则验证通过
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument