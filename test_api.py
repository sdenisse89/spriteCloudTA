from test_utils import *
from unittest import TestCase

class ApiUserOrder(TestCase):
	""" implements TEST A_1
		STORY: valid user browses a list of available pets and selects one to order
	"""
	def setUp(self):
		""" creates:
			1 user "USER_A"
			3 pets "PET_A" "PET_B" "PET_X"
		"""

		# create user USER_A
		http_post('user/createWithArray',data=data_user_a)
		# create pets
		http_post('pet',data=data_pet_a)
		http_post('pet',data=data_pet_b)
		http_post('pet',data=data_pet_x)

	def tearDown(self):
		""" cleans up all users,pets
			logs out of the system
		"""
		# delete users
		http_delete('user/'+str(data_user_a.get('username')))
		# delete pets
		http_delete('pet/'+str(data_pet_a.get('id')))
		http_delete('pet/'+str(data_pet_b.get('id')))
		http_delete('pet/'+str(data_pet_x.get('id')))

	def test_getpet_nologin(self):
		""" ACTION 1) user requests status of pets without login
		"""
		response_getA = http_get('pet/'+str(data_pet_a.get('id')))
		self.assertEqual(response_getA.status_code,		200,				'could not get data of PET_A')
		self.assertEqual(response_getA.json().get('status'),	'available', 		'PET_A has wrong status')
		
		response_getB = http_get('pet/'+str(data_pet_b.get('id')))
		self.assertEqual(response_getB.status_code,		200,				'could not get data of PET_B')
		self.assertEqual(response_getB.json().get('status'),	'pending', 			'PET_B has wrong status')

		response_getX = http_get('pet/'+str(data_pet_x.get('id')))
		self.assertEqual(response_getX.status_code,		200,				'could not get data of PET_X')
		self.assertEqual(response_getB.json().get('status'),	'sold', 			'PET_X has wrong status')
		
	def test_getpet_nopet(self):
		""" ACTION 2) user requests status of pets that do not exist
		"""
		response_get = http_get('pet/5')
		self.assertEqual(response_get.status_code,		404, 				'got wrong code for invalid pet')

	def test_orderpet_nologin(self):
		""" ACTION 3) user tries to order a pet without having logged in
		"""
		response_order = http_post('store/order',data=data_order_petA)
		self.assertEqual(response_order.status_code,		400, 			'order should have been rejected') #invalid order

	def test_orderpet_login_status(self):
		""" ACTION 4-5-6) user tries to order a pet after having logged in
			an ADMIN can check the order
		"""
		
		# login
		response_login = http_get('user/login',data={ 'username':data_user_a.get('username'),
														'password':data_user_a.get('password')}).json()
		self.assertEqual(response_login.get('code'),		200, 			'login should have passed') #valid login
		
		# place order
		response_order = http_post('store/order',data=data_order_petA).json()
		self.assertEqual(response_order.get('code'),		200, 			'order should have been successful') #valid order
		# TODO get order-id from response
		orderId = 1
		response_status = http_get('store/order/'+str(orderId)).json()
		self.assertEqual(response_order.get('code'),		200, 			'get order status failed') #valid
		self.assertEqual(response_order.get('status'),	'placed',  			'order status is wrong') #valid
		
		# logout
		response_logout = http_get('user/logout').json()
		self.assertEqual(response_logout.get('code'),	200, 				'logout failed') #valid

class ApiUserMalicious(TestCase):
	""" IMPLEMENTS TESTCASE A_2
		a malicious user tries to collect data of another user
	"""
	def setUp(self):
		""" creates:
			2 users "USER_A", "USER_E"
			3 pets "PET_A" "PET_B" "PET_X" (not required)
		"""
		# create user USER_A
		http_post('user/createWithArray',data=data_user_a)
		# create user USER_E
		http_post('user/createWithArray',data=data_user_e)

	def tearDown(self):
		""" cleans up all users,pets
			logs out of the system
		"""
		# delete users
		http_delete('user/'+str(data_user_a.get('username')))
		http_delete('user/'+str(data_user_e.get('username')))

	def test_userA_getdata(self):
		""" ACTION 1) user "USER_A" requests their own data (valid)
		"""
		response_login = http_get('user/login',data={ 'username':data_user_a.get('username'),
														'password':data_user_a.get('password')})
		self.assertEqual(response_login.status_code,		200, 'expected valid login for user USER_A') #valid login
		
		# try and get data
		response_get = http_get('user/'+data_user_a.get('username'))
		self.assertEqual(response_get.status_code,		200, 'USER_A could not get their own data') #valid
		# TODO verify data
		
		# logout
		response_logout = http_get('user/logout')
		self.assertEqual(response_logout.status_code,	200, 'logout failed') #valid

	def test_userE_getdata(self):
		""" ACTION 2) user "USER_E" attempts to get data from USER_A
		"""
		response_login = http_get('user/login',data={	'username':data_user_e.get('username'),
														'password':data_user_e.get('password')})
		self.assertEqual(response_login.status_code,		200, 'expected valid login for user USER_E') #valid login
		
		# try and get data
		response_get = http_get('user/'+data_user_a.get('username'))
		self.assertEqual(response_get.status_code,		400, 'USER_E could get data from USER_A') #valid
		# TODO verify data
		
		# logout
		response_logout = http_get('user/logout').json()
		self.assertEqual(response_logout.status_code,	200, 'logout failed') #valid



if __name__ == '__main__':
	pass