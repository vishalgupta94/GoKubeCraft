def fibonacci(n):
    if n<2:
        return 1;
    else:
        return fibonacci(n-1)+fibonacci(n-2);


print(fibonacci(5))    
'''
make a list of first seven fibonacci number 



'''

class FibIter:
	def __init__(self,length):
		self.length=length;
		self.i=0;

	def __iter__(self):
		return self

	def __next__(self):
	    if self.i>self.length:
	    	return StopIteration
	    else:
	    	item= math.fibonacci(self.i);
	        self.i+=1;
	        return item;	

# but here we are calculating from scratch everytime


def fib(n):
	fib_0=0;
	yield fib_0
	fib_1=0;
	yield fib_1
	for i in range(n-1):
		fin_0,fin_1 = fib_1,fin_0+fin_1;
		yield fib_1

gen= fib(7);

for num in gen:
	print(num);

timeit('list(FibIter(5000))',globals(),number=1);


'''
Generatos become exhausted
gen functions are functions that use yield
they are actuall iterators 

 but they beocome exhausted
 genrators functions are generators factory because they return an iterator every time we call them
 
 def squares(n):
     for i in range(n):
         yield i**2; 

 sql=squares(5)
 
 l= list(sq)  [1,4,9,16,25]
 
 l= list(sq)  [] 
 because sq got exhausted


'''

 def squares(n):
     for i in range(n):
         yield i**2; 

 sql=squares(5)
 
 l= list(sq)  [1,4,9,16,25]
 
 l= list(sq)  []

 enum1= enumerate(sq);
 # enumerate is lzy
 # but remember enumerate has not touched sq yet it has not taken out its values yet
 # enum uses lazy evaluation
 # next(sq) 0
 # next(sq) 1
 list(enum1)
 [(0,4),(1,9),(2,16)] # because 2 elements of sq are already iterated


l=[1,2,3]

enum= enumerate(l);
list(enum);  [1,2,3]
list(enum);  [] # becuase enum is an iterator

# Making an iterable 
 def squares(n):
     for i in range(n):
         yield i**2; 


class Squares:
	def __init__(self,n):
		self.n=n

	def __iter__(self):
	    return squares(n);	



sq= Squares(n);
l1= list(sq) [0,1,4,9,16]
l2= list(sq) [0,1,4,9,16]


class Squares:
	def __init__(self,n):
		self.n=n

	def __iter__(self):
	    return Squares.squares(self.n);	

    @staticmethod 
	def squares(n):
		for i in range(n):
			yield i**2; 


'''
Card Deck


from collections import namedtuple

Card= namedtuple("Card",'rank suit');
SUITS=("Spades","Hears","Diamonds","clubs")
RANKS=tuple(range(2,11))+tuple('JKQA')
suit_index= card_index // len(RANKS)
suit_index= card_index % len(RANKS) // len(RANKS)



'''	

from collections import namedtuple

Card=namedtuple("CARD",'rank suit')
SUITS=("Spades","Hears","Diamonds","Clubs");
RANKS=tuple(range(2,11))+tuple('JKQA');


for i in range(len(SUITS)*len(RANKS)):
    suit=SUITS[i // len(RANKS)]
    rank=RANKS[i%len(RANKS)]
    print(Card(rank,suit))

def card_gen():
	for i in range(len(SUITS)*len(RANKS)):
		suit=SUITS[i // len(RANKS)]
        rank=RANKS[i%len(RANKS)]
        yield Card(rank,suit)

for card in card_gen():
	print(card);

#make it an iterable

class CardDeck:
	SUITS=("Spades","Hears","Diamonds","Clubs");
	RANKS=tuple(range(2,11))+tuple('JKQA');
    

    def __iter__(self):
    	return CardDeck.card_gen():

    @staticmethod
    def card_gen(self):
        for suit in CardDeck.SUITS:
        	for rank in CardDeck.RANKS:
        		yield CARD(rank,suit);


deck= CardDeck();

print(list(deck));




