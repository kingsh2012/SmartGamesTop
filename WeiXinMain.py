#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web, sys, logging

sys.path.append('./')

from WeChatHandle.Handle import Handle

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                filename='./debug.log',
                filemode='a')

web.config.debug = True

urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()