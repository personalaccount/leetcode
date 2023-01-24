'''
Given a string "s", partition "s" such that every substring of the partition is a palindrome. 
Return the minimum cuts needed for a palindrome partitioning of "s". 

Example:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''

def minCut(s):
    n = len(s)
    # dp[i] stores the minimum cuts needed for the substring s[:i+1]
    dp = [0] * n
    for i in range(n):
        min_cut = i
        for j in range(i + 1):
            if s[j:i + 1] == s[j:i + 1][::-1]:
                min_cut = 0 if j == 0 else min(min_cut, dp[j - 1] + 1)
        dp[i] = min_cut
    return dp[-1]

s = "aab"
print(minCut(s))