import MySQLdb

class DB:
  conn = None

  def connect(self):
    self.conn = MySQLdb.connect(host='ec2union-cluster.cluster-c8tmmdxu2zy8.us-east-1.rds.amazonaws.com',user='victorcraft',passwd='ilove86415175',db='iosunion')

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



