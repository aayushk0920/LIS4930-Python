#Greeting Function
def greet(name):
    print(f"Hello, {name}!")
    print(f"It's nice to meet you, {name}.")
    print(f"Have a great day, {name}!")

#List of names
names = ["Aayush Kumar", "Ella Anselmi", "Wray Martin"]

#Loop through the list and call the greet function
for name in names:
    greet(name)

#Full Name Function
def full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    print(f"Hello, {full_name}.")

#Call the function with the updated names
full_name("Aayush", "Kumar")
full_name("Ella", "Anselmi")
full_name("Wray", "Martin")

#Addition Calculator with Printing Inside the Function
def add_and_print(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")

#Call the function with three different sets of numbers
add_and_print(5, 10)
add_and_print(20, 30)
add_and_print(100, 200)

#Return Calculator with Printing Outside the Function
def add_and_return(num1, num2):
    return num1 + num2

#Call the function and print the result outside the function
result1 = add_and_return(5, 10)
print(f"The sum of 5 and 10 is {result1}.")

result2 = add_and_return(20, 30)
print(f"The sum of 20 and 30 is {result2}.")

result3 = add_and_return(100, 200)
print(f"The sum of 100 and 200 is {result3}.")

#Expression Evaluation
result = pow(16, (1/2))
print(result)  # This will correctly print 4.0

#Defining Variables
x = [1, 2, 3, 4, 5]
y = [11, 12, 13, 14, 15]
z = (21, 22, 23, 24, 25)
