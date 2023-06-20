# CONTAINS HELPER FUNCTIONS AND PARAMS
import requests

# The API endpoint
#=========================================================
url = 'https://petstore.swagger.io/v2/'
api_key = 'special-key'

api_headers ={'accept':'application/json','Content-Type':'application/json'}

# PET DATA
#=========================================================
data_pet_a = {
	"id": 1,
	"category": {"id": 0,"name": "dog"
	},
	"name": "PET_A",
	"photoUrls": ["someurl"],
	"tags": [{"id": 0,"name": "string"}],
	"status": "available"
}

data_pet_b = {
	"id": 2,
	"category": {"id": 1,"name": "cat"},
	"name": "PET_B",
	"photoUrls": ["someurl"],
	"tags": [{"id": 0,"name": "string"}],
	"status": "pending"
}

data_pet_x = {
	"id": 10,
	"category": {"id": 2,"name": "mouse"},
	"name": "PET_X",
	"photoUrls": ["someurl"],
	"tags": [{"id": 0,"name": "string"}],
	"status": "sold"
}

# USER DATA
#=========================================================
data_user_a = {
	"id": 1,
	"username": "USER_A",
	"firstName": "UserB",
	"lastName": "A",
	"email": "doglover20@gmail.com",
	"password": "pwA",
	"phone": "stringA",
	"userStatus": 0
}
data_user_e = {
	"id": 1,
	"username": "USER_E",
	"firstName": "UserE",
	"lastName": "E",
	"email": "evilkenievil@yahoo.com",
	"password": "pwE",
	"phone": "stringE",
	"userStatus": 0
}

# ORDER DATA
#=========================================================

data_order_petA = {
	"id": 0,
	"petId": data_pet_a.get('id'),
	"quantity": 0,
	"shipDate": "2023-06-20T19:53:07.829Z",
	"status": "placed",
	"complete": "true"
}

# HELPER FUNCTIONS
#=========================================================

def http_get(req,**kwargs):
	response = requests.get(url+req,headers=api_headers,**kwargs)
	# Print the response
	print('GET: '+req+' - '+str(response)+' // '+response.text)
	return response

def http_post(req,**kwargs):
	response = requests.post(url+req,headers=api_headers,**kwargs)
	print('POST: '+req+' - '+str(response))
	# Print the response
	return response

def http_delete(req,**kwargs):
	response = requests.delete(url+req,headers=api_headers,**kwargs)
	# Print the response
	print('DELETE: '+req+' - '+str(response))
	return response
	
def http_put(req,**kwargs):
	response = requests.put(url+req,headers=api_headers,**kwargs)
	# Print the response
	print('PUT: '+req+' - '+str(response))
	return response