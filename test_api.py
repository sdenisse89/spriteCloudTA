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
		http_post('user/createWithArray',params=[data_user_a])
		# create pets
		http_post('pet',params=data_pet_a)
		http_post('pet',params=data_pet_b)
		http_post('pet',params=data_pet_x)

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
		response_getA = http_get('pet/'+str(data_pet_a.get('id'))).json()
		assertEqual(response_getA.get('code'),		200)
		assertEqual(response_getA.get('status'),	'available')
		
		response_getB = http_get('pet/'+str(data_pet_b.get('id'))).json()
		assertEqual(response_getB.get('code'),		200)
		assertEqual(response_getB.get('status'),	'pending')

		response_getX = http_get('pet/'+str(data_pet_x.get('id'))).json()
		assertEqual(response_getX.get('code'),		200)
		assertEqual(response_getB.get('status'),	'sold')
		
	def test_getpet_nopet(self):
		""" ACTION 2) user requests status of pets that do not exist
		"""
		response_get = http_get('pet/5').json()
		assertEqual(response_get.get('code'),		404)

	def test_orderpet_nologin(self):
		""" ACTION 3) user tries to order a pet without having logged in
		"""
		response_order = http_post('store/order',params=data_order_petA).json()
		assertEqual(response_order.get('code'),		400) #invalid order

	def test_orderpet_login_status(self):
		""" ACTION 4-5-6) user tries to order a pet after having logged in
			an ADMIN can check the order
		"""
		
		# login
		response_login = http_get('user/login',params={ 'username':data_user_a.get('username'),
														'password':data_user_a.get('password')}).json()
		assertEqual(response_login.get('code'),		200) #valid login
		
		# place order
		response_order = http_post('store/order',params=data_order_petA).json()
		assertEqual(response_order.get('code'),		200) #valid order
		# TODO get order-id from response
		orderId = 1
		response_status = http_get('store/order/'+str(orderId)).json()
		assertEqual(response_order.get('code'),		200) #valid
		assertEqual(response_order.get('status'),	'placed') #valid
		
		# logout
		response_logout = http_get('user/logout').json()
		assertEqual(response_logout.get('code'),	200) #valid

class ApiUserMalicious(TestCase):
	""" IMPLEMENTS TESTCASE A_2
		a malicious user tries to collect data of another user
	"""
	def setUp(self):
		""" creates:
			2 users "USER_A", "USER_E"
			3 pets "PET_A" "PET_B" "PET_X" (not required)
		"""
		 create user USER_A
		http_post('user/createWithArray',params=[data_user_a])
		# create user USER_E
		http_post('user/createWithArray',params=[data_user_e])

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
		response_login = http_get('user/login',params={ 'username':data_user_a.get('username'),
														'password':data_user_a.get('password')}).json()
		assertEqual(response_login.get('code'),		200) #valid login
		
		# try and get data
		response_get = http_get('user/'+data_user_a.get('username')).json()
		assertEqual(response_.get('code'),		200) #valid
		# TODO verify data
		
		# logout
		response_logout = http_get('user/logout').json()
		assertEqual(response_logout.get('code'),	200) #valid

	def test_userE_getdata(self):
		""" ACTION 2) user "USER_E" attempts to get data from USER_A
		"""
		response_login = http_get('user/login',params={ 'username':data_user_e.get('username'),
														'password':data_user_e.get('password')}).json()
		assertEqual(response_login.get('code'),		200) #valid login
		
		# try and get data
		response_get = http_get('user/'+data_user_a.get('username')).json()
		assertEqual(response_get.get('code'),		400) #valid
		# TODO verify data
		
		# logout
		response_logout = http_get('user/logout').json()
		assertEqual(response_logout.get('code'),	200) #valid



if __name__ == '__main__':
	pass