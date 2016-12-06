# coding: utf-8 # 
# Implementação das funções PSDs
import numpy as np


class PSD1:
    def __init__(self):
        ''' PSD properties
        '''
        self.number = 1 # number of PSD
        self.minimum = 5
        self.maximum = 10 
        self.ymax = 10.0
        xunit = "rad/s"
        yunit = "u^2/(rad/s)"
     
    def feval(self, x):
        ''' evaluates PSD function at x
        x can be a float, a list or a numpy array
        '''
        y = []
        if isinstance(x,float):
            xlist = [x]
        else:    
            xlist = x
            
        for i in xlist:
            if i<self.minimum:
                y.append(0.0)
            elif i<=self.maximum: 
                y.append(10.0)
            else:
                y.append(0.0)
        
        if isinstance(x,float):
            return y[0]
        else:
            return y
        
    def area(self,a,b):
        ''' evaluates the integral of PSD function at the interval a until b
        '''
        # check the input a and b
        if a>b:
            print("a must be greater than b")
            return 
        #elif b>self.maximum and a<self.minimum:
        #    print("the range a and b is to big. Decrease the interval.")
        #    return 
        
        # evaluate integral
        if b<self.minimum:
            #print(1)
            return 0.0
        
        elif a>self.maximum:
            #print(2)
            return 0.0
        
        elif b<=self.maximum and a>=self.minimum:            
            #print(3)
            fa = self.feval(a)            
            area = (b-a)*(fa)
            return area  
        
        elif a>=self.minimum and b>self.maximum:
            #print(4)
            fa = self.feval(a)
            area = (self.maximum-a)*(fa)
            return area
        else:
            #print(5)
            fb = self.feval(b)
            area = (b-self.minimum)*(fb)
            return area

#----------------------------------------------------------------
        
class PSD2:
    def __init__(self):
        ''' PSD properties
        '''
        self.number = 2 # number of PSD
        self.minimum = 4.
        self.maximum = 11.
        self.avg = self.minimum + (self.maximum - self.minimum)/2.0
        self.ymax = 14.3
        xunit = "rad/s"
        yunit = "u^2/(rad/s)"
     
    def feval(self, x):
        ''' evaluates PSD function at x
        x can be a float, a list or a numpy array
        '''
        y = []
        if isinstance(x,float):
            xlist = [x]
        else:    
            xlist = x
            
        for i in xlist:
            if i<self.minimum:
                y.append(0.0)
            elif i>self.maximum: 
                y.append(0.0)
            elif i<=self.avg:
                y0 = 0.0
                y1 = self.ymax
                x0 = self.minimum
                x1 = self.avg
                a = (y1-y0)/(x1-x0)
                b = y0 - a*x0
                yval = a*i+b 
                y.append(yval)
            
            else:  
                y0 = self.ymax
                y1 = 0.0
                x0 = self.avg
                x1 = self.maximum
                a = (y1-y0)/(x1-x0)
                b = y0 - a*x0
                yval = a*i+b 
                y.append(yval)
        
        if isinstance(x,float):
            return y[0]
        else:
            return y
        
    def area(self,a,b):
        ''' evaluates the integral of PSD function at the interval a until b
        '''
        # check the input a and b
        if a>b:
            print("a must be greater than b")
            return 
        #elif b>self.maximum:
        #    print("Select b at least equal to %f" %self.maximum)
        #    return 0
        #elif a<self.minimum:
        #    print("Select a greater or equal to %f" %self.minimum)
        #    return 0
        
        # evaluate integral
        if b<self.minimum:
            #print(1)
            return 0.0
        
        elif a>self.maximum:
            #print(2)
            return 0.0
        
        elif (b<=self.avg and a>=self.minimum) or (a>=self.avg and b<=self.maximum):            
            #print(3)
            fa = self.feval(a)    
            fb = self.feval(b)
            area = (b-a)*(fa+fb)/2.0
            return area  
        
        else:
            fb = self.feval(b)
            fa = self.feval(a)    
            fmax = self.ymax
            area1 = (self.avg-a)*(fa+fmax)/2.0
            area2 = (b-self.avg)*(fb+fmax)/2.0
            area = area1 + area2
            return area

        
#----------------------------------------------------------------        
        
