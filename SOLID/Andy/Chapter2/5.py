import __main__
class Vishal:
    pass

print(__main__.Vishal)
print(Vishal.__bases__)
print(Vishal.__name__)

c1 = Vishal()

class Vishal2:
    name = "vishal"
    surName = "gupta"

    def drive(self,):
        return self   # c1 = c1.drive()

c1 = Vishal2()    # c1 = c1.drive()

Vishal2.name = "els"

print(Vishal.__dict__)
print(c1.name)

print(c1 == c1.drive())

print(type(Vishal2.drive))

print(type(Vishal2.drive))


m1 = Vishal2()
m2 = Vishal2()

objs = [m1, m2]

for obj in objs:
    setattr(obj,"newName","el1s")

print(m1.newName)    