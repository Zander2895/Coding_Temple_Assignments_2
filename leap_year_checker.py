leapy_the_year = int(input("Enter a Year: "))

if leapy_the_year % 4 == 0 and leapy_the_year % 100 != 0:
    print(f"{leapy_the_year} is a leap year.")
else:
    print(f"{leapy_the_year} is not a leap year.")