#!/usr/bin/env python
# coding: utf-8

# # PALINDROME PROBLEM:
# 
# Refer to README.md for problem details, assumptions, considerations, and testing results. 
# 

class Palindrome_Problem(): 
    
    def check_9(self,n):
       
       '''
       This function is responsible for Consideration 1.
       :n: (string) The integer we want to determine the palindrome for as a string
       :return: (int) Returns the p2 if a repetitive 9 value, otherwise returns 0 
       '''
       
       if (len(str(int(n)+1)) != len(str(int(n)))):          
           p2 = "1" + ((len(n)-1)*'0')+'1'
           return int(p2)
       else:
           return 0
    
    def check_10(self,n):
       
       '''
       This function is responsible for Consideration 2.
       :n: (string) The integer we want to determine the palindrome for as a string
       :return: (int) Returns the p3 if value starts with 1 and remaining values 
       are 0, otherwise returns 0 
       '''
       
       if (len(str(int(n)-1)) != len(str(int(n)))) or (int(n)==1):
           p3 = (len(n)-1)*'9'
           return int(p3)
       else:
           return 0   
    
    def check_10_1(self,n):
       
       '''
       This function is responsible for Consideration 6 by calling check_10.
       :n: (string) The integer we want to determine the palindrome for as a string
       :return: (int) Returns the p3 if value starts with 1 all middle values are 0,
       and the last value is 1, otherwise returns 0 
       '''
       
       p3 = self.check_10(str(int(n)-1))
       return int(p3)
    
    def min_palindrome(self,p1, p2, p3, n):
        
        '''
        This function is responsible for Consideration 3.
        :n: (string) The integer we want to determine the palindrome for as a string
        :p1: (int) palindrome without increasing or decreasing middle value(s)
        :p2: (int) palindrome associated with increasing middle value(s) by 1
        :p3: (int) palindrome associated with decreasing middle value(s) by 1
        :return: (int) Returns the smallest/nearest palindrome to n; p1, p2, or p3
        '''
        
        p1_abs = abs(int(p1)-int(n))
        p2_abs = abs(int(p2)-int(n))
        p3_abs = abs(int(p3)-int(n))
        
        if (p1_abs <= p2_abs) and (p3_abs <= p1_abs):
            return p3                    # p3<=p1<=p2
        elif (p1_abs <= p2_abs):
            return p1                    # p1<=p2<=p3 or p1<=p3<=p2
        elif (p3_abs <= p2_abs): 
            return p3                    # p3<=p2<=p1 
        else:
            return p2                    # p2<=p1<=p3
    
    def possible_palindromes(self,n):
    
        '''
        This function is responsible for Consideration 5.
        :n: (string) The integer we want to determine the palindrome for as a string
        :return: (list) Returns the 3 closest palindromes [p1,p2,p3]
        '''
            
        if (len(n) % 2) == 0:            # Consideration 5.1: Even case
            
            FH1 = n[0:len(n)//2]         # FH# = First Half of the palindrome associated with p# 
            p1 = FH1 + FH1[::-1]
            
            FH2 = str(int(FH1)+1)
            p2 = FH2 + (FH2[::-1])
            
            FH3 = str(int(FH1)-1)
            p3 = FH3 + (FH3[::-1])
            
            return [p1, p2, p3]
            
        else:                             # Consideration 5.2: Odd case
            
            FH1 = n[0:(len(n) + 1)//2]
            p1 = FH1 + (FH1[::-1])[1:len(FH1)]
            
            FH2 = str(int(FH1)+1)
            p2 = FH2 + (FH2[::-1])[1:len(FH2)]
            
            FH3 = str(int(FH1)-1)
            p3 = FH3 + (FH3[::-1])[1:len(FH3)]
            
            return [p1, p2, p3]
        
    def solution(self,n):
        
        '''
        This function calls possible_palindromes and min_palindrome to determine which of 
        the palindromes [p1, p2, p3] is the nearest to n; our solution
        :n: (string) The integer we want to determine the palindrome for as a string
        :return: (string) Returns the closest palindrome to n
        '''
        
        if len(n) < 2:                 # Consideration 4, nearest/smallest palindrome is 1 less
            return str(int(n)-1)       # than n 
        
        results = self.possible_palindromes(n) 
        
        p1 = results[0]
        p2 = results[1]
        p3 = results[2]
    
        if (p1 == n):                # p1 cannot be a solution because it is already a palindrome
            p1 = "0"                 # hence set it to zero to ensure the absolute difference b/w m1 
                                     # and n is as large as possible 
                
        if self.check_9(n) > 0:
            p2 = self.check_9(n)
            
        if self.check_10(n) > 0:
            p3 = self.check_10(n)
            
        if self.check_10_1(n) > 0:
            p3 = self.check_10_1(n)
            
        return str(self.min_palindrome(p1,p2,p3,n))
        

def main():
    
    p = Palindrome_Problem()
    '''
    Runs the full program using the preassigned user defined functions.
    '''
    
    prompt = "Please enter a number between 1 and 10^6..." + "\n"
    palindrome = input(prompt)
    print("The nearest palindrome for " + palindrome + " is " + 
          p.solution(palindrome) + ".")
    
main()
    
#TESTING speed, efficiency, and overall performance 
    
import random
import time

p = Palindrome_Problem()

def crash_testing():

    '''
    This function selects 100 random integers from the range 0<n<10^6 and returns the 
    corresponding palindrome solution. This function is intended to be run repeatedly to 
    ensure their are no integers in our range for which the algorithm will crash. 
    :return: (list) Contains only palindromes for the random integers. 
    '''
    
    palindromes = []
    for _ in range(100):
        
        random_int = str(random.randint(1,10**10))
        palindrome = p.solution(random_int)
        palindromes.append(palindrome)
        
    return palindromes


def runtime():
    
    '''
    This function determines the average runtime of the algorithm by calling
    and timing crash_testing. This function is used to determine time complexity. 
    :return: (int) Returns the average runtime of the algorithm. 
    '''
    n = 100                   # change n based on number of entries you want to time 
    total_time = 0.0          # since crash_testing determines the palindrome solutions for 
    for _ in range(n):        # 100 entries, we test n*100 entries in this function
        start = time.time()
        crash_testing()
        end = time.time()
        total_time = total_time+(end-start)
 
    #print(total_time)
    print("Algorithm runtime average for each entry is %10.7fms for n=%d"%((total_time/n)*10,n*100))


# Independent entries and results per entry
# 1000 = 0.0000780ms
# 10,000 = 0.00966ms  
# 100,000 = 0.00985ms 
# 1,000,000 = 0.0091009ms  
# 10,000,000 = 0.0088922ms 
# 100,000,000 = 0.009139ms

# Time Complexity (average run time per complete entry) is 0.009ms, constant time 

#crash_testing()
runtime() 
