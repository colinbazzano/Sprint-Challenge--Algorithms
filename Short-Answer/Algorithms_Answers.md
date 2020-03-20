#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) - There are three major things happening in this code. We are assigning a value to the variable a, using a while loop and in that loop reassigning the value of a to a mathematic function. If we drop constants, we are left with O(n) for the length of the while loop.

b) O(n\*\*2) - We first assign the sum variable the value of 0. We loop through the range of the variable n (which is O(n)) and assign a variable j to 1. Inside of that for loop, we are performing a while loop in which we are comparing j (which is 1) to the variable n (our range). We are modifying both the j and sum in the while loop, so it's bes to keep track of those and then to count the time complexity, we will multiply the loops together, and then drop constants, leaving us with O(n^2).

c) O(n) - I would believe that in Big O notation, this last question is linear. The function is being called recursively n (or in this case, bunnies) amount of times before reaching the base case.

## Exercise II
