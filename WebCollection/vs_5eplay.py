# encoding:utf-8
from bs4 import BeautifulSoup
import requests,json,time

class vs_5eplay():

    def get_html(self, server_port):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        }
        url = "http://vs.5eplay.com/details/" + server_port
        res = requests.get(url,headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        return soup
    
    def get_server_info(self, server_port):
        if self.check_connect(server_port) == 1:
            soup = self.get_html(server_port)
            server_info = []
            for li in soup.select('.l')[1].contents[1]:
                if len(str(li).strip()) != 0:
                    server_info.append(str(li).replace('</h3>',':').rstrip('</li>').lstrip('<li><h3>'))
            result = "\n".join(server_info[1:])
        else:
            result = '找不到服务器'
        return result
        
    def get_server_param(self, server_port):
        if self.check_connect(server_port) == 1:
            soup = self.get_html(server_port)
            server_param, server_param_name, server_param_value, result2, result3 = [], [], [], [], []
            for li2 in soup.select('.r li'):
                server_param.append(str(li2).replace('</h5>',' ').rstrip('</li>').lstrip('<li><h5>'))
            for i in server_param[1:]:
                server_param_name.append(i.split(' ')[0])
                server_param_value.append(i.split(' ')[1])
            for i2 in range(len(server_param_name)):
                result2.append(server_param_name[i2]+':'+server_param_value[i2])
            result = "\n".join(result2)
        else:
            result = '找不到服务器'
        return result

    def get_player_info(self, server_port):
        if self.check_connect(server_port) == 1:
            soup = self.get_html(server_port)
            player_info, player_info_name, player_info_time, player_info_score, result2, result3 = [], [], [], [], [], []
            for ul in soup.select('.mt20 li'):
                player_info.append(str(ul).replace('<h4>','').replace('<span>','').rstrip('</span></li>').lstrip('<li><h4>'))
            for i in player_info[2:]:
                player_info_time.append(i.split('</h4>')[0])
                player_info_score.append(i.split('</h4>')[1])
                player_info_name.append(i.split('</h4>')[2])
            num = 1
            for i2 in range(len(player_info_name)):
                num2 = num + i2
                result2.append(str(num2)+'; '+player_info_name[i2]+'; '+player_info_score[i2]+'; '+player_info_time[i2])
            if len(result2) != 0:
                result = "\n".join(result2)
            else:
                result = '服务器暂时没有玩家'
        else:
            result = '找不到服务器'
        return result
        
    def check_connect(self, server_port):
        soup = self.get_html(server_port)
        err = soup.select('.text')
        if len(err) == 1:
            result = 0
        else:
            result = 1
        return result
        
    def organize_team(self, server_port):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            # "Accept-Encoding": "gzip, deflate",
            # "Host": "vs.5eplay.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        }
        cookie = {'__cfduid':'d11887dce9f79962e4e3669824f79f26e1481563385',
            'Hm_lvt_12861524735e59efe36180e8485a6c92':'1482138711,1482139066,1482139976,1482140921',
            'Hm_lpvt_12861524735e59efe36180e8485a6c92':'1482142905',
            '5e_firstvisit':'0',
            'sf_auth':'9f5488HXEgfGK0lSAQf0sqZxyxiciRWkpVuZ%2FxNdT1XSRbv4WHikUqaBCIAUZ4tLVNEsLRov6t4c1tvBfgVmEbPppWc'
        }
        
        if self.check_connect(server_port) == 1:
            # print(headers)

            ip  = server_port.split(':')[0]
            port = server_port.split(':')[1]
            # 毫秒级时间戳
            millis = int(round(time.time() * 1000))
            #   = :
            url = 'http://vs.5eplay.com/?mod=vs&action=ajax&op=vspost&ip='+ ip +'%3A'+ port +'&password=&about=0&_' + str(millis)
            # print(url)
            
            res = requests.Session()
            result_unicode = res.get(url,cookies=cookie,headers=headers)
            result_unicode.encoding = 'utf-8'
            result_str = json.loads(result_unicode.text)
            result = result_str['alert'].encode('utf-8')
        else:
            result = '找不到服务器'
        return result