class PSD3:
    def __init__(self):
        ''' PSD properties
        '''
        self.number = 3 # number of PSD
        self.minimum = 1.
        self.maximum = 14.
        self.avg = self.minimum + (self.maximum - self.minimum)/2.0
        self.ymax = 7.7
        xunit = "rad/s"
        yunit = "u^2/(rad/s)"
     
    def feval(self, x):
        ''' evaluates PSD function at x
        x can be a float, a list or a numpy array
        '''
        y = []
        if isinstance(x,float):
            xlist = [x]
        else:    
            xlist = x
            
        for i in xlist:
            if i<self.minimum:
                y.append(0.0)
            elif i>self.maximum: 
                y.append(0.0)
            elif i<=self.avg:
                y0 = 0.0
                y1 = self.ymax
                x0 = self.minimum
                x1 = self.avg
                a = (y1-y0)/(x1-x0)
                b = y0 - a*x0
                yval = a*i+b 
                y.append(yval)
            
            else:  
                y0 = self.ymax
                y1 = 0.0
                x0 = self.avg
                x1 = self.maximum
                a = (y1-y0)/(x1-x0)
                b = y0 - a*x0
                yval = a*i+b 
                y.append(yval)
        
        if isinstance(x,float):
            return y[0]
        else:
            return y
        
    def area(self,a,b):
        ''' evaluates the integral of PSD function at the interval a until b
        '''
        # check the input a and b
        if a>b:
            print("a must be greater than b")
            return 
        #elif b>self.maximum:
        #    print("Select b at least equal to %f" %self.maximum)
        #    return 0
        #elif a<self.minimum:
        #    print("Select a greater or equal to %f" %self.minimum)
        #    return 0
        
        # evaluate integral
        if b<self.minimum:
            #print(1)
            return 0.0
        
        elif a>self.maximum:
            #print(2)
            return 0.0
        
        elif (b<=self.avg and a>=self.minimum) or (a>=self.avg and b<=self.maximum):
            #print(3)
            fa = self.feval(a)    
            fb = self.feval(b)
            area = (b-a)*(fa+fb)/2.0
            return area  
        
        else:
            fb = self.feval(b)
            fa = self.feval(a)    
            fmax = self.ymax
            area1 = (self.avg-a)*(fa+fmax)/2.0
            area2 = (b-self.avg)*(fb+fmax)/2.0
            area = area1 + area2
            return area

#----------------------------------------------------------------   
class PSD4:
    def __init__(self):
        ''' PSD properties
        '''
        self.number = 4 # number of PSD
        self.minimum = 2.0
        self.maximum = 16.0 
        self.max1 = 4.0
        self.min2 = 14.0
        self.ymax = 16.0
        xunit = "rad/s"
        yunit = "u^2/(rad/s)"
     
    def feval(self, x):
        ''' evaluates PSD function at x
        x can be a float, a list or a numpy array
        '''
        y = []
        if isinstance(x,float):
            xlist = [x]
        else:    
            xlist = x
            
        for i in xlist:
            if i<self.minimum:
                y.append(0.0)
            elif i<=self.max1: 
                y.append(16.0)
            elif i<self.min2:
                y.append(0.0)
            elif i<=self.maximum:
                y.append(9.0)
            else:
                y.append(0.0)
        
        if isinstance(x,float):
            return y[0]
        else:
            return y
        
    def area(self,a,b):
        ''' evaluates the integral of PSD function at the interval a until b
        '''
        # check the input a and b
        if a>b:
            print("a must be greater than b")
            return 
        #elif (b-a)>1.0:
        #    print("Select a range smaller than 1")
        #    return 
        
        
        # evaluate integral
        if b<self.minimum:
            #print(1)
            return 0.0
        
        elif a>self.maximum:
            #print(2)
            return 0.0
        
        elif a>self.max1 and b<self.min2:
            #print(3)
            return 0.0
        
        elif (b<=self.max1 and a>=self.minimum) or (a>=self.min2 and b<=self.maximum):            
            #print(4)
            fa = self.feval(a)            
            area = (b-a)*(fa)
            return area  
        
        elif a>=self.minimum and a<self.max1 and b>self.max1:
            #print(5)
            fa = self.feval(a)
            area = (self.max1-a)*(fa)
            print(area)
            return area
        
        elif a<self.minimum and b<=self.max1:
            #print(6)
            fb = self.feval(b)
            area = (b-self.minimum)*(fb)
            return area
        
        elif a>=self.min2 and b>self.maximum:
            #print(7)
            fa = self.feval(a)
            area = (self.maximum-a)*(fa)
            return area
        
        elif a<self.min2 and b<=self.maximum:
            #print(8)
            fb = self.feval(b)
            area = (b-self.min2)*(fb)
            return area
        
        else:
            #print(9)            
            return 0

