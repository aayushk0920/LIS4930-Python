import math
#compute and print roots of x2-5.86 x+ 8.5408
def main():
    print("This program will compute and print the roots of a quadratic equation.")
    a,b,c = eval(input("Enter the coefficients (a,b,c): "))
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    print("The solutions are :", root1, root2)
main()

#Use a for loop to print the decimal representations of 1/2, 1/3, ... 1/10 one on each line
for i in range(2, 11):
    print(f"1/{i} = {1/i}")
