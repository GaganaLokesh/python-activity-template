file=open("example1.txt","r")
for line in file:
    print("Line:",line.strip())

file.close()
