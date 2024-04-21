num_1 = int(input("Enter your first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

if num_1  > num_2 and num_1 > num_3:
    print("The first number is the greatest number. " + str(num_1))
elif num_1 > num_2 and num_1 > num_3:
    print("The first number is the midddle number. " + str(num_1))
elif num_1 < num_2 and num_1 < num_3:
    print("The first number is the smallest. " + str(num_1))

if num_2  > num_1 and num_2 > num_3:
    print("The second number is the greatest. " + str(num_2))
elif num_2 > num_1 and num_2 < num_3:
    print("The second number is the midddle number. " + str(num_2))
elif num_2 < num_1 and num_2 < num_3:
    print("The second number is the smallest. " + str(num_2))

if num_3  > num_2 and num_1 < num_3:
    print("The third number is the greatest. " + str(num_3))
elif num_3 > num_2 and num_1 > num_3:
    print("The third number is the midddle number. " + str(num_3))
elif num_3 < num_2 and num_3 < num_1:
    print("The third number is the smallest. " + str(num_3))
