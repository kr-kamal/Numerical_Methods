# We take the function x^a +y^b, and calculate the Partial Derivatives with respect to x and y  here, x=7, y=4, a=5, b=6.
class Forwardderivative :

     def inputs(self):
                       self.a=5
                       self.b=6
                       self.x=7
                       self.y=4
                       self.arr=[0.1]*14
                       self.arry=[0.1]*14
                       self.hrr=[0.1]*14
                       self.derx=[0.1]*14
                       self.dery=[0.1]*14
                       self.h=0.01
                       self.i=0
     def calculation_of_x(self):

                       f=self.x**self.a+self.y**self.b                                                                                                                                                       #initialization of the value i to 0
                       while self.h>0.000000000000001:
                            fhx=(self.x+self.h)**self.a+self.y**self.b
                            PartialForwardderivative_of_x=(fhx-f)/self.h
                            self.arr[self.i]=PartialForwardderivative_of_x-12005

                            if self.arr[self.i]<0:
                                    self.arr[self.i]=-self.arr[self.i]
                            print(f"The value of the Partial derivative of x for h= {self.h} is", PartialForwardderivative_of_x,"with the absolute error of ",self.arr[self.i])
                            self.hrr[self.i]=self.h
                            self.h=self.h*1e-1
                            if(self.arr[self.i]<0.01 and self.arr[self.i]>-0.01):
                                break
                            self.i=self.i+1
     def calculation_of_y(self):

                       f=self.x**self.a+self.y**self.b
                       self.h=0.01
                       self.i=0
                       while self.h>0.000000000000001:

                            fhy=(self.x)**self.a+(self.y+self.h)**self.b
                            PartialForwardderivative_of_y=(fhy-f)/self.h
                            self.arry[self.i]=PartialForwardderivative_of_y-6144
                            if self.arry[self.i]<0:
                                    self.arry[self.i]=-self.arry[self.i]
                            print(f"The value of the Partial derivative of y for h= {self.h} is", PartialForwardderivative_of_y,"with the absolute error of ",self.arry[self.i])
                            self.hrr[self.i]=self.h
                            self.h=self.h*1e-1
                            self.arry[self.i]=PartialForwardderivative_of_y-6144
                            if self.arry[self.i]<0:
                                    self.arry[self.i]=-self.arry[self.i]
                            self.i=self.i+1
                            if(self.arr[self.i]<0.01 and self.arr[self.i]>-0.01):
                                break

s1=Forwardderivative()
s1.inputs()
s1.calculation_of_x()
s1.calculation_of_y()
