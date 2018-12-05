class Sample:
    def __init__(self,a,b):
        print("constructor")
        self.x = a
        self.y = b

    def sqrt(self):
        self.z = (self.y)**2
        print(self.z)

    def sum(self,x,y):
        add=x+y
        print(add)

    def diff(self):
        self.sub = -self.y
        print(self.sub)

    def __str__(self):
        return("self.x: "+str(self.x)+"sub: "+str(self.sub))

    def __gt__(self,oth):
        return ((self.x > oth.x) and (self.y > oth.y))



if __name__=='__main__':
    print("the name is: ",__name__)
    ob1=Sample(5,9)
    ob2=Sample(3,8)
    print(ob1>ob2)
    ob1.diff()
    print(ob1)
    print("self.x: "+str(ob1.x)+"sub: "+str(ob1.sub))
    print(type(ob1))