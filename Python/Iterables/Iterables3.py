#the dropback is that iteratos get exhausted
'''
become useless for iterating again
become throw away object
why should we have to re create the collection of items just to iterate over them?

Instead we would prefer to seprate these two

but two distinct things going on
1 maintaining the collection of items
2 iterating the collection

why should we have to re create the collection of items just to iterate over them 

instead we should prefer to seprate these two.

Maintaing over the data should be one object 
Iterating over the data should be another object -> iterator (it is going to be throw away object)

The collection is iterable 
 but the iterator is responsible for iterating over the collection

The Iterable is created once(collection is created once)
The iterator is created every time we need to start a fresh iteration

class Cities:
	def __init__(self):
		self._cities= ['Paris','Berlin','Rome','London']
		self._index=0
    
    def __iter__(self):
    	return self

    def __next__(self):
       if self.index >= len(self._cities):
            raise StopIteration:
       else:
           item= self._cities[self._index]
           self._index+=1
           return item     	


Cities instance are iterator
Every time we have to loop we have to create new instance of cities
this is wastedfull why re create the data(VIP) when all we have to do is reiterate over it


class Cities:
	def __init__(self):
		self._cities= ['Paris','Berlin','Rome','London']
		self._index=0
    
    def __len__(self):
    	return len(self._cities)



class CitiesIterator:
	def __init__(self,cities):
		self._cities= cities
		self._index=0
    
    def __iter__(self):
    	return self

    def __next__(self):
       if self.index >= len(self._cities):
            raise StopIteration:
       else:
           item= self._cities[self._index]
           self._index+=1
           return item           		



to use Cities and CitiesIterator together heres how we would proceed

cities = Cities();
cities_iterator = CitiesIterator();
for city in cities_iterator:
	print(city);


At this point, the cities_iterator is exhausted
if we want to re iterate over the collection we need to create a new one

cities_iterator = CitiesIterator();
for city in cities_iterator:
	print(city);

to solve that problem we have to create new instace of CityIterator

Iterable 

An iterable is a Python object that implements the iterable protocal
AN iterable protocol requires that the object implement a single method

__iter__ returns a new instance of the iterator object used to iterate over the iterable

class Cities:
	def __init__(self):
		self._cities= ['Paris','Berlin','Rome','London']
		self._index=0
    
    def __len__(self):
    	return len(self._cities)

    def __iter__(self):
    	return CitiesIterator(self)    	



class CitiesIterator:
	def __init__(self,cities):
		self._cities= cities
		self._index=0
    
    def __iter__(self):
    	return self

    def __next__(self):
       if self.index >= len(self._cities):
            raise StopIteration:
       else:
           item= self._cities[self._index]
           self._index+=1
           return item           		






AN iterator is an iterable 

Iterator vs iterable

iterable is an object that implements 
  __iter__ returns an iterator

An iterator is an object that implements
__iter__ return itself
__next__ return next element


So iterators are themselves iterables but they become exhausted

Iterables on the other hand never become exhausted
  because they always return a new iterator  that is then used to iterate



Iterating over an iterable
  Python has a build in function iter()

  It calls the __iter__ method


The first thing Python does when we try to iterate over an object 
it calls iter() to obtain an iterator

then it starts iterating (using next,StopIteration, etc)







'''