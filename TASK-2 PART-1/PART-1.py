"""Part 1:
Little Shino loves maths, today her teacher gave her two integers. Shino is now wondering how many integers can divide both the numbers. She is busy with her assignments. Help her to solve the problem

Input: Two number 'a' and 'b' are: 10 15
Ouput: Print the number of common factors of 'a' and 'b'  """


def print_common_factors(a, b):

  common_factors = set()
  for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
      common_factors.add(i)

  return len(common_factors)


if __name__ == "__main__":
  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))

  print("The number of common factors of {} and {} is {}".format(a, b, print_common_factors(a, b)))


""" EXPLATION : The code first asks the user to enter two numbers, a and b. Then, it uses a for loop to iterate through all the numbers from 1 to min(a, b). For each number, it checks if a and b are both divisible by that number. If they are, then it adds that number to a set called common_factors.

After the for loop has finished iterating, the code returns the length of the common_factors set. This is the number of common factors of a and b.

For example, if the user enters 10 and 15, then the code will iterate through the numbers from 1 to 15. It will find that 10 and 15 are both divisible by 1, 2, 5, and 10. Therefore, the common_factors set will contain 4 elements. The code will then return 4, which is the number of common factors of 10 and 15.

"""