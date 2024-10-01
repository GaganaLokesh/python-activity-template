try:
    file = open("example1.txt", "r")
    content = file.read()
    file.close()
except Exception as e:
    print(f"An error occurred: {e}")
