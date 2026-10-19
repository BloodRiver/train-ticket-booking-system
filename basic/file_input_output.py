# How to write to text file


# open("filename.txt", "r")  # to read from the file. During this time, we can NOT write
# open("filename.txt", "w")  # to write to the file. During this time, we can NOT read from the file
# open("filename.txt", "a")  # write but append to the file.
my_file = open("output.txt", "w")

my_file.write("Hello World")


my_file2 = open("example.txt", "r")

file_content = my_file2.read()

print(file_content)

my_file2.close()

my_file.write("This is a test")

my_file.write("\n")
my_file.write("This is the newline\n")
my_file.write("We can write to files now!")

my_file.close()

my_file3 = open("output.txt", "w")  # overwrites the previous content with new content (all previous content is lost)

my_file3.write("Clean\n")

my_file3.close()

my_file4 = open("output.txt", "a")  # append

my_file4.write("This is a new addition to the file")

my_file4.close()

my_file5 = open("output.txt", "a")  # append - does not erase previous content. Simply adds new content to the end of the previous content
my_file5.write("Hello World")
my_file5.close()
