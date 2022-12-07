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

***Day 5***: stack operations, adding one stacks popped elements to anothers in 2 different orders. TODO: update input method (currently harcoded input, make general probably using `mod 4` to avoid brackets and account for each space between)

***Day 5***: # distinct elements in sliding window of 2 diff lengths for the two parts of todays puzzle. i generalized with single `p(signal_length)` function since the only difference between the two parts was the sliding window's length
