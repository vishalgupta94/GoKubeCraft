

"""
# Context Managers

# try:

# finally
# #always execute


#

Pattern 
crete some object
   do some some work with that object 
clean up the object after we're done with the object.

We want to make this easy
automatic clean up once we done are using the object.

that is when Context Manager were defined.


with context as obj_name: 	 		
	#with block (can use obj_name)

# after the with block, context is cleaned up automatically.


with open(file_name) as f: #enter the context # an object is returned
   #file is nor open 
   #exit the context.

file is closed  automatically

Context management protocol 

Classes implement the context management protocal by implementing 2 methods


__enter__
#set and optionally return some object.

__exit__
#tear down/ cleanup

mgr= ContextManager();

with CtxManager() as obj:
	# do something

# done with context.


#  this is same as

mgr= ContextManager();

obj= mgr.__enter__()

try:
	#
finally:
    # done with context.
    mgr.__exit__();

# its a lot simplier this way than writing code as with class object.



###########


# Use case such as opening the file(creating a resource) and then closing the file (releasing the resources)
# Context Manger can used for much more than opening and closing the file

Common Patters
 
 Open - Close
 lock release
 change reset
 start stop
 enter exit
# how does CM work.

class Myclass:
	def __init__(self):
		# init class

	def __enter__(self):
		return obj

	def __exit__(self):
	# clean up the object


CM wokrs in conjection with with the "with " statement


had with not been there

myinstance = MyClass();
obj=myinstance.__enter__();		
#now this obj is same as 

with myCLass() as obj: 
#create an instance of my class
#calls the enter method on that instance

#with state method calls the enter method whatever gets returned as
#assigned to the object

#both the object are same	
 
# after the with block __exit__ method is called finally
with myCLass() as f: 
	row = next(f);

#both f and row are now global.

print(f) #f is cloed but symbol exist
print(row) # row is available and has a value

def __enter__(self):
   #this method should perform whatever setup it need to 
   #it can optionally return an object.

def __exit__()   

just like finally exit ales runs even if exception occurs

__exit__ will run in all cases.

exit method 
 maybe   so it need to know about any exceptions that occured

 it also needs to tell python whether to silence the exceptionsot let it propagate.






The __exit__ methods

with MyContext() as obj:
	raise ValueError:
    
print('done')

Scenario 1

__exit receives an error , 
performs some clean up and silences ValueError
print statement runs 
no exception is seen 

Scenario 2

__exit__ receives error,
performs some clean up and lets error propragete

print statement does not run in
# the Value Exception is seen

exit method need 3 arguments

the exception type that occured (if any, None otherwise)
the exception value that occured(if any, None otherwise)
the traceback object if an exception occured (if any, None otherwise)

Return True or False
true silence raised exception
false do not silence a raised exceptions 


def __exit__(self,exc_type,exc_value,exc_trace):
	return True




"""

def my_func():
	try:
		10/0
	except ZeroDivisionError:
	   return 
	finally:
	   print("Finally Run")


my_func()
#Finally run
#finally will run no what what


try:
	f=open("text.txt","w")
finally:
	f.close();

# even though the exception occured
# no matter what happens file will get closed.


with #with the with it will enter the context and will call the __enter__ method
when with is finished the exit will no
even with exception will occur no matter what


with open("text.txt") as f:
	#f is obects returned by the enter method of the open class
	print("is file close",f.closed);

print("is file close",f.closed);	

"is file close" ->  False
"is file close" ->  True

def test():
	with open("test.txt","w") as file:
		print("is file close",file.closed);
      return file

file=test();
# inside with file  closed? False
file.closed tRUE

with open() as file:
	raise ValueError()

#exception will occure but the program will get closed
#if exit returns True it will silence the error
#file is closed
file will still be closed


with open("text.txt","w") as f:
	f.writelines("this is a text")


with open("text.txt") as f:
	row=next(f);

print(row)# this si a text

with does not have a scope of its own.


#create our own context manager

class MyContext:
	def __init__(self):
		self.obj=None

	def __enter__(Self):
	   print("entering conetxt");
	   self.obj= 'the return object';
	   return self.obj;

	def __exit__(self,exc_type,exc_val,exc_tb):
	   print("entering exist");
      if exc_type:
      	print(f'*** Error occured  {exc_type},{exc_val}')
      return False	# go ahead and process the error as it hadn't been interscepted  dont silece the exception
      


ctx=MyContext()
with ctx as obj:


ctx=MyContext()
print("created context")
with ctx as obj:
	print("inside with block",obj )
	raise ValueError('custom message')

created context
entering Context	
inside with block the Return object
error occured exception



with open()  as f 
#with manipu;ate the file object 

class Resource:
	def __init__(self,name):
		self.name=name;
		self.resource='None';
   
   def __enter__(self):
   	print('entering context');
   	self.resource = Resource(self.name) 
   	self.resource.state = 'created'
   	return self.resource

   def __exit__(self,exc_ty,exc_val,exc_tb):
   	print("exiting exit")
      self.resource.state="destroyed"
      if exc_ty:
         print('error occured')
      return False

with ResourceManager('spam') as res:
	print(f'{res.name} == {res.state}')
print(f'{res.name} == {res.state}')	

entering context
spam created
entering exit
spam destroyed
               



class File:
	def __init__(self,name,mode):
		self.name=name;
		self.mode=mode;

	def __enter__(self):
	   print('opening file...')
	   self.file = open(self.name,self.mode)
	   return self.file	   
   
   def __exit__(self,exc_type,exc_value,exc_tb):
   	print("closing file")
   	self.file.close()
   	return False;

   
with File('test.txt','w') as f:
	f.write('this is a late  parrot')


opening file
closing file	

with File('test.txt','w') as f:
	print(f.readlines())


opening file
'this is a late  parrot'
closing file	
		
#####################


class File:
	def __init__(self,name,mode):
		self.name=name;
		self.mode=mode;

	def __enter__(self):
	   print('opening file...')
	   self.file = open(self.name,self.mode)
	   return self  
   
   def __exit__(self,exc_type,exc_value,exc_tb):
   	print("closing file")
   	self.file.close()
   	return False;
with File('test.txt','r') as file_ctx:
	print(next(file_ctx.file))
	print(file_ctx.mode)
	print(file_ctx.name)


file_ctx is not an instace of File it is whatever is returned from enter method


