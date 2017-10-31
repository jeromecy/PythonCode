import MySQLdb

class DB:
  conn = None

  def connect(self):
    self.conn = MySQLdb.connect(host='unionintokyo.cg6x01smgrfp.ap-northeast-1.rds.amazonaws.com',user='victorcraft',passwd='ilove86415175',db='unionmysql')

  def query(self, sql):
    try:
      cursor = self.conn.cursor()
      cursor.execute(sql)
    except (AttributeError, MySQLdb.OperationalError):
      self.connect()
      cursor = self.conn.cursor()
      cursor.execute(sql)
    return cursor
  def commit(self):
      self.conn.commit()
  def close(self):
      self.conn.close()

      #  def fetchall():
#self.conn.cursor.fetchall()



