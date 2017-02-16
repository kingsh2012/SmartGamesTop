#!/opt/deploy/web_weixin/web_weixin_venv/bin/python
# -*- coding: utf-8 -*-
import MySQLdb,logging,sys

# logging.basicConfig(level=logging.DEBUG,
                # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                # datefmt='%Y-%m-%d %H:%M:%S',
                # filename='./collection_web.log',
                # filemode='a')

class mysql:
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.password = '1qaz2wsx'
        self.db = 'gamedb'
        self.conn = MySQLdb.connect(host=self.host,port = self.port,user=self.user,passwd=self.password,db =self.db)
        self.cursor = self.conn.cursor()
    
    # 关闭数据库
    def CloseDB(self):
        self.conn.close()

    # 检测IP是否在collection_total_data表内存在 
    # 存在1 不存在0
    def Check5EServerIPExist(self, ip): 
        self.cursor.execute("SELECT * FROM `collection_total_data` WHERE `raw_ip` = '%s'" % ip)
        Result = self.cursor.fetchone()
        if Result == None:
            return 0
        else:
            return 1
    
    # 查询·用户·表ip信息
    # return tupl
    def QueryUserTableIPInfo(self, ip): 
        self.cursor.execute("SELECT `from`, `new_uid`, `new_username`, `new_ftime` FROM `collection_users` WHERE `ip` = '%s' ORDER BY `id` DESC" % ip)
        Result = self.cursor.fetchone()
        return Result
    
    # 查询·总表·IP信息
    def QueryServerIPInfo(self, ip):
        self.cursor.execute("SELECT `from`, `raw_uid`, `raw_username`, `raw_ftime` FROM `collection_total_data` WHERE `raw_ip` = '%s'" % ip)
        Result = self.cursor.fetchone()
        return Result
        
    # 获取所有IP
    def getAllServerIP(self):
        self.cursor.execute("SELECT `raw_ip` FROM `collection_total_data`")
        Result = self.cursor.fetchall()
        return Result

    # 插入采集到的数据到总表
    def InsertCollect5EDataToTotalTable(self,Data):
        SQL = """ \
        INSERT INTO `collection_total_data`(raw_game, raw_uid, raw_username, raw_ip, \
        raw_password, raw_fpassword, raw_cur, raw_max, raw_map, raw_hostname, \
        raw_prov, raw_prov_en, raw_prov_id, raw_network, raw_anti, raw_about, raw_ftime, raw_live) \
        VALUES \
        ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % \
        Data
        
        try:
            InsertLineNum = self.cursor.execute(SQL)
            self.conn.commit()
            return InsertLineNum
        except Exception, e:
            self.conn.rollback()
            logging.error('Function:{0}; Exception:{1};Data:{2}'.format(sys._getframe().f_code.co_name,e,Data))
    
    # 插入采集到的数据到用户表
    def InsertCollect5EDataToUsersTable(self,Data):
        SQL = """\
        INSERT INTO `collection_users` \
        (`ip`, `new_uid`, `new_username`, `new_ftime`, `new_about`) \
        VALUES \
        ('%s','%s',"%s",'%s','%s')""" % \
        Data
        
        try:
            InsertLineNum = self.cursor.execute(SQL)
            self.conn.commit()
            return InsertLineNum
        except Exception, e:
            self.conn.rollback()
            logging.error('Function:{0}; Exception:{1};Data:{2}'.format(sys._getframe().f_code.co_name,e,Data))
    
    def DeleteTimeOutServer(self,ip):
        try:
            DelUserTableNum = self.cursor.execute("DELETE FROM `collection_users WHERE `ip` = {0}".format(ip))
            self.conn.commit()
            DelTotalTableNum = self.cursor.execute("DELETE FROM `collection_total_data WHERE `raw_ip` = {0}".format(ip))
            self.conn.commit()
            return tupl(DelTotalTableNum,DelUserTableNum)
        except Exception, e:
            self.conn.rollback()
            logging.error('Function:{0}; Exception:{1};Data:{2}'.format(sys._getframe().f_code.co_name,e,ip))
    
        
    
    def InsertCollect5EDataToPlayerMapTable(self,Data):
        SQL = """INSERT INTO `collection_player_map`(`ip`, `new_cur`, `new_max`, `new_map`) 
        VALUES (%s,%s,%s,%s)"""
        try:
            InsertLineNum = self.cursor.executemany(SQL, Data)
            self.conn.commit()
            return InsertLineNum
        except Exception, e:
            self.conn.rollback()
            logging.error('Function:{0}; Exception:{1};Data:{2}'.format(sys._getframe().f_code.co_name,e,Data))
    