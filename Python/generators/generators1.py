import math;
class FactIter:
	def __init__(self,n):
		self.n=n;
		self.i=0;

	def __iter__(self,n):
		return self;
		
	def __next__(self,n):
		if self.i>self.n:
			return StopIteration
		else:
			self.i+=1;
		    return math.factorial(self.i);	
						
fact_iter= FactIter(5);
next(fact_iter);
next(fact_iter);
next(fact_iter);
next(fact_iter);
next(fact_iter);
next(fact_iter); #Stop Iteration



def factorial(n):
	for i in range(n):
		emit factorial(i)
		pause exection here
		wait for resume 
	return 'done!';

'''
and in our code we would want to do something like this maybe

facts= factorial(4)

__iter__ in facts True
__next__ in facts True

iter(facts) is facts  True 


because facts is an iterator 


nexxt(facts)

Yield to rescue

the yield keyword does exactly we want 
it emits a value 
the function is effectively suspended(but it retains its current value)
calling next on the function resumes the function right after the yield statement 
if function returns something instead of yielding(finishes running)-> StopIteration exception


def song():
	print("line1");
	yield "I'm a song1";
	print("line2");
	yield "I'm a song2";

line = song();
VVVVVIIPPP

when python sees yield inside a function python does not execute the function 
basically line is an iterator

print(next(line))  //I'm a song1
print(next(line))  //I'm a song2
print(next(line))  // we get a stop iteratio exception

Genarator 
a function which uses a yield statement is called a generator function
def my_func():
	yield 1;
	yield 2;
	yield 3;

calling my_func() yields a generator object
we can think of function that contains the yield statement as generator factories
the generator is created by Python when the function is called

GENERATOR implements an iterator protocal 
the resulting generator is executed by calling next(gen)
  the function body will execute until it encounters a yield statement 
  it yields the values ( as return values of next())
  the funciton is suspended 
  until next is called again suspended function resumes execution

if it encounters a retuen before a yield 
returns a StopIteration execption

def my_funct():
    yield 1;
    yield 2;
    yield 3;

gen= my_func();

next(gen); //1
next(gen); //2
next(gen); //3
next(gen); // Stop Iteration


next StopIteration

this should remind you of iterators 

in fact generators are iterators

they implement iterator protocal 
__iter__
__next__
they are exhausted when function returns a values
StopIteration
return value is the exception message





def my_funct():
    yield 1;
    yield 2;
    yield 3;

gen= my_func();

gen.__iter__() returns a generator itself
gen.__next__()
'''		

  
class FactIter:
	def __init__(self,n):
		self.n=n;
		self.i=0;

	def __iter__(self,n):
		return self;
		
	def __next__(self,n):
		if self.i>self.n:
			return StopIteration
		else:
			self.i+=1;
		    return math.factorial(self.i);	
						


def factorials(num):
	for i in range(num):
		yield math.factorial(i);
	return StopIteration	

'''
Generators are inherently lazy iterators (and can be infinite)
Generators become exhausted once the function returns a value




'''


