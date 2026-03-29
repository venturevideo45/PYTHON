number = int(input("ENTER ANY NUMBER FROM 0 - 50: "))
if number < 50  and number > 0:
             print("The number is between 0 and 50.")
else:
                 print("The number is not between 0 and 50.")
     
if number > 50 :
         print("The number is greater than 50.")

         if number % 2 == 0:
             print("The number is even.")

elif number % 2 != 0:
                print("The number is odd.")

else:
                print("The number is less than 50.") 