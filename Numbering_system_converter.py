#mohamed ahmed abdelfattah mohamed id:20230314


def from_decimal_to_converter(num, target_base, size=0):
    result = ''
    hexa_list = ['A', 'B', 'C', 'D', 'E', 'F']
    num = int(num)
    target_base = int(target_base)
    size = int(size)

    # Convert the number to the desired system
    while num > 0:
        remainder = num % target_base
        if remainder > 9:
            remainder = hexa_list[remainder - 10]
        num = int(num / target_base)
        result = str(remainder) + result

    # Optional size adjustments, default is 0
    while len(result) < size:
        result = '0' + result
    return result


def to_decimal_from_converter(num, source_base):
    result = 0
    num = str(num)
    hexa_list = ['A', 'B', 'C', 'D', 'E', 'F']

    # Convert the number to decimal
    for i in range(len(num)):
        # Convert letters from hexadecimal
        digit = num[-i - 1]
        if digit in hexa_list:
            digit = 10 + hexa_list.index(digit)

        # Calculate the final result
        result += int(digit) * (int(source_base) ** i)
    return result


choices_list = ['A', 'B', 'C', 'D']
wrong_list = ['-', ',', '.', ' ', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
decision_list = [0, 0, 'B', 0, 0, 0, 0, 0, 'C', 0, 'A', 0, 0, 0, 0, 0, 'D']

# Menu 1
print("Welcome to the numbering system converter.")
while True:
    # Repeat the menus until the user chooses to exit
    user_decision_1 = str.capitalize(input("A) Insert a new number\n"
                                           "B) Exit program\n"))

    if user_decision_1 == 'A':
        user_number = str.upper(input("Please insert a number: "))

        # Check if the number is in the correct form
        while any(wrong in user_number for wrong in wrong_list) or not user_number:
            user_number = str.upper(input("Please enter a positive integer: "))

        # Menu 2
        print("Choose the base of the input number:")
        while True:
            user_decision_2 = str.capitalize(input("A) Decimal\n"
                                                   "B) Binary\n"
                                                   "C) Octal\n"
                                                   "D) Hexadecimal\n"))

            # Check for correct number base form
            if user_decision_2 == 'A':
                while not all(num in '0123456789' for num in user_number):
                    user_number = input("Please insert a valid decimal number: ")

            elif user_decision_2 == 'B':
                while not all(num in '01' for num in user_number):
                    user_number = input("Please insert a valid binary number: ")

            elif user_decision_2 == 'C':
                while not all(num in '01234567' for num in user_number):
                    user_number = input("Please insert a valid octal number: ")

            elif user_decision_2 == 'D':
                while not all(num in '0123456789ABCDEF' for num in user_number):
                    user_number = str.upper(input("Please insert a valid hexadecimal number: "))
            else:
                print("Please enter a valid option!")
            user_decision_2 = decision_list.index(user_decision_2)
            break

        # Menu 3
        print("Choose the target base for conversion:")
        while True:
            user_decision_3 = str.capitalize(input("A) Decimal\n"
                                                   "B) Binary\n"
                                                   "C) Octal\n"
                                                   "D) Hexadecimal\n"))

            if user_decision_3 in choices_list:
                user_decision_3 = decision_list.index(user_decision_3)
                break
            print("Please enter a valid option!")

        # Converter functions
        result = to_decimal_from_converter(user_number, user_decision_2)
        result = from_decimal_to_converter(result, user_decision_3)

        print(f"Result = {result}\n")

    elif user_decision_1 == 'B':
        print("You exited the program. Goodbye!")
        break
    else:
        print("Please enter a valid option!")
