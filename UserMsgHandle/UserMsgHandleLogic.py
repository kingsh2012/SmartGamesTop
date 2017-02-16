#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from HelpMessages import *
from LogicCall import call

class MsgLogic(object):
    def __init__(self): 
        self.LoginHelp = LoginHelp()
        self.ServerHelp = ServerHelp()
        self.PlatformHelp = PlatformHelp()
        self.PlatformR3GOHelp = PlatformR3GOHelp()
        self.PlatformVS5EHelp = PlatformVS5EHelp()
        self.ErrInfo = {
        0:'命令长度错误',
        1:'您输入的IP格式有错误\nCS服务器IP格式:\n192.168.1.1:27015\n用户IP格式:\n192.168.1.1',
        2:'您输入的"发布参数"不正确',
        3:'您输入的"CS服务器IP"不正确',
        4:'您输入的第一个参数不正确\n可能是"CS服务器IP"格式错误\n可是是中文错别字',
        }
        self.call = call()

    def helpInfo(self):
        return self.LoginHelp + self.ServerHelp + self.PlatformHelp +'输入"发布参数"获取相关信息'
    
    def main(self, **args):
        wxId, userMsg = args['user'], args['messages'].split()
        
        if len(userMsg) not in [1,2,3]:
            return self.ErrInfo[0]

        if len(userMsg) == 1 and userMsg[0] in ['h','H','发布参数']: #单参数
        
            if userMsg[0] == '发布参数':
                return self.PlatformVS5EHelp + self.PlatformR3GOHelp
                
            elif userMsg[0] == 'h' or userMsg[0] == 'H':
                return self.helpInfo()
                
        elif len(userMsg) == 2 and userMsg[1] in ['参数', '信息', '玩家', '5e', 'r3', '5E', 'R3', 'ip', 'IP']: # 双参数
            ip, param = userMsg[0], userMsg[1]
            userIp = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ip)
            
            serverIp = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,9}',ip)
            
            if userIp and param == 'ip' or param == 'IP': # 这个位置的匹配不太好，192.168.1.1:27015 也会匹配成True 所有使用goup函数
                return self.call.getIpInfo(ip=userIp.group())
                # return userIp.group()
                
            else:
            
                if serverIp and param == '参数':
                    return self.call.getServerParams(ip)
                    
                elif serverIp and param == '信息':
                    return self.call.getServerInfo(ip)
                    
                elif serverIp and param == '玩家':
                    return self.call.getServerPlayers(ip)
                    
                elif serverIp and param == '5e' or param == '5E':
                    return self.call.sendMatchInfoTo5E(wxid=wxId,ip=ip,about=0)
                    
                elif serverIp and param == 'r3' or param == 'R3':
                    return self.call.sendMatchInfoToR3(ip=ip,about=0)
                    
                else:
                    return self.ErrInfo[3]
        elif len(userMsg) == 3 and userMsg[0] in ['登陆5e','登陆5E']:
            user5E, pwd5E = userMsg[1], userMsg[2]
            return self.call.postLogin(wxid=wxId,username=user5E,password=pwd5E)
                
        elif len(userMsg) == 3: # 三参数
            serip, web, param = userMsg[0], userMsg[1], userMsg[2]
            serverIp = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,9}',serip)
            if serverIp and param not in ['0','1','2','3','4','5','6','7','8','9']:
                return self.ErrInfo[2]

            if serverIp and web == '5e' or web == '5E':
                return self.call.sendMatchInfoTo5E(wxid=wxId,ip=serip,about=int(param))
                
            elif serverIp and web == 'r3' or web == 'R3':
                return self.call.sendMatchInfoToR3(ip=serip,about=int(param))
                
            else:
            
                return self.ErrInfo[4]
        else:
            return '请输入h查看具体使用方法'