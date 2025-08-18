Cavet when use lazy ietrators
with open("test.txt","w") as f:
	f.writelines("ddddd")


f=open("test.txt","w")
f.realines()
f.close()

class DataIterator:
	def __init__(self,fname):
		self._fname=fname
		self._f=None

	def __iter__(self):
	    return self

	
	def __next__    	