#-------------------------------------------------------
class PSD5:
    def __init__(self):
        ''' PSD properties
        '''
        self.number = 5 # number of PSD
        self.minimum = 1.0
        self.maximum = 14.0
        self.ymax = 3.85
        xunit = "rad/s"
        yunit = "u^2/(rad/s)"
     
    def feval(self, x):
        ''' evaluates PSD function at x
        x can be a float, a list or a numpy array
        '''
        y = []
        if isinstance(x,float):
            xlist = [x]
        else:    
            xlist = x
            
        for i in xlist:
            if i<self.minimum:
                y.append(0.0)
            elif i<self.maximum: 
                y.append(self.ymax)
            else:
                y.append(0.0)
        
        if isinstance(x,float):
            return y[0]
        else:
            return y
        
    def area(self,a,b):
        ''' evaluates the integral of PSD function at the interval a until b
        '''
        # check the input a and b
        if a>b:
            print("a must be greater than b")
            return 
        #elif b>self.maximum and a<self.minimum:
        #    print("the range a and b is to big. Decrease the interval.")
        #    return 
        
        # evaluate integral
        if b<self.minimum:
            #print(1)
            return 0.0
        
        elif a>self.maximum:
            #print(2)
            return 0.0
        
        elif b<=self.maximum and a>=self.minimum:            
            #print(3)
            fa = self.feval(a)            
            area = (b-a)*(fa)
            return area  
        
        elif a>=self.minimum and b>self.maximum:
            #print(4)
            fa = self.feval(a)
            area = (self.maximum-a)*(fa)
            return area
        else:
            #print(5)
            fb = self.feval(b)
            area = (b-self.minimum)*(fb)
            return area

#----------------------------------------------------------------

class PSD6:
    def __init__(self):
        ''' PSD properties
        '''
        self.number = 6 # number of PSD
        self.minimum = 0.15
        self.maximum = 3.3
        self.ymax = self.feval(self.minimum)		
        xunit = "ciclos/m"
        yunit = "m^2/(ciclo/m)"
     
    def feval(self, x):
        ''' evaluates PSD function at x
        x can be a float, a list or a numpy array
        '''
        y = []
        if isinstance(x,float):
            xlist = [x]
        else:    
            xlist = x
            
        for i in xlist:
            if i<self.minimum:
                y.append(0.0)
            elif i<=self.maximum:
                yval = 2.6E-3*i**(-1.6)
                y.append(yval)
            else:
                y.append(0.0)
        
        if isinstance(x,float):
            return y[0]
        else:
            return y
        
    def area(self,a,b):
        ''' evaluates the integral of PSD function at the interval a until b
        '''
        # check the input a and b
        if a>b:
            print("a must be greater than b")
            return 
        #elif b>self.maximum and a<self.minimum:
        #    print("the range a and b is to big. Decrease the interval.")
        #    return 
        
        # evaluate integral
        if b<self.minimum:
            #print(1)
            return 0.0
        
        elif a>self.maximum:
            #print(2)
            return 0.0
        
        elif b<=self.maximum and a>=self.minimum:            
            #print(3)
            area = 2.6E-3*(1.0/-0.6)*b**(-0.6)-2.6E-3*(1.0/-0.6)*a**(-0.6)
            return area  
        
        elif a>=self.minimum and a<=self.minimum and b>self.maximum:
            #print(4)
            area = 2.6E-3*(1.0/-0.6)*self.minimum**(-0.6)-2.6E-3*(1.0/-0.6)*a**(-0.6)
            return area
        else:
            #print(5)
            area = 2.6E-3*(1.0/-0.6)*b**(-0.6)-2.6E-3*(1.0/-0.6)*self.minimum**(-0.6)
            return area
