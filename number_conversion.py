
import os

def menu():
    #print what to input by number example: [1] = hexadecimal, [2] = octal, [3] = binary
    return """
Enter a number to convert: 
[1] Binary
[2] Octal 
[3] Decimal
[4] Hexadecimal 
[5] Exit
"""

continue_program = True


while continue_program:
    #get the number from the user
    print(menu())
    numberInput = str(input("Enter number: "))
    os.system('cls')
    
    if numberInput == "1":
        try:
            os.system('cls')
            binary_value = int(input("Enter binary number: "))
            decimal_value = int(str(binary_value), 2)
            octal_value = oct(decimal_value)[2:]
            hexadecimal_value = hex(decimal_value)[2:]
            
            print(f"input: {binary_value}")
            print(f"Octal value [8]: {octal_value}")
            print(f"Decimal value [10]: {decimal_value}")
            print(f"Hexadecimal value [16]: {hexadecimal_value}")            
            
            
        except ValueError as e:
            print(e)
            
    elif numberInput == "2":
        try:
            os.system('cls')
            octal_value = int(input("Enter octal number: "))
            decimal_value = int(str(octal_value), 8)
            binary_value = bin(decimal_value)[2:]
            hexadecimal_value = hex(decimal_value)[2:]
            
            print(f"input: {octal_value}")
            print(f"Binary value [2]: {binary_value}")
            print(f"Decimal value [10]: {decimal_value}")
            print(f"Hexadecimal value [16]: {hexadecimal_value}")
            
        except ValueError as e:
            print(e)
    
    elif numberInput == "3":
        try:
            os.system('cls')
            decimal_value = int(input("Enter decimal number: "))
            binary_value = bin(decimal_value)[2:]
            octal_value = oct(decimal_value)[2:]
            hexadecimal_value = hex(decimal_value)[2:]
            
            print(f"input: {decimal_value}")
            print(f"Binary value [2]: {binary_value}")
            print(f"Octal value [8]: {octal_value}")
            print(f"Hexadecimal value [16]: {hexadecimal_value}")
            
        except ValueError as e:
            print(e)

    elif numberInput == "4":
        try:
            os.system('cls')
            hexadecimal_value = input("Enter a hexadecimal number: ")
            decimal_value = int(hexadecimal_value, 16)
            binary_value = bin(decimal_value)[2:]
            octal_value = oct(decimal_value)[2:]

            print(f"input: {hexadecimal_value}")
            print(f"Binary value [2]: {binary_value}")
            print(f"Octal value [8]: {octal_value}")
            print(f"Decimal value [10]: {decimal_value}")
            
        except ValueError as e:
            print(e)
    elif numberInput == "5":
        os.system('cls')
        print("Goodbye!")
        break
    
    else:
        os.system('cls')
        print("Invalid input. Please try again.")
        continue
    
    try:
        # ask the user if they want to continue 1 = True, 0 = False
        continue_program = input("Do you want to continue? [1] Yes, [0] No: ")
        continue_program = eval(continue_program)
    except ValueError:
        # clear the screen and ask the user if they want to continue
        os.system('cls')
        print("Invalid input. THE PROGRAM WILL NOW EXIT.")
    
    if not continue_program:
        os.system('cls')
        print("Goodbye!")
        break
        
    