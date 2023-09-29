# This is the script you would execute, like
#    python main_script.py


# Let us import some functions you wrote in
# auxiliary_functions.py
import auxiliary_functions

# Alterantively, you can load specific functions with
# from auxiliary_functions import tentimes


# Here we define some auxiliary functions in the 
# script we would exectue:
def square_number(num):
	res = num**2
	return res


def odd_number(num):
	if num%2:
		print(num, "is odd")
	else:
		print(num, "is even")


# This is the "main" part of the script
# Version 1: "Main" part directly after
# function definitions
my_number = 5

the_result = square_number(my_number)

print("The result of", my_number, "squared is", the_result)

odd_number(my_number)

my_number_x10 = auxiliary_functions.tentimes(my_number)

print("Output of tentimes auxiliary function for", my_number, ":", my_number_x10)

my_number_sign = auxiliary_functions.num_sign(my_number)

print("Output of num_sign auxiliary function for", my_number, ":", my_number_sign)






# V2: This is the nicer way to distinguish 
# between the function part and the 
# "main" part of the script
# if __name__ == '__main__':

# 	my_number = 5

# 	the_result = square_number(my_number)

# 	print("The result of", my_number, "squared is", the_result)

# 	odd_number(my_number)

# 	my_number_x10 = auxiliary_functions.tentimes(my_number)

# 	print("Output of tentimes auxiliary function for", my_number, ":", my_number_x10)

# 	my_number_sign = auxiliary_functions.num_sign(my_number)

# 	print("Output of num_sign auxiliary function for", my_number, ":", my_number_sign)
