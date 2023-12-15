""" Recursive solution with DP. Works well here since
for each index we will look for substrings that can
match pattern. 

so for example if we find out combinations(4, 1) doesnt work
for e.g. 

???.### 1, 1, 3

We will start checking ??#.### seing that combinations(4, 1) doesnt work
by recursing down to the end of the string but then we will also check
?#?.### but we dont have to recurse the entire way. Same thing for
#??.###. Obviously for large strings with lots of combinations this
will reduce processing by a lot.

Key insight being the recursive nature of a problem like
1."find the possible pattern matches of this string" well for
each substring there will be a new string which means apply 1 again,
i.e. recursion. But then also utilizing DP to actually make it computable.

To have that solution in your mind you need to be familiar with recursion, DP
but also the patterns that appear in the recursiveness of the solution
to realize that DP will drastically reduce runtime. You can of course
take a guess and see how it performs.
"""

from functools import cache
def run_combinations(line):
    chars, pattern = line.split()
    chars, pattern = (chars + '?')*5, eval(pattern)*5

    @cache
    def combinations(i, j, c=0):
        if i == len(chars):
            # Recursion stops here and
            # if we have managed to create
            # all groups, i.e. j == len(pattern)
            # that means we have one more combination
            # that works for the pattern
            return j == len(pattern)

        # coming here means we have essentially tried the
        # non #-path of current ?
        try:
            # if we can match the entire group we continue
            if chars[i] in '?#' and '.' not in chars[i:i+pattern[j]] and chars[i+pattern[j]] in '?.':
                # matching the current pattern group
                # means we eat up to the final index
                # and move on to the next group
                c += combinations(i+pattern[j]+1, j+1)
        except IndexError:
            pass

        if chars[i] in '.?':
            # we start recursing with the option of 
            # selecting ? as a #. When we return
            # we will do the opposite
            c += combinations(i+1, j)

        return c

    return combinations(0, 0)

print(sum(map(run_combinations, open("d12/input.txt"))))
