#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) TIME: O(1) SPACE: O(1) - It is O(1) because even though we are using a while loop, the returned answer is only assigning a to the output of a + n \* n. Math like this is constant and is why it is O(1). We aren't printing anything, which could make it O(n), just assigning the variable and looping till that ends.

b) TIME: O(n) SPACE: O(1) - The function will grow longer as the input is longer, because it stops only when j no longer less than n. This would grow at a linear rate. However, the space complexity is O(1) because we are only ever using the four variables, `sum`, `i`, `j`, and `n`. There won't be anymore space used nor build up of the stack.

c) TIME: O(2n), so O(n), SPACE: O(n) - What we are doing in this function is first calculating how many bunnies there are, by calling the function minus 1 until we reach the base case, 0. Then we move back up the stack calling 2 + the number to return the amount of bunny ears. bunnyEars(40) will return 80 because 2 ears per bunny for 40 bunnines is 80. This is n multiplied by 2, drop the constant and you are left with O(n).

## Exercise II
