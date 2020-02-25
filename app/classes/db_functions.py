from . db_config import connection

class Functions():
	"""docstring for Functions"""
	def __init__(self):
		
		self.db = connection()
		self.cursor = self.db.cursor(buffered=True, dictionary=True)


	def _closeDb(self):

		self.db.close()
		self.cursor.close()

	def _commitDb(self):

		self.db.commit()

	def _initiateDb(self):
		
		self.db = connection()
		self.cursor = self.db.cursor(buffered=True, dictionary=True)
