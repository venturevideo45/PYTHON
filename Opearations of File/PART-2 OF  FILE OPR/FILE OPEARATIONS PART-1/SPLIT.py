with open('Spilt.txt','w') as f:
    f.write("This is the first line.\n")
    f.write("This is the second line.\n")
    f.write("This is the third line.\n")




with open('Spilt.txt','r') as f:
    data = f.readlines()
    print("Words in this File are:",)
    for line in data:
        word = line.split()
        print(word)
f.close()