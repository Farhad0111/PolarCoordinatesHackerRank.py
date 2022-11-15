import cmath
class Farhad:
    def __init__(self,i):
        self.i=i
    def faru(self):
        print(pow((pow(self.i.imag, 2) + pow(self.i.real, 2)), 0.5))
class Farhad1(Farhad):
    def faru1(self):
        print(cmath.phase(self.i))
farhad=Farhad1(i=complex(input()))
farhad.faru()
farhad.faru1()
'''i=complex(input())
print(pow((pow(i.imag,2)+pow(i.real,2)),0.5))
print(cmath.phase(i))'''
#print(cmath.phase(input().strip("+")))
#print(complex(input()))
