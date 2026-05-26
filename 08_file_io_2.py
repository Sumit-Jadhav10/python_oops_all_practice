# with open("first.txt","w") as f:
#     data = f.write("this is a line")
#     f.close()
# with open("seconds3.txt","w") as f:
#     f.write("this is the secound line i make today")
# with open("seconds3.txt","r") as f:
#     data = f.read()    
#     print(data)

# with open("secound4.txt","w+") as f:
#     f.write("this is the secound line i make today")
#     f.seek(0)
#     # data = f.read()
#     # print(data)
#     print(f.read())



# with open("secound5.txt","w+") as f:

#      f.write("this is the line i wanted to write todays")
#      f.seek(0)
#      data = f.read()
#      write = data.split()
#      print(len(write))



# with open("secound6.txt","a+") as f:
#     f.write("tis is first\nthis is second\nthis is third \n And this is last line\n")
#     f.seek(0)
#     data=f.readline()
#     print(len(data))

# with open("secound6.txt", "r") as f:
#     lines = f.readlines()
#     print(len(lines))


# with open("secound6.txt", "a+") as f:
#     # Write lines
#     f.write("this is first\nthis is second\nthis is third\nthis is last")
    
#     # Go back to start
#     f.seek(0)
    
#     # Count lines
#     count = 0
#     for line in f:
#         count += 1
    
#     print(count)

# with open("file1.txt", "w") as f:
#     f.write("hello,\nthis is the second line of the file \n and this is thord ")
# with open("file1.txt", "r") as f:
#     data = f.read().lower()
#     count = 0
    
#     for ch in data:
#         if ch in "aeiou":
#             count += 1
    
#     print("Vowels:", count)
#     f.close()

# with open("secoiund7.txt","w+") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java. \n I like programming in Java.\nApna C")
#     f.seek(0)
#     data =f.read()
#     writ = data.replace("Java","python")
#     print(writ)

# with open("second7.txt", "w+") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.\nApna C")
    
#     f.seek(0)
#     data = f.read()   # read actual content
    
#     new_data = data.replace("Java", "Python")
#     print(new_data)
def find_word_line(filename):
    with open(filename, "r") as f:
        line_no = 1
        
        for line in f:
            if "learning" in line:
                return line_no
            line_no += 1
    
    return -1


# Example usage
result = find_word_line("second7.txt")
print(result)