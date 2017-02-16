# -*- coding: utf-8 -*-
# filename: handle.py
import reply        #回复
import receive      #接收
import web
import sys
sys.path.append('../')
from UserMsgHandle.UserMsgHandleLogic import MsgLogic

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData) #发送给接收机制 解析
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName # 用户
                fromUser = recMsg.ToUserName # 公众号
                toUserContent = MsgLogic().main(user = toUser, messages = recMsg.Content)
                replyMsg = reply.TextMsg(toUser, fromUser, toUserContent)
                return replyMsg.send()
            else:
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                replyMsg = reply.TextMsg(toUser, fromUser, '您发送的内容非文本信息，暂时不给予处理。')
                return replyMsg.send()
        except Exception, Argment:
            return Argment