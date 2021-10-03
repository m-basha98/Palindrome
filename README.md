# Palindrome Project 

A palindrome is a sequence that reads the same backwards as forwards (ie: racecar, 112211).

# Description 

A python based algorithm that given a string representing an integer, returns the nearest palindrome outside of itself as a string. 

**Example...**

Input: n = '123'    

Output: '121'

This project is a Junior Software Developer Challenge that is part of an interview procress. 

# Assumptions 

1. For simplicity and efficiency we assume digits are under 10^10. 

2. There are only digits in the inputed value, that is, their are no letters, decimals, symbols, etc,.

3. No inputs start off with a 0, such as '01234', as it affects incrementation based on mathematic principles. 

4. We assume no negative numbers with the lowest digit being 1 and the largest being 10^10. 

# Considerations 

Considerations are the unique scenerios or conditions that make the general algorithm not effective or in need of adaptations. 
Thus, they are listed below and referred to later in the code documentation for each function it directly relates to. 

1. Repititive number 9's (9, 99, 999, 9999), their nearest palindrome can be found by simply adding 2 to the number to get (101, 1001, 10001). 

2. Similarly, numbers like (1, 10, 100, 1000), their nearest palindrome can be found by subtracting 1 to get (9, 99, 999). 

3. Numbers that are already a palindrome still need the nearest smaller palindrome number determined for it.

4. Approach for when n is 0 < n < 10, n less 1 is the nearest palindrome. 

5. There will be different approaches for odd and even lengthed digits. 

6. Similar to part 1. except the converse; from 1001 to 999, 101 to 99, and so on. 

# Contributors 

- Manaal Basha (<manaal@ualberta.ca>)


