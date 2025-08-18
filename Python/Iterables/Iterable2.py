'''
Iterables
what are iterators 

till now cannot use for loop
no going back we have to reinitialise
once we reach StopIteration we're basically done with the object

we have __next__,StopIteration,while loop
using these using for loop is implemented

but how do we tell python that the next method 
we have implemented is consistent with for loops next method

the Iterator protocol

A protocol is simply a fancy way of saying that our class is going to implement certain 
functionality that Python can count on

To let Python is quite simple - the class needs to implement two methods

__iter__ this method should just return the object (class instance) itself sounds weird but we will undestand later
__next__ return elements until no elements left raise StopIteration exception

An object that implements these 2 methods is called iterator

An iterator is therefore an object that implements 

__iter__
__next__

If an object is an iterator we can use it for loops ,comprehension

lets make squares in iterator


'''

class Squares:
	def __init__(self,length):
		self.i=0;
		self.length=length;
	
	def __iter__(self):
	    return self;
		
    def __next__(self):
		if self.i> self.length:
			raise StopIteration
		else:
		    result=self.i**2;
		    self.i+=1;
		    return result;	

			    
for i in Squares(10):
    print(i);


'''
still one issue 
the iterator cannot be restarted 
once we have looped througt all the items
   the iterator has been exhausted

to loop a second time througth the collection we have to create 
a new instance and loop throught that
   


'''    