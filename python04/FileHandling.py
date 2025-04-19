import os

# WRITE FILE & CREATE DEFULT
file = open("Demo_File.txt", "w")
write_file = file.write("My Name Is Huzaifa \n My Father Name Is Huzaifa Abdulrab")
print(f"# Create file Method {write_file}")
file.close()


# READ FILE DATA

file = open("Demo_File.txt", "r")
read_file = file.read()
print(f"# Read File Methos{read_file}")
# file.close()


# READ FILE DATA LINE BY LINE

file.seek(0)
lines = file.readline()
print(f"# Read File Data Line By Line {lines}")
# file.close()

# LOOPS METHOD

file.seek(0)
lines = file.readlines()
for line in lines:
    print(f"# Loop Method : {line}")

for line in open("Demo_FIle.txt","r"):
    print(f"# Simple Method {line.strip()}")


#SIMPLE EASY METHOD TO FILE READ AND CLOSE
with open("Demo_File.txt" , "r") as file:
    print(file.read())

file.close()

#PROBLEM NO 1 :  WRITE FILE & CREATE DEFULT 
def copy_file(source , disk):
    try:
        with open (source , 'r') as s, open (disk , "w") as d:
            d.write("Created by Huzafa Abdulrab")
            for line in s:
                d.write(line)
            print("File Copy Sucessfully")
    except FileNotFoundError:
        print("File Not Found")

copy_file("Demo_File.txt" ,"Demo_File_Copy.txt")