my_file = open("output2.txt", "w")  # write

for i in range(3):
    my_file.write("Hello World")

my_file.close()
