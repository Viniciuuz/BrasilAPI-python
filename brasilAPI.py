from requests import get

class Cep(object):
	# set the arguments
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    #get the argument and send the request for the url
    def info(self, param):
    	data = get(f"https://brasilapi.com.br/api/cep/v1/{self.__dict__['cep']}").json()
    	if param == 'all':
    		return data
    	else:
    		return data[param]