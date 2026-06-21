#This program calculates the derivative of the function f(x) = x^a + 12.5 at x==9 and a==5 point 
#This program also plots a graph between the value of h and the error in the derivative 
#This is the defination of the class named derivative
class derivative :      
                                                
     def inputs(self):                              # Defination of the member function named "inputs" for getting input from user as i passes the self as an argument so that i can access the variables in other Member Function inside the class
                                                    #I hope you are ready to understand the code
                       self.a=5                   #Data member a is initialized to 5 
                       self.x=9                   #Data member x is initialized to 9
                       self.arr=[0.1]*11            #Initialization of the list named arr of size 15 to store the error values        
                       self.hrr=[0.1]*11
                       self.der=[0.1]*11  
      
                                         
     def calculation(self):                                                                               #Defination of the member function named "calculation" for calculating the derivative using forward method as i passes the self as an argument so that i can access the variables in other Member Function inside the class
                                                                                                          #I hope you understand the logic behind the calculation of derivative using forward method
                       f=self.x**self.a+12.5                                                        #calculation of f(x) at x=9 and a=5
                       h=0.1                                                                              #initialization of the value of h to 0.1
                       i=0                                                                                #initialization of the value i to 0
                       while h>=0.00000000001:                                                                #loop will run until the value of h is greater than or equal to 0.0000001
                     
                            fh=(self.x+h)**self.a+12.5                                              #calculation of f(x+h)
                            Forwardderivative=(fh-f) / h                                              #calculation of the Forward Derivative using the forward method formula
                            print(f"{i}The value of the derivative for {h} is", Forwardderivative)           #showing the output of the Forward Derivative calulated by the program 
                            self.hrr[i]=h                                                                 #storing the value of h in the list named hrr
                            h=h*1e-1   
                            self.der[i]=Forwardderivative                                                                   #decreasing the value of h 
                            self.arr[i]=(Forwardderivative-32805)    
                            if self.arr[i]<0:
                                    self.arr[i]=-self.arr[i]                               #storing the error value in the list named arr
                            i=i+1                                                                         #incrementing the value of i by 1 after each iteration
                    
     def graph(self):                                                                                                                                      #Defination of the member function named "graph" for plotting the graph between the value of h and the error
                                                                                                                                                           #i hope you understand the calulation function of the derivative
                       import matplotlib.pyplot as pl                                                                                                    #importing the matplotlib module for plotting the graph 
                       pl.loglog(self.hrr, self.der, marker='o')                                                                                          #plotting the graph using loglog function as i have to plot the graph for very low values of h
                       pl.ylabel('Forward Derivative    ------>', color="red",fontsize=12, fontweight='bold')                                                                        #label of x-axis
                       pl.xlabel('Step size (h)    ------>',color="red", fontsize=12, fontweight='bold')                                                                      #label of y-axis
                       pl.show()                                                                                                                          #showing the graph

s1=derivative()                                                                             # This step  for the creation of the object of the class derivative named s1
s1.inputs()                                                                                 # Function Call of inputs function using the object s1
s1.calculation()                                                                            # Function Call of calculation funnction using the object s1
s1.graph()                                                                                 