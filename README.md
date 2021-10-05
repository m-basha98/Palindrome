# Palindrome Project 

A palindrome is a sequence that reads the same backwards as forwards (ie: racecar, 112211).

# Description 

A python based algorithm that given a string representing an integer, returns the nearest palindrome outside of itself as a string. 

**Example...**

Input: n = '123'    

Output: '121'

This project is a Junior Software Developer Challenge that is part of an interview procress. 

# Assumptions 

1. For simplicity and efficiency we assume digits are between 1 and 10^6, hence, no negative integers. 

2. There are only digits in the inputed value, that is, their are no letters, decimals, symbols, spaces, etc,.

3. No inputs start with a 0, such as '01234'. 

# Considerations 

Considerations are the unique scenerios or conditions that make the general algorithm not effective or in need of specific adaptations. 
Thus, these considerations are listed below and referred to later on in the code documentation for each function it directly relates to. 

1. Repetitive number 9's (9, 99, 999, 9999, ...); their nearest palindrome can be found by simply adding 2 to the integer (101, 1001, 10001, ...). 

2. Similarly, numbers like (1, 10, 100, 1000, ...); their nearest palindrome can be found by subtracting 1 to get (9, 99, 999, ...). 

3. Integers that are already a palindrome or are equidistant from 2 possible polindrome solutions need the nearest and smallest palindrome integer returned.

4. When the inputted integer is between (0,10), the integer less 1 is the nearest palindrome. 

5. Odd and even lengthed digits require different approaches. 

6. Similar to consideration 1. except the converse; from 1001 to 999, 101 to 99, and so on. 

# Testing 

All functions were tested individually; the crash_testing function confirmed the algorithms ability to consistently return results without failure 
within our assumed range. 

**Time Complexity of Algorthim**
- Runtime: ~0.009ms
- Constant time

**Space Complexity of Algorithm** 
- O(n) 

# Contributors 

- Manaal Basha (<manaal@ualberta.ca>)


