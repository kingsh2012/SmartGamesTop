# -*- coding: utf-8 -*-
# filename: receive.py
import xml.etree.ElementTree as ET

def parse_xml(web_data):
    if len(web_data) == 0:      #判断传来的数据内容长度
        return None
    xmlData = ET.fromstring(web_data)   #加载XML字符串
    msg_type = xmlData.find('MsgType').text #得到MsgType子节点下的值
    if msg_type == 'text':
        return TextMsg(xmlData)
    elif msg_type == 'image':
        return ImageMsg(xmlData)
    # elif msg_type == 'voice':
        # return VoiceMsg(xmlData)

class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text               #公众号
        self.FromUserName = xmlData.find('FromUserName').text           #发送人
        self.CreateTime = xmlData.find('CreateTime').text               #时间
        self.MsgType = xmlData.find('MsgType').text                     #信息类型
        self.MsgId = xmlData.find('MsgId').text                         #信息ID

class TextMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Content = xmlData.find('Content').text.encode("utf-8")     #信息内容

class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text
        
# class VoiceMsg(Msg):
    # def __init__(self, xmlData):
        # Msg.__init__(self, xmlData)
        # self.PicUrl = xmlData.find('PicUrl').text
        # self.MediaId = xmlData.find('MediaId').text