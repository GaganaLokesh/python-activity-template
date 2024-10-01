file=open("example1.txt","a")
file.write("\nDear Dairy")
file.close()
with open("example1.txt", "r") as file:
    content = file.read()
print("File automatically closed after exiting the block.")