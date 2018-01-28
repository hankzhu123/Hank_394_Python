user = "Hank"

numbers = [int(i) for i in input("Enter numbers: ").split()] #ask user to give list of numbers
print ("The list of numbers are: ", numbers)

avg = [sum(numbers) / len(numbers)] #avg of total numbers from user input
print ("The average of the numbers is: ", avg)

n = [(a + b) / 2 for a, b in zip(numbers[::2], numbers[1::2])] #avg of two consecutive numbers
print ("The average of two consecutive numbers are: ", n)
