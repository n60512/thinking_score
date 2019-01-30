import pymysql


class DBConnection(object):
	"""docstring for DBConnection"""
	def __init__(self):
		super(DBConnection, self).__init__()

		self.connection = pymysql.connect(host='xxx',
		                             user='xxx',
		                             password='xxx',
		                             db='xxx',
		                             charset='utf8mb4',
		                             cursorclass=pymysql.cursors.DictCursor)		
		self.sqlCmd = ""		#	SQL 指令
		self.res = []

		pass

	#-------------------------------------------------------------------------
	#	execute
	#-------------------------------------------------------------------------
	def execute(self):	
		try:
		    with self.connection.cursor() as cursor:
		        cursor.execute(self.sqlCmd)
		        #self.res = cursor.fetchall()
		    self.connection.commit()
		    pass
		finally:
		    pass
		pass

	#-------------------------------------------------------------------------
	#	select
	#-------------------------------------------------------------------------
	def select(self):	
		try:
		    with self.connection.cursor() as cursor:
		        cursor.execute(self.sqlCmd)
		        res = cursor.fetchall()
		    self.connection.commit()
		    pass
		finally:
			return res
			pass
		pass		


	#-------------------------------------------------------------------------
	#	SetCmd
	#-------------------------------------------------------------------------
	def SetCmd(self,qurey):	
		self.sqlCmd = qurey
		pass

	#-------------------------------------------------------------------------
	#	DB Connection Close
	#-------------------------------------------------------------------------
	def ConnClose(self):
		self.connection.close()
		pass

	def GetRes(self):
		return self.res
		pass