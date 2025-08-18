'''
Lazy Evaluation

This is often used in class properties
   properties 


'''

import math
class Circle:
	def __init__(self,r):
		self.radius=r;

	@property
	def radius(self):
		return self.radius

	@radius.setter
	def radius(self,r):
	    self.radius=r;

	@property
	def area(self):
		return math.pi *(self.radius**2);

c= Circle(1);
# now every time we dont change the radius every time we ask for area it will re calculate it


	    
#every time we set the radius we calculate the area.
		

import math
class Circle:
	def __init__(self,r):
		self.radius=r;
		self._area=None;

	@property
	def radius(self):
		return self.radius

	@radius.setter
	def radius(self,r):
	    self.radius=r;
	    self._area=None;

	@property
	def area(self):
		if self.area is None:
			self._area=math.pi * (self.radius **2);
		return self._area;

c= Circle(1);
# now every time we dont change the radius every time we ask for area it will re calculate it	


class Factorials:
	def __init__(self,length):
		self.length=length;

	def __iter__(self):
	    return self.FactorialsIterator(self.length)

	class FactorialsIterator:
		def __init__(self,length):
			self.length=length;
			self.i=0;

	    def __iter__(self):
	    	return self.FactorialsIterator(self.length)

	    def __next__(self):
	        if self.i >= self.length:
	           raise StopIteration
	        else:
	           result= math.factorial(self.i);
	           self.i+=1;
	           return resultl;
	              	

