'''
Generator expression use the same comprehension syntax 
but instead of using []  we use ()

[i**2 for i in range(5)]
a list is returned
evaludation is eager
has local scope


(i**2 for i in range(5))
a generator is returned 
evaluation is lazy
has local scope

both can access nonlocal and global scopes
iterable

Resource Utlization
list comprehension is eager 
all objects are created right away 


Genrators are lazy 

object creation is delayed until requested by next()
  generator is created/returned immediately

iteration is fasterf compared in case of list comprehensionn

it is slower in case of generator because iteratin is slow 
because of lazy evaluation 

in casse of list comprehenion entire collection is loaded into memory at once
in case of lazy evaluation is loaded in memeory one at a time

if you do not iterate over entire collection use generartos 
elese use list comprehension 
'''

# Generator Expresion 


g=(i**2 for i in range(5))
type(g)
#generator


import dis

exp = compile('[i**2 for i in range(5)]',filename='<string>',mode='eval');
# here we find out that a function is being created 

exp = compile('(i**2 for i in range(5))',filename='<string>',mode='eval');
# here we find out the same thing 
# a function is being created


l=[i**2 for i in range(5)];
g=(i**2 for i in range(5));

type(l)
# iterable

type(g)
# iterator


#now the element in g do not get created when generator is being defined 
#they are only get created when they are being called

start=1
stop=10

mult_list= [[i*j for j in range(start,stop+1)] for i in range(start,stop+1)]

here we have list within list 

mult_list= ((i*j for j in range(start,stop+1)) for i in range(start,stop+1))
# here we have generator and each element of generator is also a generator
# so we will have a problem when iterating a generator
# list(mult_list) is a list containing all the generators

#

print([  [j for j in i] for i in mult_list ])

print ( ', '.join(str(item) for item in row)   for row in mult_list  )

for i in mult_list:
	for j in i:
		print(j)
	print('\n')	





#how about this 

start = 1
stop= 10

mult_list = ([ i*j for j in range(start,stop+!)] for i in range(start,stop+1) );
# now its is a comprehension with a generator which means when we iterarte over it we alredy
# have an element defined over it


def combo(n,k):
	return factorial(n) // factorial(k) * factorial(n-k)

def pascal_list(size):
	l=[[combo(n,k) for k in range(n+1)] for n in range(size+1) ]
	for row in l:
		for item in row:
			pass

def pascal_gen(size):
	l=((combo(n,k) for k in range(n+1)) for n in range(size+1) )
	for row in l:
		for item in row:
			pass			

#now if we iterate over it time required to iterate over is almost similiar

# but if we compare memeory wise gen tool a lot less memory becuase elements were computed 
# at the time of iteration


# when we are iterating over a file we only need to use a small chunk of memeory if we go with 
# generator because it will take lot less memory








'''