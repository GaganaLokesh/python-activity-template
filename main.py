try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("The file does not exist.")