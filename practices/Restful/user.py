
class User():

	def __init__(self, id, username, password):
		self.id = id
		self.username = username
		self.password = password

	def __str__(self):
		return 'User ID is: {}'.format(self.id)