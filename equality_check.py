smallest_num = int(input("Enter the first number: "))
middle_num = int(input("Enter the second number: "))
greatest_num = int(input("Enter the third number: "))

if smallest_num <= middle_num and smallest_num <= greatest_num:
    print("The first number is the smallest number. " + str(smallest_num))
elif smallest_num < middle_num and smallest_num > greatest_num:
    print("The first number is the midddle number. " + str(smallest_num))
elif smallest_num  > middle_num and smallest_num > greatest_num:
    print("The first number is the greatest number. " + str(smallest_num))

if middle_num < smallest_num and middle_num < greatest_num:
    print("The second number is the smallest number. " + str(middle_num))
elif middle_num > smallest_num and middle_num < greatest_num:
    print("The second number is the midddle number. " + str(middle_num))
elif middle_num  > smallest_num and middle_num > greatest_num:
    print("The second number is the greatest number. " + str(middle_num))

if greatest_num < middle_num and greatest_num < smallest_num:
    print("The third number is the smallest number. " + str(greatest_num))
elif greatest_num > middle_num and smallest_num > greatest_num:
    print("The third number is the midddle number. " + str(greatest_num))
elif greatest_num  > middle_num and smallest_num < greatest_num:
    print("The third number is the greatest number. " + str(greatest_num))

if smallest_num == middle_num:
    print("There are two equal numbers. " + str(smallest_num))
elif smallest_num == greatest_num:
    print("There are two equal numbers. " + str(smallest_num))
elif middle_num == greatest_num:
    print("There are two equal numbers. " + str(middle_num))
elif smallest_num == middle_num and smallest_num == greatest_num:
        print("All three are equal. " + str(smallest_num))
else:
    print("Two numbers are equal and the largest is. " + str(greatest_num))