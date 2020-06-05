from requests import get

class Cep(object):
	# set the arguments
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    #get the argument and send the request to the url
    def info(self, param):
    	data = get(f"https://brasilapi.com.br/api/cep/v1/{self.__dict__['cep']}")

    	#check if the request was successfull
    	if data.status_code == 200:
    		data = data.json()

    		if param == 'all':
    			# return the response formatted in json
	    		return data
	    	else:
	    		#return only the specific query
	    		return data[param]

	    #if not successfull return the error message from the APi
    	else:
    		return data.json()['message']