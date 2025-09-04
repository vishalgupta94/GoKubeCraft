'''
List Comprehension 
goal-> generate a list by tansforming and optioonally filtering another iteratble


start with iterable                                 other_list=['this','is','a','parrot']
create empty new list                               new_list=[]  
iterate over the original iterable                  for item in other_list:
skip over certain values                                 if len(item)>2: 
transform value and append to new list                       new_list.append(item[::-1])

# [item[::-1]   for item in other_list if len(item)>2 ]
# transform           iteration           filter

sq=[i**2 for i in range(100) if i%2 and i%3 and i%4];
list of square of integer that are not divisible 2,3 and 5

We could write this over multiple lines:
sq=[i**2 for i in range(1,101)
         if i%2 and i%3 and i%5 ]


internals 
what is a comprehension 

comprehension have their own local scope - just like a function 

we should think of a list comprehension as being wrapped in a function that is created by 
Python that will return the new list when executed.

sq= [i**2 for i in range(10)]
when this is compiled 
Python created a temporary function 
def temp():
	new_list=[];
	for i in range(10):
		new_list.append(i**2);
	return new_list


When the line is executed Executes temp()
stores the returned object (the list) in memory
Points sq to that object	
 


 Comprehension Scopes 

So comprenhension Scope 

they have their own local scope 
[item**2 for item in range(100)]
item is local scope

But they can access global variables 

num=100
sq=[[i**2 for i in range(num)]]
here i is local 
and num is globallocal
is is a closure



[ [i**J for j in range(num)] for i in range(5)    ]
--------------------------
  nested comprehension       local variable j
  closure
--------------------------------------------------
      outer comprehenison 
       local variable i 

       free variable i 
this basically is a nested function 

===================================================
We can have nested loops in comprehensions 

This is not the same as nested comprehension  (VVVVIIIIPPPP)

l=[]


for i in range(5):
    for j in range(5):
        for k in range(5):
            l.append((i,j,k))

l=[(i,j,k) for i in range(5) for j in range(5) for k in range(5)]

Nested loops in comprehensions can also contain if statements 

Again the order of the for and if statements does matter,
just like a normal set of for loops and if statements


l=[]
for i in range(5):
	for j in range(5):
		if i==j:
			l.append((i,j))

Correct

[(i,j) for i  in range(5) for j in range(5) if i==j ]
l=[]
for i in range(5):
	if i==j:
	for j in range(5):
		     l.append((i,j))
InCorrect
[(i,j) for i  in range(5) if i==j for j in range(5)  ]

Exercies 
l=[]
for i in range(1,6):
	if i%2 == 0:
		for j in range(1,6):
			if j%3 == 0:
				l.append((i,j))

[(i,j) 
for i  in range(1,6) if i%2==0 
for j in range(1,6)  if j%3==0]			


l=[]
for i in range(1,6):
		for j in range(1,6):
            if i%2 == 0:
			    if j%3 == 0:
				    l.append((i,j))

[(i,j) 
for i  in range(1,6) 
for j in range(1,6) if i%2==0 if j%3==0]			


=======================
Coding

compiled_code=compile('[i**2 for i in (1,2,3)],filename='string',mode='eval')
compiled_code

it is making a function out of list comprehension 
table=[]
for i in range(1,11):
	row=[]
	for j in range(1,11):
		row.append(i*j)
	table.append(row)

convert this into list comprehension 
nested comprehension 
[ [ i*j for j in range(1,11)] for i in range(1,11) ] 
		

'''
		