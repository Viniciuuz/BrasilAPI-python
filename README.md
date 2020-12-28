# Wraper for [BrasilAPI](https://github.com/BrasilAPI/BrasilAPI) in python

Simple wraper for [BrasilAPI](https://github.com/BrasilAPI/BrasilAPI) created by [@filipedeschamps](https://github.com/filipedeschamps) and [@lucianopf](https://github.com/lucianopf) built with python and the requests module

---

## instalation (Not yet in pip)
### Requirements
* Python 3
* Requests

all you need is the brasilAPI file. Clone the repo and you're good to go


## Endpoints
## Cep
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

cep = Cep(cep='05010000').info('all') #save response to any variable, no error handling function

print(cep['street']) #print street from the variable you set
```

## Bank
### Method 1
```python
from brasilAPI import Bank #import only the class you need

bank = Bank(bank='260') # set the bank code

#supported parameters are: ispb, name, code and fullName

print(cep.info('ispb')) # print only the ispb
print(cep.info('name')) # print only the name
```

### Method 2
#### There is no error handling function in this method
```python
from brasilAPI import Bank #import only the class you need

bank = Bank(bank='260').info('all') #save response to any variable, no error handling function

print(bank['name']) #print street from the variable you set
```