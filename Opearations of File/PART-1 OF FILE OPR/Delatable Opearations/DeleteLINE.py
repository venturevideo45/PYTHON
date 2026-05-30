file1 = open("Delatable Opearations\FPV2.txt", 'r')
file2 = open("Delatable Opearations\FPV1.txt", 'w')

for line in file1.readlines():


   if not (line.startswith('Coding')):

     print(line)

     file2.write(line)
