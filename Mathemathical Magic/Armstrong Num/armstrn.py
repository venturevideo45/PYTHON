number = int(input("Enter a number: "))

digit = len(str(number))

resultnumber = 0

temp = number
while temp > 0:
    digit = temp % 10
    resultnumber += digit ** digit
    temp //= 10

if resultnumber == number:
    print(number, "is an Armstrong number")

else :
    print(number, "is not an Armstrong number")
      
