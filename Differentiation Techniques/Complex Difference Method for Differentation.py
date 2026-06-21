#Done By using Complex Difference Method we compute the derivative of the function  x^a+x^b+x^c at x=9,a=3, b=4, c=2
import math
import numpy as np
class derivative :

     def inputs(self):

                       self.a=3
                       self.b=4
                       self.c=2
                       self.x=9
                       self.arr=[0.1]*9
                       self.hrr=[0.1]*9
                       self.der=[0.1]*9

     def calculation(self):


                       h=0.1
                       i=0
                       z=complex(0,1)
                       while h>=0.000000001:
                         Complexderivative=(((self.x +z*h)**self.a +(self.x+z*h)**self.b +(self.x+z*h)**self.c ).imag)/h
                         self.der[i]=Complexderivative
                         self.hrr[i]=h
                         self.arr[i]=(Complexderivative-3177)
                         if self.arr[i]<0:
                            self.arr[i]=-self.arr[i]
                         h=h*1e-1
                         print(f"The value of the derivative for h= {h} is", Complexderivative,"with the absolute error ",self.arr[i])
                         i=i+1

s1=derivative()
s1.inputs()
s1.calculation()