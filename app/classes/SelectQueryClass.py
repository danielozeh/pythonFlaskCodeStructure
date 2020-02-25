from .db_functions import Functions


DBFunctionsClass = Functions()

class SelectQueryClass():
	"""docstring for SelectQueryClass"""
	# def __init__(self, arg):
	# 	super(SelectQueryClass, self).__init__()
	# 	self.arg = arg


	def _getAllusers(self):

		try:
			query = "SELECT username, login_ip, last_login FROM Users_Login"

			DBFunctionsClass._initiateDb()

			DBFunctionsClass.cursor.execute(query)

			data = DBFunctionsClass.cursor.fetchall()

			if data:

				return data

			else:

				return False

		except Exception as e:
			return str(self.traceback.format_exc())
			raise e
		finally:

			DBFunctionsClass._closeDb()

	def _findUserByUsername(self, username):

		try:
			query = "SELECT username FROM Users_Login WHERE username = '%s'" %(username)

			DBFunctionsClass._initiateDb()

			DBFunctionsClass.cursor.execute(query)

			data = DBFunctionsClass.cursor.fetchone()

			if data:

				return data

			else:

				return False

		except Exception as e:
			return str(self.traceback.format_exc())
			raise e
		finally:

			DBFunctionsClass._closeDb()