class A:
         def m1(self):
                  print("m1")
class B(A):
         def m2(self):
                  print("m2")
class C:
         def m3(self):
                  print("M3")
class D(B,C,A):
         def m4(self):
                  print("M4")
                  
