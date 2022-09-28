class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def Details(self):
        return f"{self.name}'s age is {self.age}"
    def Update_name(self,name):
        self.name=name
    def Update_age(self,age):
        self.age=age


def main():
    p1=Person('jojo',22)
    p2=Person('ram',33)

    print("\nbefore updation\n")
    print("\np1 details\n",p1.Details())
    print("\np2 details\n",p2.Details())

    p1.Update_age(45)
    p2.Update_name(f'Mr.{p2.name}')

    print("\nafter updation\n")
    print("\np1 details\n",p1.Details())

    print("\np2 details\n",p2.Details())

def main2():
    Persons=[('arun',22),('sanal',36),('rahul',17)]
    per=[Person(name,age) for name,age in Persons]
    print("persons details are using list")
    for p in per:
        print(p.Details())

def main3():
    persons=[('arun',22),('sanal',36),('rahul',17)]
    per={name:Person(name,age)
         for name,age in persons}

    arun=per.get('arun')
    arun.Update_age(45)
    print("\npersonal details are using list\n")
    for key,p in per.items():
        print(f"{key}:{p.Details()}")
   

if __name__=='__main__':
    main()
    main2()
    main3()
 

