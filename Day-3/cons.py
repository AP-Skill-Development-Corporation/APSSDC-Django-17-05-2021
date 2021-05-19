class Student:
         def __init__(f2,a,b):
                  print("i am From Construtor method")
                  f2.a=a
                  f2.b=b
                  
         def add(f1):
                  c=30
                  d=40
                  print("Addition of {} and {} is {}".format(f1.a,f1.b,f1.a+f1.b))
         def  myfun(self):
                  print(c,d)
                  print("i am from Myfun")

h1=Student(10,20);
h1.add()
h1.myfun()
