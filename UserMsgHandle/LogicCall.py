#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys 

sys.path.append('../')

from Extend.Login5E import Login5E
from Extend.vs_5eplay import vs_5eplay # 这个写的还是不太好 有机会换成lxml xpath
from Extend.Send5Eplay import Web5Eplay
from Extend.SendR3gogogo import WebR3gogogo
from Extend.QueryIpInfo import QueryIpinfo

class call(object):
    def __init__(self):
        self.login5e = Login5E()
        self.vs = vs_5eplay()
        self.s5e = Web5Eplay()
        self.sr3 = WebR3gogogo()
        self.QueryIpinfo = QueryIpinfo()
    
    def getIpInfo(self, **ip):
        return self.QueryIpinfo.get_Ip_Info(ip)
        # return ip
    
    def getServerParams(self,ip):
        return self.vs.get_server_param(ip)
    
    def getServerInfo(self,ip):
        return self.vs.get_server_info(ip)
    
    def getServerPlayers(self,ip):
        return self.vs.get_player_info(ip)
    
    def sendMatchInfoTo5E(self, **args):
        return self.s5e.ReleaseMatch(args)
        
    def sendMatchInfoToR3(self, **args):
        return self.sr3.ReleaseMatch(args)
    
    def postLogin(self,**args):
        return self.login5e.login(args)