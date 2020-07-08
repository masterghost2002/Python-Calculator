########################## Creating Calculator using Lambda Fuunction ####################################33
add= lambda x, y: x+y
minus= lambda x, y: x-y
division= lambda x, y: x/y
multiplication= lambda x, y: x*y
power= lambda x, y: x**y
###################### We use lamba function to convert a function in one line function ############
"""
                    Like if we want to create a function which add 2 number then we will write like this
                    def add(x, y):
                       return x + y 
                    
                    but lambda can be use any where you can  while the help of single  line 
                     like 
                     add= lambda x, y: x+y   
"""
######################  Calculator Part            ###############################################
######################  Calculator Part            ###############################################
print("1.Addition(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\n5.Power(**)\n6.q for Exit" )
operation= input("Enter the operation You Want to Perform\n")
while operation != "q":
    if operation == "+":
        number_1 = float(input("Enter 1st Number\n"))
        number_2 = float(input("Enter 2nd Number\n"))
        print(f"The sum of {number_1} and {number_2} is: ", add(number_1, number_2))
    elif operation == "-":
        number_1 = float(input("Enter 1st Number\n"))
        number_2 = float(input("Enter 2nd Number\n"))
        print(f"The difference of {number_1} and {number_2} is: ", minus(number_1, number_2))
    elif operation == "*":
        number_1 = float(input("Enter 1st Number\n"))
        number_2 = float(input("Enter 2nd Number\n"))
        print(f"The product of {number_1} and {number_2} is: ", multiplication(number_1, number_2))

    elif operation == "/":
        number_1 = float(input("Enter 1st Number\n"))
        number_2 = float(input("Enter 2nd Number\n"))
        print(f"The division of {number_1} and {number_2} is: ", divide(number_1, number_2))
    elif operation == "**":
        number_1 = float(input("Enter Number\n"))
        number_2 = float(input("Enter How Much Power You want to raise\n"))
        print(f"The power of {number_1} rasie to {number_2} is: ", power(number_1, number_2))
    else:
        print("Thank You For Using\n")
########################################################################################################################
a = input()
########################### Lamba Function Calculator Rakesh Dhariwal ##############################################