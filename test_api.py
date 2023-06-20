import requests

# The API endpoint
url = 'https://petstore.swagger.io/v2/'

def http_get(req,**kwargs):
	response = requests.get(url+req,**kwargs)
	# Print the response
	return response

def http_post(req,**kwargs):
	response = requests.post(url+req,**kwargs)
	print(response.text)
	# Print the response
	return response

def http_delete(req,**kwargs):
	response = requests.delete(url+req,**kwargs)
	# Print the response
	return response
	
def http_put(req,**kwargs):
	response = requests.put(url+req,**kwargs)
	# Print the response
	return response


def test_1():
	"""
	"""
	# A GET request to the API
	#print( http_post('pet',params={'id':0,'category':{'id':1,'name':'dog'},'name':'PET_A'}))
	print( http_post('pet',params={
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}))
	print( http_get('pet/1') )

	"""
	{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
	"""
if __name__ == '__main__':
	test_1()