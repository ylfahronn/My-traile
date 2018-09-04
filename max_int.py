#max int = 0
#num_int = input a value
# count_int -= 1 will lower the number
#max_int = 0 will asign the 0 to the sum
# Do not change this line

num_int = int(input("Input a number: "))
max_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: ")) # Fill in the missing code
    if num_int > max_int:
        max_int = num_int

print("The maximum is", max_int)    # Do not change this line
