user = "Hank"

numbers = [int(n) for n in input("Enter numbers: ").split()]
print ("The list of numbers are: ", numbers)

avg = [sum(numbers) / len(numbers)]
print ("The average of the numbers is: ", avg)

n = [(a + b) / 2 for a, b in zip(numbers[::2], numbers[1::2])] #avg of two consecutive numbers
print ("The average of two consecutive numbers are: ", n)
