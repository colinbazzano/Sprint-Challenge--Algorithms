#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) TIME: O(1) SPACE: O(1) - It is O(1) because even though we are using a while loop, the returned answer is only assigning a to the output of a + n \* n. Math like this is constant and is why it is O(1). We aren't printing anything, which could make it O(n), just assigning the variable and looping till that ends.

b) TIME: O(n) SPACE: O(1) - The function will grow longer as the input is longer, because it stops only when j no longer less than n. This would grow at a linear rate. However, the space complexity is O(1) because we are only ever using the four variables, `sum`, `i`, `j`, and `n`. There won't be anymore space used nor build up of the stack.

c) TIME: O(2n), so O(n), SPACE: O(n) - What we are doing in this function is first calculating how many bunnies there are, by calling the function minus 1 until we reach the base case, 0. Then we move back up the stack calling 2 + the number to return the amount of bunny ears. bunnyEars(40) will return 80 because 2 ears per bunny for 40 bunnines is 80. This is n multiplied by 2, drop the constant and you are left with O(n).

## Exercise II

The variables we have are:

number of floors in the building (total): n
floor = f, if an egg is thrown off of floor f or higher, it will break
less than floor f, it will not break.

We know that floor 0 is the ground, and an egg will no break on that floor. It if did, there are no viable floors for egg throwing.

A question I would ask if being asked to solve this would be: Will I know when an egg is broken from a floor?

If I do know the state of the egg upon returning, I would have a base case that is if `f == 0` return because we are on the floor, as well as when the egg is returned `broken`. This way, I would climb up the floors and call the function again with the floor + 1. Climb up the floors until an egg is returned broken which I would then know is the first floor that eggs cannot be thrown from, as each floor above would also return a broken egg.

The recursive function can continue to call itself so long as the egg is returned unbroken, otherwise we would want to break out of the function and return the broken egg.
