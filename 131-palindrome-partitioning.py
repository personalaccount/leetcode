'''
Problem: 131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 
Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''

'''
Solution expalained:

Using a backtracking approach. 
Start with an empty partition, and for each substring of the given string "s" check if the substring is a palindrome. 

If it is, add the substring to the partition and recursively call the backtracking function with the next substring. 
If the entire string has been processed, add the partition to the result list. 

Finally, return the result list, containing all possible partitions of the given string "s" into palindromes.
'''

def partition(s):
    def backtrack(start, partition, result):
        if start == len(s):
            result.append(list(partition))
            return
        for i in range(start, len(s)):
            if s[start:i+1] == s[start:i+1][::-1]:
                partition.append(s[start:i+1])
                backtrack(i+1, partition, result)
                partition.pop()
    result = []
    backtrack(0, [], result)
    return result

s = "aababa"
print(partition(s))