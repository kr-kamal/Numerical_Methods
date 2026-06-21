# Backward Diff. Derivative of fn (x**a)+12.5
class derivative :      
                                                
     def inputs(self):     
                                                                
                       self.a=int(input("enter the power of a: "))                      
                       self.x=int(input("enter the value of x: "))   

     def calculation(self):
                          
                       f=self.x**self.a+12.5
                       fh=(self.x-0.00001)**self.a+12.5                                       
                       Backwardderivative=(f-fh)/0.00001                                   
                       print("The value of the derivative is", Backwardderivative)         
                       
s1=derivative()
s1.inputs()         
s1.calculation()                                
