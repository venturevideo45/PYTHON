
file_read = open('MYMY.txt','r')
print("File in Read Mode-")
print(file_read.read())
file_read.close()

file_write = open('MYMY.txt', 'w')

file_write.write(" File in write mode ....")
file_write.write("Hil I am Jeswika. I am 8 yr. old ")
file_write.close()

file_append = open('MYMY.txt', 'a')

file_append.write("\n File in append mode ....")
file_append.write("And I am in 3rd class. I love to play with my friends.")
file_append.close()