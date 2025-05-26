#https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List

def candy(ratings: List[int]) -> int:
        ar_size = len(ratings)
        candy = [1] * ar_size

         # if there're less than 3 elements
        if ar_size == 1:
            return 1

        if ar_size == 2:
            if ratings[0] != ratings[1]:
                return 3
            else:
                return 2


        # Now for each child in line, we need to know the rankings of right neighbors

        for i in range(1, ar_size):
            if ratings[i] > ratings[i - 1]: # if rating is better than previous,  give this child more candy than the next neighbor has
                candy[i] = candy[i-1] + 1

        # Now let's do a second pass from right to left, this time comparing candy
        for i in range (ar_size - 2, -1, -1):
            if ratings[i] > ratings[i+1]: # if this rating is better,                
                candy[i] = max(candy[i+1] + 1, candy[i])

        output = sum(candy)                
        print(f"Output is {output}, candy array is {candy}")

        return output


def main():

    #ratings = [1,3,4,5,2]
    ratings = [3,2,1,1,4,3,3]
    output = candy(ratings = ratings)
    print(f"Final output: {output}")

if __name__ == "__main__":
    main()



    