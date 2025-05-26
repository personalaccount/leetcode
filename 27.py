#https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

def main():

    nums = [0,1,2,2,3,0,4,2]
    val = 2; 
    k = 0

    cache_array = [] 

    for i in range(len(nums)):
        if nums[i] != val:
            k = k + 1
            cache_array.append(nums[i])
        nums[i] = ""
    
    cache_array.sort()

    for i in range(len(cache_array)):
        nums[i] = cache_array[i]

    print(f"K is {k}\n nums is {nums}")


if __name__ == "__main__":
    main()