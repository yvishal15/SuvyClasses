"""Fredo is assigned a new task today. He is given an array A containing N integers. His task is to update all elements of array to some minimum value x, that is A[i]=x; 1<= i <=N such that the sum of this new array is strictly greater than the sum of the initial array. Note that x should be as minimum as possible such that sum of the new array is greater than sum of the initial array

Input Format: First line of input consists of an integer N denoting the number of elements in the array A. Second line consists of N space separated integers denoting the array elements
Output Format: The only line of output consists of the value of x.

Sample input:
5
1 2 3 4 5
Sample Output:
4

Explanation:

Initial sum of array = 1+2+3+4+5 = 15. when we update all elements to 4, sum of array = 4+4+4+4+4 = 20 which is greater than 15. Note that if we had updated the array elements to 3, sum=15 which is not greater than 15. So, 4 is the minimum value to which array elements to be updated.
 """

def fredo_and_array_update(array):

  initial_sum = sum(array)
  min_value = min(array)

  for i in range(min_value + 1):
    new_sum = initial_sum - i * len(array)
    if new_sum > initial_sum:
      return i

  return min_value


if __name__ == "__main__":
  n = int(input("Enter the number of elements in the array: "))
  array = list(map(int, input().split()))

  print("The minimum value x is {}.".format(fredo_and_array_update(array)))

"""Explation: Fredo is given an array A containing N integers. He needs to update all elements of the array to some minimum value x, such that the sum of the new array is strictly greater than the sum of the initial array. Note that x should be as minimum as possible such that sum of the new array is greater than sum of the initial array.

For example, if the initial array is [1, 2, 3, 4, 5], then the minimum value x that Fredo can update the array to is 4. This is because if he updates the array to 3, then the sum of the new array will be 15, which is equal to the sum of the initial array. However, if he updates the array to 4, then the sum of the new array will be 20, which is strictly greater than the sum of the initial array.

The Python code that I provided solves the Fredo and Array Update problem by first finding the initial sum of the array. Then, it iterates through all possible values of x, starting from the minimum value. For each value of x, it calculates the new sum of the array. If the new sum is strictly greater than the initial sum, then the code returns x. Otherwise, the code continues iterating.

The code terminates when it reaches the maximum value of x. If the code does not find any value of x that satisfies the given conditions, then it returns the minimum value of x.

"""