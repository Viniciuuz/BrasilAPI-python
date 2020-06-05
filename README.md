# Wraper for [BrasilAPI](https://github.com/filipedeschamps/BrasilAPI/) in python

Simple wraper for [BrasilAPI](https://github.com/filipedeschamps/BrasilAPI/) created by [@filipedeschamps](https://github.com/filipedeschamps) and [@lucianopf](https://github.com/lucianopf) built with python and the requests module

---

## instalation (Not yet in pip)
### Requirements
* Python 3
* requests

all you need is the brasilAPI file. Clone the repo and your are good to go


## Usage
### Method 1

#### Recommended
```python
from brasilAPI import Cep #import only the class you need

cep = Cep(cep='05010000') # set the adress

#supported parameters are: state, city, neighborhood, street and all

print(cep.info('neighborhood')) # print only the neighborhood
print(cep.info('state')) # print only the state
```

### Method 2
#### There is no error handling function in this method
```python
from brasilAPI import Cep #import only the class you need

cep = Cep(cep='05010000').info('all') #save response to any variable, no error 

print(cep['street']) #print street from the variable you set
```