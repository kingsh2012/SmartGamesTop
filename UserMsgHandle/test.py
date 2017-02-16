#!/usr/bin/env python
# -*- coding: utf-8 -*-

from LogicCall import call

class a(object):
    def __init__(self):
        self.call = call()
    
    def main(self):
        print('a')
        
if __name__=='__main__':
    b = a()
    b.main()