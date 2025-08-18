'''
With sequences index its just iterting indexs.

But iterating can be more general than based on sequenctial indexing.

All we need is 
a bucket ot items -> containers(bag of marbles)
get next items-> next item from the containers(no concept of ordering here)
                 pick up next marble from bag of marbles.


Sets are unorderd collection of items.

Sets are not indexable but they are iterable.

Foe general iteration , all we really need is the concept of get the next item in the collection

If a collection impplements a get_next_item method

get_next_item()
get_next_item()
get_next_item()
marble from bag of marbles.

we could iterate over the collection as follows

for _ in range(10):
  item= coll.get_next_item();
  print(item);



# coll is the collection

but how do we know how to end the squence
IndexError exception
Stopiteration exception to stop the iteration


let build a iterable ourselves

'''
class Squares:
	def __init__(self):
		self.i=0;

	def next_(self):
	    result=self.i**2;
        self.i+=1 
	    return result;	


sq= Sqaures();
# collection right now is infinite



'''
problems
1 for loop wont work 
2 cannot start from beginning 
//solution sq= Squares();
//we restart by creating a new instance
3 infinite

sq.next_()
// keep on going 

we make it finite first
specify the size first 

'''

class Squares:
	def __init__(self,length):
		self.i=0;
		self.length=length;

	def next_(self):
		if self.i> self.length:
			raise StopIteration
		else:
		    result=self.i**2;
		    self.i+=1;
		    return result;	


sq= Squares(5)

while True:
	try:
		item= sq.next_();
		print(item)
	except StopIteration:
	    break;


len()  -> __len__
next() -> __next__ 

while True:
	try:
		item= next(sq);
		print(item)
	except StopIteration:
	    break;
# if we call this again it wont print anything because 
# its already exhausted so have to initialise instance again
# sq=Sqaures(10)


print item in sq:
    print(item)
#error
# Squares() object is not iterable


import random;
class RandomNunbers():
    def __init__(self,length,*,range_min=0,range_max=10):
        self.length=length;
        self.range_min=range_min;
        self.range_max=range_max;
        self.num_requested=0;
    
    def __len__(self):
        return self.length
    
    def __next__(self):
        if self.num_requested>self.length:
            raise StopIteration;
        else:
            self.num_requested+=1;
            return random.randint(self.range_min,self.range_max);
            
numbers= RandomNunbers(10);            
# next(numbers);
# next(numbers);
# next(numbers);
# next(numbers);
# #...after 10 
# # will raise the exception
# numbers= RandomNunbers(10):

while True:
	try:
		item = next(numbers);
		print(item)
	except StopIteration:
	    break;    
    