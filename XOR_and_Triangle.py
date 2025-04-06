'''
Problem link: https://codeforces.com/problemset/problem/2074/C

Difficulty: 1100 / 3-C

Given some x, y should satisfy the given inequalities:
y < x -- (1)
x + y > x^y -- (2)
x + x^y > y -- (3)
y + x^y > x -- (4)

Using bitmasking, we can write (2) as:
x^y + 2*(x & y) > x^y
=> x & y > 0
Which would imply that y must have atleast one turned on bit that is also found in x

Using bitmasking, we can (4) as:
y + x + y - 2*(x & y) > x
=> 2y > 2*(x & y)
=> y > x & y
Which would imply that y must have atleast one turned on bit that is not found in x

Given these inferences, we can calculate y turning on only two bits. One bit which is found in x, and another which is not.
Thus, the answer y but have atleast two bits, but y < x, thus x-1 must have atleast two bits
=> Solution does not exist if x <= 3 -- edge (1)

Also, to compute y, x must have atleast one turned off bit, that is x cannot be of the form 111...111
=> Solution does not exist if there exists n such that x = 2^n - 1 -- edge (2)

Finally, if x is of the form 1000...000, there is only one choice (which is the MSB) for the common bit that needs to be turned on in y, but it's also required at the same time to turn on another bit--this would make y > x, which contradicts our requirements for y.
=> Solution does not  exist if there exists n such that x = 2^n -- edge (3)                            

Except for the above three edge cases, we can calculate y easily by just starting with y = 0, and finding one turned off and one turned on bit in x, and turning them on in y using bitmasking techniques
  
Time complexity: O(log(n))
Space complexity: O(1)
'''

def solve():
    x = int(input())
    if x <= 3: # Handles edge (1)
        print(-1)
        return
    
    y = 0
    found_common = False
    found_different = False
    
    
    for i in range(12): # Input condition for problem: x < 2000 => number of bits in x < 11
        if found_common and found_different: # Prints y when the two required bits are turned on
            print(y)
            return

        if (1 << i >= x-1): # Handles edge (2) and (3) and breaks the loop if the bit we are on is 
            print(-1)
            return
        
        if not (x & (1 << i)) and not found_different: # Checks for turned off bit in x--if true, turns it on in y
            y |= (1 << i)
            found_different = True
        
        if (x & (1 << i)) and not found_common: # Checks for truned on bit in x--if true, turns it on in y
            y |= (1 << i)
            found_common = True

p = int(input())
for _ in range(p):
    solve()
