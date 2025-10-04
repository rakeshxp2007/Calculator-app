from calc_choices import do_addition, do_subtraction
from multiply import do_multiply
from division import do_division
from area import area


def main():
    print("Welcome to Calculator App")
    print("""\nSelect operation:
    1. Addition
    2. Subtraction
    3. Multiplication 
    4. Division
    5. Area of rectangle 
    6. Exit
    """)

    user_input = input("Enter choice(1/2/3/4/5/6): ")

    if user_input =='6':
        print("Exiting the program.")
        exit()
    else:
        a=float(input("Enter first number: "))
        b=float(input("Enter second number: "))

    if user_input == '1':
        result = do_addition(a, b)
    elif user_input == '2':
        result = do_subtraction(a, b)
    elif user_input == '3':
        result = do_multiply(a, b)
    elif user_input == '4':
        result = do_division(a, b)
    elif user_input =='5':
        result = area(a,b)
    print("Result: ", result)

if __name__ =="__main__":
    main()

