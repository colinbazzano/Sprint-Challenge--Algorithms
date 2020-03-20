#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) - There are three major things happening in this code. We are assigning a value to the variable a, using a while loop and in that loop reassigning the value of a to a mathematic function. If we drop constants, we are left with O(n) for the length of the while loop.

b) O(n\*\*2) - We first assign the sum variable the value of 0. We loop through the range of the variable n (which is O(n)) and assign a variable j to 1. Inside of that for loop, we are performing a while loop in which we are comparing j (which is 1) to the variable n (our range). We are modifying both the j and sum in the while loop, so it's bes to keep track of those and then to count the time complexity, we will multiply the loops together, and then drop constants, leaving us with O(n^2).

c) O(n) - I would believe that in Big O notation, this last question is linear. The function is being called recursively n (or in this case, bunnies) amount of times before reaching the base case.

## Exercise II

number of floors in the building = n
floor f, if egg is thrown off of floor f or higher, it will break
less than floor f, it will not break

I would begin by setting the base cases, 0 aka the ground. I would inquire about whether or not you could throw any egg on the ground level floor, but either way we know that it will not break as if it could that would be floor f and no floor above would be viable for egg throwing.

We are trying to minimize the amount of eggs thrown/broken, so I would think it would be best to increment until the egg is broken, which could be our next base case. I suppose that it would depend on if I know whether or not the eggs return broken/unbroken.

If the last sentence above is the case and I do know how they return

I would loop through the range of n and for each loop check if we are at 0 (for our base case) as well as if the egg is broken, if not, recursively call the function again but with n + 1 indicating we have gone up a floor and tested again.
