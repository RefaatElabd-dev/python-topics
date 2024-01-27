#!/bin/python3

import re

if __name__ == '__main__':
    N = int(input().strip())
    ans = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        if(re.match(".+@gmail\.com", emailID)):
            ans.append(firstName)
    
    print("\n".join(sorted(ans)))
    
