#https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

def isPalindrome(s: str) -> bool:

    # first pass add all chars to the list
    processed_list = []
    
    for c in s:
        if c.isalnum():
            processed_list.append(c.lower())
      
#    print(f"{processed_list}")
    total_chars = len(processed_list)
    
    for c in range(total_chars):
        other_end = total_chars - c - 1
        if c <= other_end:
            if processed_list[c] != processed_list[other_end]:
                return False
        else:
            return True

    return True


if __name__ == "__main__":
    
    s = "race a car"

    k = isPalindrome(s)
    print(f"k = {k}")
