# AdventOfCode2022
My solutions for the puzzles in [adventofcode.com](https://adventofcode.com/2022) for the 2022 December season.

These 25 holiday-themed thought-provoking puzzles allow a participant to code in any language to get an numerical answer to the day's puzzle based on their unique-per-user input.

### My Participation
My solutions are written in `Python` and my specific input is kept in an `input.in` file within the `Day#` folder along with the `.py` file.
I run in terminal in the `Day#` folder to allow the script to recognize the input.in file.

### Concepts I Used/Learned
***Day 1***: file i/o, stripped empty lines (from a file) are empty strings

***Day 2***: maps, modular-usage for cyclic ideal of Rock-Paper-Scissors

***Day 3***: set intersection operation in python is very simply `setA & setB`

***Day 4***: interval intersections, for simplification of intersecting condition, we can do `swap((a, b), (c, d)) if c < a` => `a, b, c, d = c, d, a, b` (nice "pythonic" swap).

***Day 5***: stack operations, adding one stacks popped elements to anothers in 2 different orders. 
**TODO**: update input method (currently harcoded input, make general probably using `mod 4` to avoid brackets and account for each space between)

***Day 6***: # distinct elements in sliding window of 2 diff lengths for the two parts of todays puzzle. I generalized with single `p(signal_length)` function since the only difference between the two parts was the sliding window's length

***Day 7***: Spent some time on this one. **Main thing: good idea to have default constructors for classes**, otherwise can give error for example when we have it as the value in the key-value pairs in map. also important for this problem was the fact that directories can be in different locations but *same* name.

***Day 8***: While this question is very simple to do in `O(n^3)`, that is quite boring. So, I reduced part 1 of the puzzle by a linear factor, ie time complexity `O(n^2)`. We do this by using iterating over whole array (row) and *keeping track of max and using that to check whether a tree would be visible*. However, for part 2, I just did `O(n^3)`. 