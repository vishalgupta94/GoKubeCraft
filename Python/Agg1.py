/*

functions that iterable as an argument and return a values are called aggretors
considering every element of the iterable.RANKS
min(iterable)
max()

Assocaited truth value.

Evry object returns True
By default everything is true unless certain things happen


None
False
0 in any numeric 
empty sequence 
empty mapping types 

any(iterable) true
all(iterable) true only for all
a function that takes a single argument  adn returns a true or false retuns a predicte.RANKS

 we can make any and all usefull by applying predicate to all the elements of that iterable.RANKS

 l=[1,2,3,4,100]
 if any elemnt is less than 10

 first define a suitable predicate
 pred= lambda x : x<10
 
 any([pred(x) for x in l]);


 check if every element is less than 10

 all([pred(x) for x in l])

we can also use map 

coding 

def squares(n):
	for i in range(n):
		yield i**2;

list(squares(5));


// now remember that sq= Squares(5) return an iterator not an iterbale 
so min(sq) is some values
and min(sq)  is an error

even next(Sq) will also return StopIteration exception
now bool(sq)
again it will be true remember that every object is truthy unless we explicity reutrn false.



class Person:
	pass

p=Person()	
bool(p)  true


class Person:
	def __bool__(self):
		return 0

p=Person()	
bool(p)  false


class Person:
	def __init__(self):
		return 0

p=Person()	
bool(p)  false

class Person:
	def __bool__(self):
		return True

	def __init__(self):
		return 0	
p = Perosn();
bool(p) true

L=[10,20,30,40,'NONE']

is_all_numbers= True;

for item in L:
	if not isinstance(item,Number):
		is_all_numbers=False;
		break;

is_all_numbers
False


def is_numeric(v):
	return isinstance(v,Number)

pred_l= map(is_numeric,L);
pred_l= [is_numeric(item) for item in L];


file contains many lines 


with open() as f:
	//now f is either an iterable or iterator:
	all(map(lambda row:len(row) >= 4 , f))



with open()  as f:
	(len(row)>=4 for row in f)
	result= all( len(row)>=4 for row in f)

print(result);	











*/