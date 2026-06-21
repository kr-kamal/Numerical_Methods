#By using Central Difference Method we compute the derivative of the given function 1/(x+b) at x=0 and b=1e-5
import numpy as np
class derivative :

     def inputs(self):

                       self.b=1e-5
                       self.x=0
                       self.arr=[0.1]*15
                       self.hrr=[0.1]*15
                       self.der=[0.1]*15
                       
     def calculation(self):

                       f=1/((self.x+self.b))
                       h=0.2
                       i=0
                       while h>=0.000000000000002:

                         forward_step= 1/((self.x+h)+self.b)
                         backward_step= 1/((self.x-h)+self.b)
                         Centralderivative=(forward_step-backward_step)/(2*h )

                         self.hrr[i]=h
                         self.der[i]=-Centralderivative
                         self.arr[i]=Centralderivative+1e10
                         if self.arr[i]<0:
                            self.arr[i]=-self.arr[i]
                         print(f"The value of the derivative for {h} is", Centralderivative,"with the absolute error ",self.arr[i])
                         h=h*1e-1
                         i=i+1


s1=derivative()
s1.inputs()
s1.calculation()