#!/opt/deploy/web_weixin/web_weixin_venv/bin/python
# -*- coding: utf-8 -*-
from vs_5eplay import *
vs = vs_5eplay()
#print(vs.get_html('101.227.68.8:8000'))
#print(vs.get_html('123.56.167.34:7777'))
print(type(vs.organize_team('123.56.167.34:7777')))
print('================================')
print(vs.organize_team('123.56.167.34:7777'))
#print(type(vs.get_player_info('123.56.167.34:7777')))
# a = vs.get_player_info('121.199.61.68:23000')
