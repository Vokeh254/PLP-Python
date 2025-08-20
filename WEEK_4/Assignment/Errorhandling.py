try :
    file  = input("Enter your file name: ")
    with open(file, "r") as f:
        content = f.read()
        print ("File content read successfully.")
except FileNotFoundError:
    print("Error: File not found. Please check the file name and try again.")
except IOError:
    print("Error: Could not read file. Please check the file permissions and try again.")