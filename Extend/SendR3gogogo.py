#!/opt/deploy/web_weixin/web_weixin_venv/bin/python
# -*- coding: utf-8 -*-
import requests, json, re, sys
from bs4 import BeautifulSoup

sys.path.append('../')

from Util.HttpHeaders import HttpRequestHeader

class WebR3gogogo(object):
    def __init__(self):
        self.head = HttpRequestHeader().getHttpRequestHeader()
        self.about = {
            0 : 'R7R3',
            1 : '来支素质娱乐队',
            2 : '来支训练队',
            3 : '来不跑的兵',
            4 : '来个素质强兵',
            5 : 'OP寻素质CSER组队',
            6 : '来2连',
            7 : '来M6，观察作弊',
            8 : '有M6，再来一个强兵',
            9 : '进来练练枪',
        }
    
    def ReleaseMatch(self, args):
            url = "http://r3gogogo.com/index.php/Home-Index-serverCreate.html"
            
            params =  {
                'y_server':args['ip'],
                'y_info':self.about[args['about']],
            }
            # print(params)
            res = requests.post(url,headers=self.head,data=params)
            res.encoding = 'utf-8'
            
            # print(res.text.encode('utf-8'))
            reData = re.search(r'{"id":\d{0,1}}',res.text.encode('utf-8'))
            
            if reData:
                # print(reData.group())
                jsonData = json.loads(reData.group())
                # print(jsonData['id'])
                if int(jsonData['id']) == 4:
                    return 'R3gogogo约战信息发送成功!'
                elif int(jsonData['id']) == 3:
                    return 'R3gogogo约战信息发送失败!'
                else:
                    return 'R3gogogo返回未知;返回值{0}'.format(reData.group())
            else:
                soup = BeautifulSoup(res.text,'html.parser')
                for i in soup.select('.error'):
                    return i.text.encode('utf-8')
                    
# if __name__ == '__main__':
    # a = WebR3gogogo()
    # print(a.ReleaseMatch(ip='182.92.122.10:9999',about=3))