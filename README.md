# LeetCode-Practice
Here I will include all of my Leetcode practice problems.

For Palindrome Problem:
The prompt was to test if a variety of integers were palindromes. The first thing I did was make the integers into a string. By doing this, I would be able to easily access each digit of the integer by using simple iteration techniques. If I had not done this, I would have likely had to use modulus to get access to the digits I would want to evaluate. Next, I knew given the nature of a palindrome, the first digit and last digit will be the same. Then all it took was the implementation of a simple for loop, where if the first and last digits were equal, it would add 1 to the iteration and subtract 1 from the max_len. This made it so the program would evaluate the next digits. If it goes through the loop enough times and never meets the false statement, it will return true as it is a palindrome. 
