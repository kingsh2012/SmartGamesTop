#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
class ConfigMySQL:
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.password = '1qaz2wsx'
        self.db = 'gamedb'
        self.conn = MySQLdb.connect(host=self.host,port = self.port,user=self.user,passwd=self.password,db =self.db)
        self.cursor = self.conn.cursor()
        
    def Insert5EplayCookie(self,**args):
        SQL = """\
        INSERT INTO `cookie` \
        (`wxid`, `username`, `password`, `cname1`, `cvalue1`) \
        VALUES \
        ("%s", "%s", "%s", "%s", "%s") \
        """ % \
        (args['wxid'],args['username'],args['password'],args['cname1'],args['cvalue1'])
        try:
            InsertLineNum = self.cursor.execute(SQL)
            self.conn.commit()
            return InsertLineNum
        except Exception, e:
            return e
    
    def Query5EplayUser(self,username):
        self.cursor.execute("SELECT username FROM `cookie` WHERE `username`='%s'" % username)
        return self.cursor.fetchone()

    def QueryWxid(self,wxid):
        self.cursor.execute("SELECT wxid FROM `cookie` WHERE `wxid`='%s'" % wxid)
        return self.cursor.fetchone()
    
    def GetCookie(self,wxid):
        self.cursor.execute("SELECT cvalue1 FROM `cookie` WHERE `wxid`='%s'" % wxid)
        return self.cursor.fetchone()